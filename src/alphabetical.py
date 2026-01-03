import re
from collections import defaultdict
from urllib.parse import urlparse, urlunparse


def convert_to_title_case(readme_text):
    # Only title-case bracketed text that is immediately followed by '(' —
    # this targets the link text portion in Markdown like [Name](url)
    def _tc_match(m):
        inner = m.group(1)
        # Use a robust split that treats common whitespace (including NBSP) as separators
        tokens = re.split(r"[\s\u00A0]+", inner)
        cleaned_tokens = []
        for t in tokens:
            # strip common punctuation that may be attached to tokens
            stripped = t.strip("()[]{}.,:;\"'`—–-")
            if stripped == "":
                # nothing left after stripping punctuation
                continue
            # Option B: only remove 'Aaa' when it's a separate token (case-insensitive)
            if stripped.lower() == "aaa":
                # drop standalone 'Aaa' token
                continue
            if re.fullmatch(r"(?i)[A-Za-z]", stripped):
                # drop standalone single-letter tokens (e.g. 'A', 'B', 'x')
                continue
            cleaned_tokens.append(stripped)
        if not cleaned_tokens:
            # If removing single-letter tokens would leave the bracket empty,
            # fall back to the original behavior (title-case the original text)
            return f"[{inner.title()}]"
        processed = " ".join(cleaned_tokens).strip()
        return f"[{processed.title()}]"

    # Use a lookahead to ensure we only match bracket text that precedes a (
    return re.sub(r"\[([^]]+)](?=\()", _tc_match, readme_text)


def find_duplicate_lines(lines, ignore_case=False, ignore_trailing_whitespace=True):
    """Return a dict mapping a representative original line text -> list of 1-based line
    numbers where duplicates (by normalization) appear.

    By default, the normalization ignores trailing whitespace (so "foo\n" and
    "foo " are treated as duplicates). Pure-empty lines are ignored. Matching is
    case-sensitive unless `ignore_case=True` is passed explicitly.
    """
    positions = defaultdict(list)
    representative = {}

    for idx, line in enumerate(lines, start=1):
        if line is None:
            continue
        if line.strip() == "":
            # ignore pure-empty lines
            continue

        key = line
        if ignore_trailing_whitespace:
            # remove trailing whitespace/newline but preserve leading whitespace
            key = key.rstrip()
        if ignore_case:
            key = key.lower()

        positions[key].append(idx)
        # keep the first-seen original text for preview
        if key not in representative:
            representative[key] = line

    # Build duplicates keyed by representative original line text
    duplicates = {representative[k]: v for k, v in positions.items() if len(v) > 1}
    return duplicates


def sort_lists_alphabetically(lines):
    header_pattern = re.compile(r"^##\s+([A-Z])")
    # Remove a trailing slash from captured http(s) URLs even when the slash is
    # immediately followed by a closing parenthesis (e.g. Markdown link) or
    # whitespace or end-of-line. Uses a lookahead so the ')' remains in the
    # surrounding text.
    http_pattern = re.compile(r"(http[s]?://[^\s/]+)/(?=[)\s]|$)")
    current_header = None
    list_items = []
    sorted_lines = []
    header_indices = []

    for i, line in enumerate(lines):
        # Remove trailing `/` from http links
        line = http_pattern.sub(r"\1", line)

        header_match = header_pattern.match(line)
        if header_match:
            if current_header and list_items:
                sorted_lines.extend(sorted(list_items))
                list_items = []
            current_header = header_match.group(1)
            sorted_lines.append(line)
            header_indices.append(i)
        elif current_header and line.startswith("- "):
            list_items.append(line)
        else:
            if list_items and not line.startswith("- "):
                if line.startswith("  "):
                    list_items[-1] += line
                    continue
                else:
                    sorted_lines.extend(sorted(list_items))
                    list_items = []
            sorted_lines.append(line)

    if current_header and list_items:
        sorted_lines.extend(sorted(list_items))

    return sorted_lines, header_indices


# Shared URL normalizer so multiple functions use the same rules for equivalence
def _normalize_url(url: str) -> str:
    """Normalize a URL for comparison:
    - lowercase scheme and netloc
    - remove default ports (:80, :443)
    - strip a single trailing slash from the path
    - preserve query/fragment
    Returns a reconstructed URL string.
    """
    url = str(url)
    try:
        p = urlparse(url)
    except Exception:
        return str(url)

    scheme = p.scheme.lower()
    netloc = p.netloc.lower()
    # remove default ports
    if scheme == "http" and netloc.endswith(":80"):
        netloc = netloc[: -3]
    if scheme == "https" and netloc.endswith(":443"):
        netloc = netloc[: -4]

    # strip trailing slash from path
    path = (p.path or '').rstrip('/')
    # ensure all components are strings
    params = p.params or ''
    query = p.query or ''
    fragment = p.fragment or ''
    new = urlunparse((str(scheme), str(netloc), str(path), str(params), str(query), str(fragment)))
    return str(new)


def remove_duplicate_urls(lines):
    """
    Remove later occurrences of the same normalized URL across the entire document,
    keeping the first occurrence. Only considers the first parenthesized URL on a line
    (typical Markdown link). Returns (filtered_lines, removed_count).
    Non-markdown lines or lines without a parenthesized URL are preserved.
    """
    paren_re = re.compile(r"\(([^)]+)\)")
    seen_urls = set()
    out = []
    removed = 0
    for line in lines:
        m = paren_re.search(line)
        if m:
            norm = _normalize_url(m.group(1))
            if norm in seen_urls:
                removed += 1
                continue
            seen_urls.add(norm)
        out.append(line)
    return out, removed


def remove_exact_duplicate_links(lines):
    """
    Scan adjacent lines and remove the second line when both the [text] and (link)
    are exactly equal. Returns a tuple (filtered_lines, removed_count).

    This only considers the first occurrence and its immediate successor; it
    preserves non-list lines and non-markdown lines unchanged.
    """
    bracket_re = re.compile(r"\[([^]]*?)]")
    paren_re = re.compile(r"\(([^)]+)\)")

    result = []
    i = 0
    removed = 0
    while i < len(lines):
        line = lines[i]
        # By default, keep the current line
        # If the next lines are duplicates (same bracket text and same normalized link),
        # skip all of them so only the first in the run is kept.
        j = i + 1
        m1 = bracket_re.search(line)
        p1 = paren_re.search(line)
        norm_text_1 = None
        norm_url_1 = None
        # If this line has both a [text] and (url), trim trailing spaces inside the []
        # but do NOT normalize case — comparisons should be exact after trimming.
        if m1 and p1:
            text1 = m1.group(1).rstrip()
            # if trimming removed trailing spaces, replace the bracketed portion in the line
            if text1 != m1.group(1):
                line = bracket_re.sub(f"[{text1}]", line, count=1)
            norm_text_1 = text1
            norm_url_1 = _normalize_url(p1.group(1))
            # advance while the next line matches both bracket text and normalized link
            while j < len(lines):
                next_line = lines[j]
                m2 = bracket_re.search(next_line)
                p2 = paren_re.search(next_line)
                if not (m2 and p2):
                    break
                text2 = m2.group(1).rstrip()
                url2 = _normalize_url(p2.group(1))
                # exact match on the trimmed bracket text and normalized URL
                if text2 == norm_text_1 and url2 == norm_url_1:
                    removed += 1
                    j += 1
                    continue
                break
        # append the (possibly trimmed) current line, and continue from j
        result.append(line)
        i = j
    return result, removed


def main():
    # Open with explicit utf-8
    with open("README.md", "r", encoding="utf-8") as file:
        orig_lines = file.readlines()

    # make a small backup so changes are reversible
    try:
        with open("README.md.bak", "w", encoding="utf-8") as bfile:
            bfile.writelines(orig_lines)
    except Exception:
        # non-fatal if backup can't be written
        pass

    # Convert names to title case
    title_case_names = [convert_to_title_case(line) for line in orig_lines]

    # Trim trailing spaces inside any bracketed text (e.g. "[Name ]" -> "[Name]")
    bracket_trailing_space_re = re.compile(r"\[([^]]*?)\s+]")
    # use a single backreference so the captured inner text replaces the group
    trimmed_lines = [bracket_trailing_space_re.sub(r"[\1]", line) for line in title_case_names]

    # Normalize common spelling variants: convert any "Full-Stack" (any case) to "Full Stack"
    # but only inside bracketed descriptions that follow a link, e.g. '](url) [Full-Stack]'
    desc_bracket_re = re.compile(r"(\)\s*\[)([^]]*?)(])")
    # also apply to parenthesized descriptions that follow a link, e.g. '](url) (FullStack)'
    desc_paren_re = re.compile(r"(\)\s*\()([^)]+?)(\))")

    def _norm_desc(m):
        prefix, inside, suffix = m.group(1), m.group(2), m.group(3)
        # replace full-stack variants case-insensitively inside the bracket content
        # match 'full' and 'stack' as whole words allowing optional non-word or underscore separators
        inside2 = re.sub(r"(?i)\bfull(?:[\W_]*?)stack\b", "Full Stack", inside)
        return f"{prefix}{inside2}{suffix}"

    # first normalize bracketed descriptions, then parenthesized descriptions
    normalized_lines = [desc_bracket_re.sub(_norm_desc, line) for line in trimmed_lines]
    normalized_lines = [desc_paren_re.sub(_norm_desc, line) for line in normalized_lines]

    # New: remove duplicate URLs across the document (keep first occurrence)
    url_deduped_lines, url_removed = remove_duplicate_urls(normalized_lines)
    if url_removed:
        print(f"Removed {url_removed} duplicate URL line(s) from README.md (kept first occurrences).")

    # Auto-remove duplicates: ignore trailing whitespace but remain case-sensitive.
    # Keep the first occurrence of each (normalized) line. Pure-empty lines are preserved.
    seen = set()
    deduped_lines = []
    duplicates_removed = 0

    for line in url_deduped_lines:
        if line is None:
            deduped_lines.append(line)
            continue
        if line.strip() == "":
            # preserve empty lines as-is
            deduped_lines.append(line)
            continue

        # Normalize by removing trailing whitespace/newline only (keep case)
        key = line.rstrip()
        if key in seen:
            duplicates_removed += 1
            continue
        seen.add(key)
        deduped_lines.append(line)

    if duplicates_removed:
        print(f"Removed {duplicates_removed} duplicate line(s) from README.md (kept first occurrences).")

    # Sort and write back (using the deduplicated list)
    sorted_lines, header_indices = sort_lists_alphabetically(deduped_lines)

    # New: remove adjacent exact duplicates where both [text] and (link) match
    final_lines, post_removed = remove_exact_duplicate_links(sorted_lines)
    if post_removed:
        print(f"Removed {post_removed} adjacent exact duplicate link(s) after sorting.")

    # Write back using utf-8 as well
    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(final_lines)


if __name__ == "__main__":
    main()

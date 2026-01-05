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


# Define emoji ranges as integer codepoint intervals. We check characters
# against these ranges with ord(), which avoids complex regex issues and is
# portable across Python implementations.
_EMOJI_RANGES = (
    (0x1F300, 0x1F5FF),  # Misc Symbols and Pictographs
    (0x1F600, 0x1F64F),  # Emoticons
    (0x1F680, 0x1F6FF),  # Transport & Map
    (0x1F700, 0x1F77F),  # Alchemical Symbols
    (0x1F780, 0x1F7FF),  # Geometric Shapes Extended
    (0x1F800, 0x1F8FF),  # Supplemental Arrows-C etc.
    (0x1F900, 0x1F9FF),  # Supplemental Symbols and Pictographs
    (0x1FA00, 0x1FA6F),  # Chess Symbols, Symbols and Pictographs
    (0x1FA70, 0x1FAFF),  # Symbols and Pictographs Extended-A
    (0x2600, 0x26FF),    # Misc symbols
    (0x2700, 0x27BF),    # Dingbats
    (0x24C2, 0x1F251),   # Enclosed characters (broad)
)


def _is_emoji_codepoint(cp: int) -> bool:
    for start, end in _EMOJI_RANGES:
        if start <= cp <= end:
            return True
    return False


def has_emoji(text: str) -> bool:
    """Return True if `text` contains any emoji-like character.

    This implementation scans codepoints and returns True if any character
    falls into one of the configured emoji ranges. It's conservative but
    reliable without extra regex dependencies.
    """
    if not text:
        return False
    for ch in text:
        if _is_emoji_codepoint(ord(ch)):
            return True
    return False


def link_text_has_emoji(markdown_line: str) -> bool:
    """Return True if the first Markdown bracketed link text in the line
    contains an emoji.

    Example: "- [Alice 😊](https://example.com)" -> True
    """
    if not markdown_line:
        return False
    m = re.search(r"\[([^]]+)\]", markdown_line)
    if not m:
        return False
    return has_emoji(m.group(1))


def emoji_adjacent_to_link(markdown_line: str) -> bool:
    """Return True if there is an emoji inside a description immediately
    following a link. Matches both bracketed and parenthesized descriptions
    that directly follow a Markdown link, for example:
      - [Foo](https://x) [Desc 😄]
      - [Foo](https://x) (😄)

    Only the description immediately after the first parenthesized URL is
    checked.
    """
    if not markdown_line:
        return False
    # Find a link followed by a bracketed description: '](url) [desc]'
    br_match = re.search(r"\]\s*\([^)]*\)\s*\[([^]]+)\]", markdown_line)
    if br_match and has_emoji(br_match.group(1)):
        return True
    # Find a link followed by a parenthesized description: '](url) (desc)'
    par_match = re.search(r"\]\s*\([^)]*\)\s*\(([^)]+)\)", markdown_line)
    if par_match and has_emoji(par_match.group(1)):
        return True
    return False


# New: functions to remove emoji from link text or adjacent descriptions
def _remove_emoji_chars(s: str) -> (str, int):
    """Return (new_string, removed_count) where emoji-like codepoints are removed from s."""
    if not s:
        return s, 0
    out_chars = []
    removed = 0
    for ch in s:
        if _is_emoji_codepoint(ord(ch)):
            removed += 1
            continue
        out_chars.append(ch)
    # Collapse any remaining runs of whitespace to a single space and strip
    # leading/trailing space so removing an emoji doesn't leave an extra space
    # inside bracketed text or descriptions. Preserve internal single spaces.
    joined = ''.join(out_chars)
    # replace any whitespace (space, NBSP, tabs, newlines) runs with single space
    cleaned = re.sub(r"[\s\u00A0]+", " ", joined).strip()
    return cleaned, removed


def remove_emoji_from_lines(lines):
    """Scan the given list of lines and remove emoji characters from:
    - the bracketed link text (the [text] immediately followed by a parenthesis), and
    - the immediate descriptions that follow a link, either bracketed or parenthesized
      (e.g. '](url) [Desc 😄]' or '](url) (😄)').

    Returns a tuple: (new_lines, removed_count) where removed_count is the total
    number of emoji characters removed.
    """
    new_lines = []
    total_removed = 0

    # regex to find bracketed link text that is followed by '(' (typical Markdown link)
    link_text_re = re.compile(r"\[([^]]+)\](?=\()")
    # regex to find a link followed by either [desc] or (desc)
    adj_desc_re = re.compile(r"\](\s*\([^)]*\)\s*)(?:\[([^]]*)\]|\(([^)]*)\))")

    for line in lines:
        modified_line = line
        removed_this_line = 0

        # 1) remove emoji from the first bracketed link text that precedes a '('
        m = link_text_re.search(modified_line)
        if m:
            inner = m.group(1)
            new_inner, removed = _remove_emoji_chars(inner)
            if removed:
                # replace only the first occurrence
                modified_line = link_text_re.sub(f"[{new_inner}]", modified_line, count=1)
                removed_this_line += removed

        # 2) remove emoji from an adjacent description that immediately follows the first link
        # Use a function to replace the captured description while preserving surrounding text
        def _replace_adj(m):
            nonlocal removed_this_line
            sep = m.group(1)  # the intervening '(url)'-like section plus whitespace
            bracket_desc = m.group(2)
            paren_desc = m.group(3)
            if bracket_desc is not None:
                new_desc, removed = _remove_emoji_chars(bracket_desc)
                removed_this_line += removed
                return f"]{sep}[{new_desc}]"
            if paren_desc is not None:
                new_desc, removed = _remove_emoji_chars(paren_desc)
                removed_this_line += removed
                return f"]{sep}({new_desc})"
            return m.group(0)

        modified_line = adj_desc_re.sub(_replace_adj, modified_line, count=1)

        total_removed += removed_this_line
        new_lines.append(modified_line)

    return new_lines, total_removed


def remove_emoji_from_readme(dry_run=True, backup=True):
    """Scan README.md and remove emojis from link text and adjacent descriptions.

    Arguments:
      dry_run (bool): if True, do not write changes, just return (removed_count, preview_lines)
      backup (bool): if True and not dry_run, write README.md.bak with original content

    Returns:
      (removed_count, original_lines, new_lines) when dry_run True
      (removed_count, None, new_lines) when dry_run False
    """
    path = "README.md"
    with open(path, 'r', encoding='utf-8') as f:
        orig_lines = f.readlines()

    new_lines, removed = remove_emoji_from_lines(orig_lines)

    if removed and not dry_run:
        if backup:
            with open(path + '.bak', 'w', encoding='utf-8') as b:
                b.writelines(orig_lines)
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    if dry_run:
        return removed, orig_lines, new_lines
    return removed, None, new_lines


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

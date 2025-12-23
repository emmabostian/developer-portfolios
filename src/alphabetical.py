import re
from collections import defaultdict


def convert_to_title_case(readme_text):
    # Find all text between square brackets
    # `]` does not need escaping outside a character class; remove redundant escape
    matches = re.findall(r"\[(.*?)]", readme_text)
    for match in matches:
        # Convert to Title Case
        title_case = match.title()
        # Replace the original text with the Title Case version
        readme_text = readme_text.replace(f"[{match}]", f"[{title_case}]")
    return readme_text


def find_duplicate_lines(lines, ignore_case=False, ignore_trailing_whitespace=True):
    """Return a dict mapping a representative original line text -> list of 1-based line
    numbers where duplicates (by normalization) appear.

    By default the normalization ignores trailing whitespace (so "foo\n" and
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
    http_pattern = re.compile(r"(http[s]?://[^\s/]+)/$")
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

    # Auto-remove duplicates: ignore trailing whitespace but remain case-sensitive.
    # Keep the first occurrence of each (normalized) line. Pure-empty lines are preserved.
    seen = set()
    deduped_lines = []
    duplicates_removed = 0

    for line in title_case_names:
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

    # Write back using utf-8 as well
    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(sorted_lines)


if __name__ == "__main__":
    main()

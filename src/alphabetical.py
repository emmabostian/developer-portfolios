import re


def convert_to_title_case(readme_text):
    # Find all text between square brackets
    matches = re.findall(r"\[(.*?)\]", readme_text)
    for match in matches:
        # Convert to Title Case
        title_case = match.title()
        # Replace the original text with the Title Case version
        readme_text = readme_text.replace(f"[{match}]", f"[{title_case}]")
    return readme_text


def sort_lists_alphabetically(lines):
    header_pattern = re.compile(r"^##\s+([A-Z])")
    http_pattern = re.compile(r"(http[s]?://[^\s/]+)/$")
    current_header = None
    list_items = []
    sorted_lines = []
    header_indices = []

    for i, line in enumerate(lines):
        
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
        lines = file.readlines()

    # Convert names to title case
    title_case_names = [convert_to_title_case(line) for line in lines]

    sorted_lines, header_indices = sort_lists_alphabetically(title_case_names)

    # Write back using utf-8 as well
    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(sorted_lines)


if __name__ == "__main__":
    main()

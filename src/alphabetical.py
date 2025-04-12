import re

def sort_lists_alphabetically(lines):
    header_pattern = re.compile(r'^##\s+([A-Z])')
    current_header = None
    list_items = []
    sorted_lines = []
    header_indices = []

    for i, line in enumerate(lines):
        header_match = header_pattern.match(line)
        if header_match:
            if current_header and list_items:
                sorted_lines.extend(sorted(list_items))
                list_items = []
            current_header = header_match.group(1)
            sorted_lines.append(line)
            header_indices.append(i)
        elif current_header and line.startswith('- '):
            list_items.append(line)
        else:
            if list_items and not line.startswith('- '):
                sorted_lines.extend(sorted(list_items))
                list_items = []
            sorted_lines.append(line)

    if current_header and list_items:
        sorted_lines.extend(sorted(list_items))

    return sorted_lines, header_indices

def main():
    with open('README.md', 'r') as file:
        lines = file.readlines()

    sorted_lines, header_indices = sort_lists_alphabetically(lines)

    with open('README.md', 'w') as file:
        file.writelines(sorted_lines)

if __name__ == "__main__":
    main()

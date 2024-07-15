import re

# Load the README file
with open('README.md', 'r') as file:
    readme_contents = file.read()

# Count the list items
list_count = len(re.findall(r'^\s*[-*]\s', readme_contents, re.MULTILINE))

# Define the new banner message
new_banner = f'## Current List Count: {list_count}'

# Replace old banner with new banner in README
new_readme_contents = re.sub(r'## Current List Count: \d+', new_banner, readme_contents)

# Save the changes back to README.md
with open('README.md', 'w') as file:
    file.write(new_readme_contents)

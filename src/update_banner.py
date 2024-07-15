import re
import os

# Set the correct path to the README.md file
script_dir = os.path.dirname(__file__)  # Get the directory where the script is located
root_dir = os.path.join(script_dir, '..')  # Move up to the root directory
readme_path = os.path.join(root_dir, 'README.md')  # Path to the README.md in the root

# Load the README file
with open(readme_path, 'r', encoding='utf-8') as file:
    readme_contents = file.read()

# Count the list items
list_count = len(re.findall(r'^\s*-\s', readme_contents, re.MULTILINE))
print(list_count)

# Define the new banner message
new_banner = f'## Current List Count: {list_count}'
print(new_banner)

# Replace old banner with new banner in README
new_readme_contents = re.sub(r'## Current List Count: \d+', new_banner, readme_contents)
print(new_readme_contents)

# Save the changes back to README.md
with open(readme_path, 'w', encoding='utf-8') as file:
    file.write(new_readme_contents)

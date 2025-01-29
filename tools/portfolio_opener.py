import re
import webbrowser
import argparse
import sys
from pathlib import Path

def open_portfolio_links(file_path):
    """
    Opens all portfolio links found in the given markdown file in new browser tabs.
    
    Args:
        file_path (str): Path to the markdown file containing portfolio links
    """
    try:
        # URL pattern to match the url link in mark down file
        url_pattern = re.compile(r'https?://\S+?(?=\)|\])|https?://\S+')
        
        # Reads the file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            urls = url_pattern.findall(content)
        
        # Open URLs
        for url in urls:
            webbrowser.open_new_tab(url)
        
        print(f"Successfully opened {len(urls)} links in your default browser :`).")
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="Open all portfolio links from the developer-portfolios README in your browser."
    )
    parser.add_argument(
        "-f", "--file",
        default="../README.md",
        help="Path to the markdown file containing portfolio links (default: ../README.md)"
    )
    
    args = parser.parse_args()
    open_portfolio_links(args.file)

if __name__ == "__main__":
    main()
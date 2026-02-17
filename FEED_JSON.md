# Feed JSON Documentation

This project automatically generates a `feed.json` file that contains structured data for all portfolio entries in the README.md file.

## What is feed.json?

The `feed.json` file is a machine-readable JSON file that contains all portfolio entries with the following structure:

```json
[
  {
    "name": "Developer Name",
    "url": "https://portfolio-url.com",
    "tagline": "Optional tagline or expertise"
  },
  {
    "name": "Another Developer",
    "url": "https://another-portfolio.com"
  }
]
```

## Structure

Each portfolio entry is an object with the following fields:

- **name** (string, required): The developer's name
- **url** (string, required): The portfolio website URL
- **tagline** (string, optional): The developer's title, expertise, or description

## How it's Generated

The `feed.json` file is automatically generated when you run:

```bash
python src/alphabetical.py
```

This script:
1. Processes the README.md file
2. Extracts all portfolio entries (lines starting with `- [Name](url)`)
3. Parses optional taglines (text in `[brackets]` after the link)
4. Generates/updates the `feed.json` file

## Standalone Feed Generation

If you only want to update the `feed.json` file without running the full alphabetical sorting, you can use:

```bash
python src/generate_feed.py
```

## Use Cases

The `feed.json` file can be used for:

- Building web applications that display portfolio listings
- Creating search functionality
- Generating statistics about the developer community
- Building portfolio aggregators or discovery tools
- API endpoints for third-party integrations

## Example Usage

### Python
```python
import json

with open('feed.json', 'r') as f:
    portfolios = json.load(f)

# Get all portfolios
for portfolio in portfolios:
    print(f"{portfolio['name']}: {portfolio['url']}")

# Filter portfolios with taglines
portfolios_with_taglines = [p for p in portfolios if 'tagline' in p]
```

### JavaScript
```javascript
const portfolios = require('./feed.json');

// Get all portfolios
portfolios.forEach(portfolio => {
    console.log(`${portfolio.name}: ${portfolio.url}`);
});

// Filter by tagline keyword
const fullStackDevs = portfolios.filter(p => 
    p.tagline && p.tagline.toLowerCase().includes('full stack')
);
```

## Maintenance

The feed.json file is automatically regenerated each time the alphabetical.py script runs. You don't need to manually edit this file.

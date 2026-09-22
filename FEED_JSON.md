# Feed JSON Documentation

This project automatically generates a `feed.json` file that contains structured data for all portfolio entries in the README.md file.

## What is feed.json?

The `feed.json` file is a machine-readable JSON file that contains all portfolio entries with the following structure:

```json
[
  {
    "name": "Developer Name",
    "url": "https://portfolio-url.com",
    "tagline": "Optional tagline or expertise",
    "date_added": "2024-10-15",
    "views": 120,
    "clicks": 8
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
- **date_added** (string, optional): ISO date (`YYYY-MM-DD`) the entry first
  appeared in `README.md`, derived from git history
- **views** (number, optional): How often the portfolio has been viewed
- **clicks** (number, optional): How often the portfolio link has been clicked
- **popularity** (number, optional): Explicit popularity score; overrides the
  default `views + clicks` metric

All fields beyond `name` and `url` are optional, so older consumers keep
working unchanged.

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

The standalone generator preserves metadata (`date_added`, `views`, `clicks`,
`popularity`) that already exists in `feed.json`, so regenerating the feed
never drops it.

### Generating metadata for sorting

`date_added` comes from the git history of `README.md` and is filled in
automatically when running inside a full clone:

```bash
python src/generate_feed.py --with-git-dates
```

Use `--refresh-dates` to recompute dates for every entry, or
`--no-git-dates` to skip git entirely (for example in a shallow clone).

`views` / `clicks` / `popularity` come from an optional
`portfolio_metrics.json` file in the repository root. It can be either a
mapping keyed by URL:

```json
{
  "https://portfolio-url.com": { "views": 120, "clicks": 8 },
  "https://another-portfolio.com": { "views": 40, "clicks": 3, "popularity": 95 }
}
```

or a list:

```json
[
  { "url": "https://portfolio-url.com", "views": 120, "clicks": 8 }
]
```

A missing metrics file is not an error — the view/click sorts simply fall
back to alphabetical order for entries without data. Pass a custom location
with `--metrics path/to/metrics.json`.

## Sorting the list

`feed.json` can be sorted by four options:

| Option    | Label              | Order                                                        |
| --------- | ------------------ | ------------------------------------------------------------ |
| `name`    | Name (A–Z)         | Alphabetical by name (default)                                |
| `newest`  | Newest             | `date_added` descending; entries without a date come last     |
| `popular` | Most Popular       | `popularity` descending (defaults to `views + clicks`)        |
| `views`   | Most Viewed/Clicked| `views` descending, then `clicks` descending                  |

Sorting is stable and deterministic: entries missing a metric are placed
after entries that have one, and alphabetical order breaks ties.

### Python

```python
import json
from src.portfolio_sorting import sort_portfolios

with open("feed.json", encoding="utf-8") as f:
    portfolios = json.load(f)

newest = sort_portfolios(portfolios, "newest")
most_popular = sort_portfolios(portfolios, "popular")
```

### Command line

```bash
# Print the 20 most recently added portfolios as markdown lines
python src/portfolio_sorting.py --by newest --limit 20

# Print the full sorted feed as JSON
python src/portfolio_sorting.py --by views --json
```

Run `python src/portfolio_sorting.py --list-options` to see every option and
alias.

### Web viewer

A small dependency-free viewer with a sorting control lives in `web/`:

```bash
python -m http.server
# then open http://localhost:8000/web/
```

It loads `feed.json`, lets you pick a sort option (Newest, Most Popular, Most
Viewed/Clicked, Name A–Z) and re-renders the list instantly. The selected
option is reflected in the URL (`?sort=newest`) and remembered between
visits.

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

The feed.json file is automatically regenerated each time the alphabetical.py script runs. You don't need to manually edit this file. Metadata fields (`date_added`, `views`, `clicks`, `popularity`) are preserved when it is regenerated; run `python src/generate_feed.py --with-git-dates` to fill in `date_added` for newly added entries.

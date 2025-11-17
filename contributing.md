# Contributing to Developer Portfolios

Thank you for your interest in contributing! This project collects high-quality developer portfolios to inspire and motivate the developer community.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open-source project. In return, they should reciprocate that respect in addressing your issue or assessing patches and features.

---

## 📌 How to Add Your Portfolio

### 1. Open `portfolios.json`

All portfolios are stored in the [`data/portfolios.json`](./data/portfolios.json) file.

### 2. Add a New Entry

Add a new JSON object to the list. You can use the structure from [`data/template.json`](./data/template.json) as a reference.

**Example:**

```json
{
  "name": "Your Full Name",
  "portfolio": "https://your-portfolio-link.com",
  "position": "Optional tag or role"
}
```

**Supported Keys:**

- `name` (required): Your full name.
- `portfolio`: The URL to your portfolio.
- `position`: Your role or a tag (e.g., "Frontend Developer", "Full-Stack", "Designer").

**Important:**

- Make sure your portfolio link starts with `https://`.
- Please add your entry in the correct alphabetical order based on your `name`.

### 🧪 Validate Your Entry

Before creating a pull request, please validate your entry by running the following command in your terminal:

```bash
python3 maker.py > README.md
```

This script will:

- Validate the JSON structure of [`data/portfolios.json`](./data/portfolios.json).
- Regenerate the [`README.md`](./README.md) with the updated list of portfolios.
- Ensure that the file is correctly formatted and sorted.

If the script runs without any errors, your contribution is valid.

### 🔀 Submitting a Pull Request

1.  **Create a new branch:**
    ```bash
    git checkout -b add-your-name
    ```
2.  **Commit your changes:**
    ```bash
    git add data/portfolios.json README.md
    git commit -m "feat: Add <Your Name>'s portfolio"
    ```
3.  **Push the branch:**
    ```bash
    git push origin add-your-name
    ```
4.  **Open a Pull Request:**
    - **Title:** `feat: Add <Your Name>'s Portfolio`
    - **Description:** Briefly describe your addition.

The maintainers will review your pull request as soon as possible.

### 📝 Contribution Rules

- ✔️ Use proper JSON formatting.
- ✔️ Include a valid and active portfolio link.
- ✔️ Provide your full real name.
- ❌ No spam or irrelevant links.

❤️ **Thank You**
Your contribution helps other developers to discover new ideas, get inspiration, and build better portfolios. We appreciate every pull request!

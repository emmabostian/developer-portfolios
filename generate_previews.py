#!/usr/bin/env python3
"""
generate_previews_streaming.py

Parse README.md for portfolio links, take screenshots in parallel,
and as each screenshot finishes, insert its preview into README.md.
"""

import re
import time
from io import BytesIO
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# --- CONFIGURATION ---
README       = Path("README.md")
PREVIEWS_DIR = Path("previews")
VIEWPORT     = (1280, 720)
LOAD_DELAY   = 2
MAX_WORKERS  = 16  # tune this to your machine
# ----------------------

def find_links(text):
    """Return list of (name, url) for all '- [Name](https://...)' lines."""
    pattern = re.compile(r"^\s*-\s*\[([^\]]+)\]\((https?://[^\)]+)\)", re.MULTILINE)
    return pattern.findall(text)

def take_screenshot(url, output_path):
    """Capture top of page via headless Chrome, convert to JPEG."""
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument(f"--window-size={VIEWPORT[0]},{VIEWPORT[1]}")
    driver = webdriver.Chrome(options=opts)
    try:
        driver.get(url)
        time.sleep(LOAD_DELAY)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        png = driver.get_screenshot_as_png()
        img = Image.open(BytesIO(png)).convert("RGB")
        img.save(output_path, format="JPEG", quality=85)
    finally:
        driver.quit()

def insert_preview(name, img_path):
    """
    Read README.md, strip any old preview for this name,
    then insert a new preview markdown line right after its link.
    """
    safe = re.sub(r"[^\w\-]", "_", name).lower()
    preview_pat = re.compile(
        rf"^\s*!\[Preview of {re.escape(name)}\]\(previews/{re.escape(safe)}\.jpg\)$"
    )
    link_pat = re.compile(
        rf"^(\s*-\s*\[{re.escape(name)}\]\([^\)]+\))"
    )

    text = README.read_text(encoding="utf-8")
    lines = text.splitlines()

    # remove old preview line(s)
    lines = [ln for ln in lines if not preview_pat.match(ln)]

    # rebuild with new preview insertion
    out = []
    for ln in lines:
        out.append(ln)
        m = link_pat.match(ln)
        if m:
            indent = m.group(1).split("-")[0] + "  "
            rel = img_path.as_posix()
            out.append(f"{indent}![Preview of {name}]({rel})")

    README.write_text("\n".join(out) + "\n", encoding="utf-8")

def main():
    PREVIEWS_DIR.mkdir(exist_ok=True)
    text = README.read_text(encoding="utf-8")
    links = find_links(text)

    # schedule only missing screenshots
    jobs = []
    for name, url in links:
        safe = re.sub(r"[^\w\-]", "_", name).lower()
        img = PREVIEWS_DIR / f"{safe}.jpg"
        if not img.exists():
            jobs.append((name, url, img))

    if jobs:
        print(f"[+] Capturing {len(jobs)} previews with {MAX_WORKERS} workers…")
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            future_map = {
                pool.submit(take_screenshot, url, img): (name, img)
                for name, url, img in jobs
            }
            for fut in as_completed(future_map):
                name, img = future_map[fut]
                try:
                    fut.result()
                    print(f"    ✔ {name}")
                    insert_preview(name, img)
                    print(f"      → injected into README.md")
                except Exception as e:
                    print(f"    ✖ {name}: {e}")

    else:
        print("✅ All previews already exist; nothing to do.")

if __name__ == "__main__":
    main()

import json
from collections import defaultdict
import string

with open("data/portfolios.json", "r") as f:
    data = json.load(f)

groups = defaultdict(list)
for p in data:
    name = p.get("name", "Unknown")
    c = name[0].upper() if name else "#"
    if c < "A" or c > "Z":
        c = "#"
    groups[c].append(p)

# 🔥 sort full names A→Z inside each group
for c in groups:
    groups[c] = sorted(groups[c], key=lambda x: x.get("name", "").lower())


print("# Developer Portfolios\n")
print("---\n")
print("A list of developer portfolios for your inspiration\n")
print("Have you built a portfolio? Are you proud of it?! Open a [Pr](./CONTRIBUTING.md) to this repo and")
print("let's showcase your work! Refer to the [Contributing](./CONTRIBUTING.md) file for direction.\n")
print("This repo was inspired by [Ali Spittel'S](https://twitter.com/ASpittel) tweet\n")
print("[<Img Width=\"597\" Alt=\"Portfolio\" Src=\"assets/ASpittel_tweet.png\">](https://twitter.com/ASpittel/status/1171604728951779328)\n")
print("Hopefully this repo can serve as a source of inspiration for your portfolio!\n")
print("---\n")
print("## 🎉 Contributor Highlight\n")
print("### **Om Khalane**\n")
print("**Portfolio:** https://omkhalane.is-a.dev\n")
print("**GitHub:** https://github.com/omkhalane\n")
print("**Credits:** Redesigned and modernized this repository\n")
print("---\n")

print("---\n")
print(f"## Current Portfolio Count: {len(data)}\n")

print("**Jump to:** ", end="")
for c in string.ascii_uppercase:
    print(f"[{c}](#{c.lower()}) | ", end="")
print("[Random Portfolio](https://s111ew.github.io/random-button-redirector)\n")

for c in string.ascii_uppercase:
    print(f"## {c}\n")
    for p in groups.get(c, []):
        name = p.get("name", "Unknown")
        url = p.get("url") or p.get("portfolio") or "#"
        tag = p.get("tag") or p.get("position") or ""

        line = f"- [{name}]({url})"
        if tag:
            line += f" [{tag}]"
        print(line)
    print()

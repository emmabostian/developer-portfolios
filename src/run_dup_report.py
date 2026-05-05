#!/usr/bin/env python3
"""Generate a concise duplicate report for README.md using the project's
URL normalization rules (no modifications).

This module is intended to be run as a module: python -m src.run_dup_report
or via the top-level shim `run_dup_report.py`.
"""
import re
import sys
from . import alphabetical


def main():
    path = 'README.md'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('README.md not found', file=sys.stderr)
        return 2

    paren_re = re.compile(r"\(([^)]+)\)")
    seen = {}
    url_duplicates = []
    for i, line in enumerate(lines):
        m = paren_re.search(line)
        if m:
            raw = m.group(1)
            norm = alphabetical._normalize_url(raw)
            if norm in seen:
                url_duplicates.append({'index': i, 'line': line.rstrip(), 'norm': norm, 'first_index': seen[norm]})
            else:
                seen[norm] = i

    bracket_re = re.compile(r"\[([^]]*?)]")
    paren_re = re.compile(r"\(([^)]+)\)")
    adj_duplicates = []
    i = 0
    while i < len(lines):
        line = lines[i]
        j = i + 1
        m1 = bracket_re.search(line)
        p1 = paren_re.search(line)
        if m1 and p1:
            t1 = m1.group(1).rstrip()
            u1 = alphabetical._normalize_url(p1.group(1))
            while j < len(lines):
                nl = lines[j]
                m2 = bracket_re.search(nl)
                p2 = paren_re.search(nl)
                if not (m2 and p2):
                    break
                t2 = m2.group(1).rstrip()
                u2 = alphabetical._normalize_url(p2.group(1))
                if t2 == t1 and u2 == u1:
                    adj_duplicates.append({'index': j, 'line': nl.rstrip(), 'text': t2, 'norm': u2, 'first_index': i})
                    j += 1
                    continue
                break
        i = j

    combined_indices = sorted({d['index'] for d in url_duplicates} | {d['index'] for d in adj_duplicates})

    print('Duplicate detection report for README.md')
    print('Total lines:', len(lines))
    print('URL-based duplicates found (document-wide, keep first occurrence):', len(url_duplicates))
    print('Adjacent exact-link duplicates found (collapsing adjacent runs):', len(adj_duplicates))
    print('Combined unique lines that would be removed:', len(combined_indices))
    print('')

    if url_duplicates:
        print('First 20 URL-based duplicate examples:')
        for d in url_duplicates[:20]:
            print(f"line {d['index']:4d} (keep @ {d['first_index']:4d}): {d['norm']}  -> {d['line']}")
        print('')

    if adj_duplicates:
        print('First 20 adjacent-exact duplicate examples:')
        for d in adj_duplicates[:20]:
            print(f"line {d['index']:4d} (keep @ {d['first_index']:4d}): [{d['text']}] {d['norm']}  -> {d['line']}")
        print('')

    if combined_indices:
        print('First 50 combined line indices:')
        for idx in combined_indices[:50]:
            print(idx)

    return 0


if __name__ == '__main__':
    sys.exit(main())


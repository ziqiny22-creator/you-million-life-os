#!/usr/bin/env python3
"""Heuristic scanner; DOES NOT verify that uploading to GitHub is safe."""
from pathlib import Path
import re, sys
ROOT = Path(__file__).resolve().parents[1]
PATTERNS = {
  'CN_mobile': re.compile(r'(?<!\d)1[3-9]\d{9}(?!\d)'),
  'CN_id_card': re.compile(r'(?<![\da-zA-Z])(?:[1-9]\d{5}(?:18|19|20)\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])\d{3}[0-9Xx])(?![\da-zA-Z])'),
  'email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'),
  'github_token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b'),
  'possible_vehicle_vin': re.compile(r'(?<![A-Z0-9])[A-HJ-NPR-Z0-9]{17}(?![A-Z0-9])'),
}
issues=[]
for path in ROOT.rglob('*'):
    if not path.is_file() or path.suffix.lower() not in {'.md','.json','.jsonl','.txt','.yml','.yaml'}: continue
    content=path.read_text(encoding='utf-8')
    for lineno,line in enumerate(content.splitlines(),1):
        # Deliberately do not echo matching line or secrets to terminal.
        for name,p in PATTERNS.items():
            if p.search(line): issues.append((path.relative_to(ROOT),lineno,name))
if issues:
    print('POTENTIAL SENSITIVE PATTERNS FOUND (no values displayed):')
    for f,lineno,kind in issues: print(f'  {f}:{lineno}: {kind}')
    sys.exit(1)
print('No patterns found in scanned text; manual privacy and third-party review still required.')

#!/usr/bin/env python3
"""Create an editable local markdown entry. Never auto-pushes."""
from pathlib import Path
import sys, datetime, re
ROOT=Path(__file__).resolve().parents[1]
KIND_DIR={'idea':'04_原创思想','decision':'06_生活与决策','project':'05_项目与商业','review':'08_持续更新'}
if len(sys.argv)<3 or sys.argv[1] not in KIND_DIR:
    print('Usage: python scripts/new_entry.py idea|decision|project|review "标题"'); sys.exit(2)
kind,title=sys.argv[1],sys.argv[2].strip()
if not title: raise SystemExit('Empty title')
today=datetime.date.today().strftime('%Y%m%d')
template=(ROOT/'templates'/f'{kind}.md').read_text(encoding='utf-8')
name=re.sub(r'[\\/:*?"<>|\s]+','-',title).strip('-')[:48]
folder=ROOT/KIND_DIR[kind]
for i in range(1,100):
    path=folder/f'{kind.upper()}-{today}-{i:02d}-{name}.md'
    if not path.exists():break
else: raise SystemExit('Too many entries for today')
path.write_text(template.replace('YYYYMMDD',today).replace('灵感标题',title).replace('决策标题',title).replace('项目名称',title).replace('一周/一月复盘',title),encoding='utf-8')
print('Created:',path.relative_to(ROOT))
print('Next: edit contents, update changelog, inspect privacy, commit to PRIVATE repo.')

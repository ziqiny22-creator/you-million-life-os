#!/usr/bin/env python3
"""Rebuild the private single-file context document from topic Markdown files."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ORDER=[
'01_个人画像/个人档案.md','01_个人画像/性格与工作方式.md',
'02_职业与教学/职业成长历程.md','02_职业与教学/教学方法与表达哲学.md','02_职业与教学/组织管理与银川项目.md',
'03_AI发展史/AI使用完整时间线.md','03_AI发展史/工具履历与当前取舍.md','03_AI发展史/AI工作流与项目资产.md',
'04_原创思想/原创观点与灵感原文.md','04_原创思想/人生决策六问与YI-SUN.md',
'05_项目与商业/创业项目总档.md','05_项目与商业/自媒体与个人IP.md','05_项目与商业/电竞模型与股票试错.md',
'06_生活与决策/车辆与停车位决策.md','06_生活与决策/健身与生活目标.md','06_生活与决策/其他重要现实事务.md',
'07_时间线/2026年大事记.md','08_持续更新/未来行动与风险清单.md'
]
other=sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*.md')
             if p.relative_to(ROOT).as_posix() not in ORDER
             and any(v in p.parts for v in ['01_个人画像','02_职业与教学','03_AI发展史','04_原创思想','05_项目与商业','06_生活与决策','07_时间线','08_持续更新']))
header=['# 尤百万个人完整档案 · AI上下文单文件版', '> **私人使用，禁止上传公开仓库。** 本文档由主题文档拼接生成，编辑请回到原文件。', '']
for relative in ORDER+other:
    header += ['\n---\n',f'<!-- 来源：{relative} -->\n', (ROOT/relative).read_text(encoding='utf-8')]
out=ROOT/'个人完整档案_单文件阅读版.md'
out.write_text('\n'.join(header),encoding='utf-8')
print('Rebuilt:',out.relative_to(ROOT),'chars:',len(out.read_text(encoding='utf-8')))

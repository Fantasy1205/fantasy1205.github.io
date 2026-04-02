import re
import os

input_file = "/Users/baiyibo/Projects/Github/fantasy1205.github.io/_posts/zsxq_2024_2026_面试题整理.md"
output_file = "/Users/baiyibo/Projects/Github/fantasy1205.github.io/_posts/zsxq_2024_2026_面试题整理.md"

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

questions = []
ignore_prefixes = [
    "来源用户足迹：",
    "星球 ID：",
    "生成时间：",
    "帖子数量：",
    "主题链接："
]

# We also want to skip markdown comments/metadata if feasible, but since this file is primarily questions,
# we are specifically targeting lines that naturally parse as lists '-' or naturally are questions.
# The user's prompt suggests they want ALL questions across the 2万行.

for line in lines:
    line = line.strip()
    if line.startswith("- "):
        q = line[2:].strip()
        # Skip ignoring patterns
        if any(q.startswith(prefix) for prefix in ignore_prefixes):
            continue
        
        # Strip numbering out like "1. ", "2. ", "123、", etc
        q = re.sub(r'^\d+[\.．、]\s*', '', q)
        
        if q and q not in questions:  # Option to deduplicate, but maybe preserving order is better. Let's not deduplicate immediately unless needed, wait, let's keep all
            questions.append("- " + q)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("---\nlayout: post\ntitle:  \"2024-2026 面试题整理\"\ndate:   2026-04-01 13:57:08 +0800\ncategories: interview\n---\n\n")
    f.write("# 知识星球 2024-2026 面试题纯净版\n\n")
    for q in questions:
        f.write(q + "\n")

print(f"Extracted {len(questions)} questions.")


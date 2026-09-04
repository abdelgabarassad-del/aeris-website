import re

with open('dashboard.css', 'r', encoding='utf-8', errors='ignore') as f:
    css_text = f.read()

keywords = ['.task-form', '.task-card', '.eval-select', '.tracker-table', '.task-modal']
for kw in keywords:
    matches = [m.start() for m in re.finditer(re.escape(kw), css_text)]
    print(f"CSS {kw}: {len(matches)} matches")

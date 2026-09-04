import re

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
    lines = content.splitlines()

print(f"Total lines: {len(lines)}")

print("\n--- HTML Structure Highlights ---")
for i, line in enumerate(lines[:950]):
    if any(k in line.lower() for k in ['<section', 'modal', 'id="view-', 'id="tab-', 'class="modal', 'btn-add-task', 'task-modal']):
        print(f"{i+1}: {line.strip()[:100]}")

print("\n--- Search for Task & Progress Tracker Functions ---")
pattern = re.compile(r'function\s+([a-zA-Z0-9_$]+)\s*\(', re.I)
functions = []
for i, line in enumerate(lines[900:], start=901):
    m = pattern.search(line)
    if m:
        fn_name = m.group(1)
        if any(w in fn_name.lower() for w in ['task', 'kanban', 'progress', 'tracker', 'attendance', 'point', 'warning', 'role', 'user', 'member', 'render', 'modal', 'save', 'submit', 'head', 'ceo']):
            functions.append((i, fn_name))

print(f"Found {len(functions)} relevant functions:")
for l, fn in functions[:40]:
    print(f"  Line {l}: {fn}")
if len(functions) > 40:
    print(f"  ... and {len(functions) - 40} more")

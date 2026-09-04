import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

def print_section(title, start_line, end_line):
    print(f"\n==================== {title} (Lines {start_line}-{end_line}) ====================")
    for idx in range(start_line - 1, min(end_line, len(lines))):
        print(f"{idx+1}: {lines[idx].rstrip()}")

# Let's search where member data / TEAM_MEMBERS / ROLES are defined
for i, l in enumerate(lines):
    if 'TEAM_MEMBERS' in l or 'const ROLES' in l or 'allMembers' in l or 'const DEPARTMENTS' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")

# Let's find where task form / task creation is located in HTML and JS
for i, l in enumerate(lines):
    if 'task-form' in l.lower() or 'add task' in l.lower() or 'createtask' in l.lower() or 'form id=' in l.lower():
        print(f"Form Line {i+1}: {l.strip()[:100]}")


import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()
    lines = text.splitlines()

print("=== Check theme overrides for task form ===")
for i, l in enumerate(lines):
    if any(k in l for k in ['task-form__title', 'taskTitle', 'taskPriority', 'taskDeadline', 'submit-task']):
        print(f"Line {i+1}: {l.strip()[:110]}")

import re

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
    lines = content.splitlines()

# 1. Search for role system & currentUser
print("=== Role & User Logic ===")
for i, line in enumerate(lines):
    if any(k in line for k in ['currentUser', 'userRole', 'userDept', 'ROLES', 'isCEO', 'isHead', 'isViceHead', 'isLeader']):
        print(f"{i+1}: {line.strip()[:100]}")

# 2. Search for Add Task Modal / Form in HTML and JS
print("\n=== Add Task / Create Task Logic ===")
for i, line in enumerate(lines):
    if any(k in line.lower() for k in ['btn-add-task', 'add-task', 'createtask', 'new-task', 'task_type', 'rendertracker', 'renderprogresstracker']):
        print(f"{i+1}: {line.strip()[:100]}")

# 3. Search for Tracker / Attendance / Warnings
print("\n=== Tracker & Warnings & Points Logic ===")
for i, line in enumerate(lines):
    if any(k in line.lower() for k in ['function rendertracker', 'function renderprogresstracker', 'function checkmember', 'attendance', 'missedtask', 'deduct', 'penalty', 'warning']):
        print(f"{i+1}: {line.strip()[:100]}")

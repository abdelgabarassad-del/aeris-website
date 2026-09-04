import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()
    lines = text.splitlines()

print("=== Check all occurrences of task creation and submission ===")
for i, l in enumerate(lines):
    if 'submit-task' in l or 'submitBtn' in l or 'newTask' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")

print("\n=== Check all places evaluating memberProgress ===")
for i, l in enumerate(lines):
    if 'memberProgress' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")

print("\n=== Check all places calculating score in Leaderboard ===")
for i, l in enumerate(lines):
    if 'tierScoreTotal' in l or 'rawScore' in l or 'missedPenalty' in l:
        print(f"Line {i+1}: {l.strip()[:100]}")

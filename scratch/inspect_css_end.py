import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.css', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

print(f"Total lines in dashboard.css: {len(lines)}")
for i in range(max(0, len(lines) - 50), len(lines)):
    print(f"{i+1}: {lines[i].rstrip()}")

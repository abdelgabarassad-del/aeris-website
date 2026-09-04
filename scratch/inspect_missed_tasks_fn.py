import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(1550, 1620):
    print(f"{i+1}: {lines[i].rstrip()}")

import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i in range(3225, 3405):
    print(f"{i+1}: {lines[i].rstrip()}")

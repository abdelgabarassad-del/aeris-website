import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '1. Build table headers' in l:
        print(f"Build table headers at line {i+1}")
        for j in range(i, i + 50):
            print(f"{j+1}: {repr(lines[j])}")
        break

for i, l in enumerate(lines):
    if 'Calculate score based on department configuration' in l:
        print(f"Calculate score at line {i+1}")
        for j in range(i - 20, i + 15):
            print(f"{j+1}: {repr(lines[j])}")
        break

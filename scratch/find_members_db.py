import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

def show(start, end):
    print(f"\n==================== LINES {start} to {end} ====================")
    for i in range(start-1, min(end, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()}")

# Let's search where MEMBERS_DATABASE is declared
for i, l in enumerate(lines):
    if 'MEMBERS_DATABASE' in l and ('=' in l or '{' in l):
        print(f"MEMBERS_DATABASE at line {i+1}: {l.strip()[:100]}")
    if 'const POINT_SYSTEM' in l or 'POINT_RULES' in l or 'pointConfig' in l:
        print(f"Point system at line {i+1}: {l.strip()[:100]}")


import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

def show(start, end):
    print(f"\n==================== LINES {start} to {end} ====================")
    for i in range(start-1, min(end, len(lines))):
        print(f"{i+1}: {lines[i].rstrip()}")

show(1025, 1085)
show(1515, 1630)
show(18400, 18560)

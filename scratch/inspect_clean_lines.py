import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

def print_clean(start, end):
    print(f"\n--- Clean Lines {start}-{end} ---")
    for idx in range(start - 1, min(end, len(lines))):
        print(f"{idx+1}: {lines[idx].rstrip()}")

print_clean(18240, 18360)
print_clean(18460, 18510)
print_clean(18540, 18600)

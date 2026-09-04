import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

def print_range(start, end):
    print(f"\n--- Range {start}-{end} ---")
    for idx in range(start - 1, min(end, len(lines))):
        print(f"{idx+1}: {repr(lines[idx])}")

print_range(18120, 18230)
print_range(18335, 18385)
print_range(18430, 18475)

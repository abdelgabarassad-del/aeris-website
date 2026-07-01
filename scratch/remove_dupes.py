with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
deleted_count = 0

for i, line in enumerate(lines):
    # 0-indexed line number is i, 1-indexed is i+1
    # We only delete duplicate declarations after line 500
    if i + 1 > 500:
        stripped = line.strip()
        if (stripped.startswith('const ') and stripped.endswith(';') and '_REG' in stripped):
            # Check if it matches our target constants
            parts = stripped.split()
            if len(parts) >= 4 and parts[1].endswith('_REG') and parts[2] == '=':
                print(f"Deleting duplicate declaration at line {i+1}: {stripped}")
                deleted_count += 1
                continue # Skip writing this line
    new_lines.append(line)

print(f"Total deleted: {deleted_count}")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

import sys

def main():
    dashboard_path = 'c:/Users/abdel/Desktop/aeris-website-main/dashboard.html'
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fixed_lines = []
    fixed_count = 0
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#') and not stripped.startswith('#!') and not stripped.startswith('#include'):
            # Convert Python comment to JS comment
            indent = line[:line.find('#')]
            fixed_line = indent + '//' + line[line.find('#')+1:]
            fixed_lines.append(fixed_line)
            fixed_count += 1
        else:
            fixed_lines.append(line)

    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)

    print(f"Successfully fixed {fixed_count} Python '#' comments into JS '//' comments in dashboard.html!")

if __name__ == '__main__':
    main()

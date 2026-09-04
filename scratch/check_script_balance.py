import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Extract main script content
m = re.search(r'<script>(.*?)</script>', text, re.DOTALL)
if not m:
    print("❌ Could not find script block")
    sys.exit(1)

script_code = m.group(1)

# Check balanced brackets while ignoring strings/comments
stack = []
bracket_map = {')': '(', '}': '{', ']': '['}
lines = script_code.split('\n')

in_string = None
in_multiline_comment = False
escaped = False

for line_num, line in enumerate(lines, start=1):
    i = 0
    while i < len(line):
        ch = line[i]
        
        if in_multiline_comment:
            if ch == '*' and i + 1 < len(line) and line[i+1] == '/':
                in_multiline_comment = False
                i += 2
                continue
            i += 1
            continue
            
        if in_string:
            if escaped:
                escaped = False
            elif ch == '\\':
                escaped = True
            elif ch == in_string:
                in_string = None
            i += 1
            continue
            
        # Check single line comment
        if ch == '/' and i + 1 < len(line) and line[i+1] == '/':
            break # rest of line is comment
            
        # Check multiline comment start
        if ch == '/' and i + 1 < len(line) and line[i+1] == '*':
            in_multiline_comment = True
            i += 2
            continue
            
        # Check strings (single, double, template)
        if ch in ("'", '"', '`'):
            in_string = ch
            escaped = False
            i += 1
            continue
            
        # Check brackets
        if ch in ('(', '{', '['):
            stack.append((ch, line_num))
        elif ch in (')', '}', ']'):
            expected = bracket_map[ch]
            if not stack:
                print(f"❌ Unmatched closing '{ch}' at script line {line_num}")
                sys.exit(1)
            last_open, open_line = stack.pop()
            if last_open != expected:
                print(f"❌ Mismatched '{ch}' at script line {line_num}, expected closing for '{last_open}' from line {open_line}")
                sys.exit(1)
        i += 1

if stack:
    print(f"❌ Unclosed brackets remaining: {len(stack)}, first unclosed: {stack[-1]}")
    sys.exit(1)
else:
    print("✅ All brackets, braces, and parentheses in dashboard.html script are perfectly balanced!")

import re
import sys

def check_brackets(code):
    brackets = {
        '(': 0, ')': 0,
        '{': 0, '}': 0,
        '[': 0, ']': 0
    }
    
    in_string = False
    string_char = ''
    in_comment = False
    comment_type = '' # 'single' or 'multi'
    
    escaped = False
    
    i = 0
    while i < len(code):
        char = code[i]
        
        # Handle escape characters
        if escaped:
            escaped = False
            i += 1
            continue
            
        if char == '\\' and in_string:
            escaped = True
            i += 1
            continue
            
        # Handle comments
        if not in_string and not in_comment:
            if char == '/' and i + 1 < len(code) and code[i+1] == '/':
                in_comment = True
                comment_type = 'single'
                i += 2
                continue
            elif char == '/' and i + 1 < len(code) and code[i+1] == '*':
                in_comment = True
                comment_type = 'multi'
                i += 2
                continue
        
        if in_comment:
            if comment_type == 'single' and char in ('\r', '\n'):
                in_comment = False
            elif comment_type == 'multi' and char == '*' and i + 1 < len(code) and code[i+1] == '/':
                in_comment = False
                i += 2
                continue
            i += 1
            continue
            
        # Handle strings
        if not in_comment:
            if char in ("'", '"', '`'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif string_char == char:
                    in_string = False
                i += 1
                continue
                
        if in_string:
            i += 1
            continue
            
        # Count brackets
        if char in brackets:
            brackets[char] += 1
            
        i += 1
        
    print("Bracket Counts:")
    for b, count in brackets.items():
        print(f"'{b}': {count}")
        
    if brackets['('] != brackets[')']:
        print("WARNING: Parentheses mismatch!")
    if brackets['{'] != brackets['}']:
        print("WARNING: Braces mismatch!")
    if brackets['['] != brackets[']']:
        print("WARNING: Brackets mismatch!")

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract script content
script_matches = re.findall(r'<script>([\s\S]*?)<\/script>', html)
for idx, script in enumerate(script_matches):
    print(f"--- Script {idx} ---")
    check_brackets(script)

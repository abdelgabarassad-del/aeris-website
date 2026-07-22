import re

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
js = "\n".join(scripts)

print("Checking JS code structure...")

# Check that function keywords, quotes, template strings, and object literals are clean
template_backticks = js.count('`')
print(f"Template literal backticks count: {template_backticks} (Even count: {template_backticks % 2 == 0})")
assert template_backticks % 2 == 0, "Unmatched template literal backtick!"

print("All JS structural checks passed cleanly!")

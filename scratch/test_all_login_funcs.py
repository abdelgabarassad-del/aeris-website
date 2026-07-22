import re, sys

with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract script tags content
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
full_js = "\n".join(scripts)

print(f"Total script length: {len(full_js)} characters.")

# Search for any obvious syntax issues or unmatched brackets / quotes
open_curly = full_js.count('{')
close_curly = full_js.count('}')
open_paren = full_js.count('(')
close_paren = full_js.count(')')
open_bracket = full_js.count('[')
close_bracket = full_js.count(']')

print(f"Curly brackets: {open_curly} open, {close_curly} close (diff: {open_curly - close_curly})")
print(f"Parentheses: {open_paren} open, {close_paren} close (diff: {open_paren - close_paren})")
print(f"Square brackets: {open_bracket} open, {close_bracket} close (diff: {open_bracket - close_bracket})")

# Look at lines in renderDashboardGuide, grantAccess, showGrantedMessage, applySennaTheme, applySonicTheme
print("\nChecking function definitions...")
funcs = ['handleAuth', 'grantAccess', 'showGrantedMessage', 'renderDashboardGuide', 'applySennaTheme', 'applySonicTheme', 'initSennaSparkParticles']
for func in funcs:
    if f"function {func}" in full_js:
        print(f"Found function {func}")
    else:
        print(f"MISSING function {func}!")

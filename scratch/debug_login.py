import sys, re

def check_html():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Check for unclosed template literals, string mismatches, or missing symbols
    print("Checking dashboard.html for potential JS breaks...")

    # Find all function calls in applySennaTheme and applySonicTheme
    senna_idx = html.find('function applySennaTheme()')
    sonic_idx = html.find('function applySonicTheme()')
    guide_idx = html.find('function renderDashboardGuide')

    print("Senna function found at:", senna_idx)
    print("Sonic function found at:", sonic_idx)
    print("Guide function found at:", guide_idx)

if __name__ == '__main__':
    check_html()

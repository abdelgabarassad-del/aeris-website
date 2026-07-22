import sys, os

def main():
    dashboard_path = 'c:/Users/abdel/Desktop/aeris-website-main/dashboard.html'
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update ALL_MEMBERS
    old_all_mem = "const ALL_MEMBERS = new Set([\n      '231000393'"
    new_all_mem = "const ALL_MEMBERS = new Set([\n      '231000662', '231000393'"
    if old_all_mem in html:
        html = html.replace(old_all_mem, new_all_mem, 1)

    # 2. Clean up MEMBERS_DATABASE & add Basmala Omar under Software Division
    # Move line 1003 if present
    errant_line = "      '231000393': { name: 'Ahmed Hany', message: '🏎️ Welcome back, Ahmed Hany! \"If you no longer go for a gap that exists, you are no longer a racing driver.\" 🇧🇷🏁' },\n"
    if errant_line in html:
        html = html.replace(errant_line, "", 1)

    old_sw_db = "// Software Division (Pure SW)\n      '251010424': { name: 'Sara Ahmed', depts: ['software'], role: 'head', email: 'saragaber382007@gmail.com' },"
    new_sw_db = "// Software Division (Pure SW)\n      '251010424': { name: 'Sara Ahmed', depts: ['software'], role: 'head', email: 'saragaber382007@gmail.com' },\n      '231000662': { name: 'Basmala Omar', depts: ['software'], role: 'member', email: 'basmala.omar@aeris-team.org' },"
    if old_sw_db in html:
        html = html.replace(old_sw_db, new_sw_db, 1)

    # 3. Add to PERSONAL_GREETINGS
    old_greetings = "const PERSONAL_GREETINGS = {\n      '231000393':"
    new_greetings = "const PERSONAL_GREETINGS = {\n      '231000662': { name: 'Basmala Omar', message: 'Sba7 el fol, Basmala! Welcome back to the software team dashboard. 💻✨' },\n      '231000393':"
    if old_greetings in html:
        html = html.replace(old_greetings, new_greetings, 1)

    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully added Basmala Omar (231000662) to dashboard.html!")

if __name__ == '__main__':
    main()

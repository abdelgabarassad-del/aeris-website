import sys

def main():
    dashboard_path = 'c:/Users/abdel/Desktop/aeris-website-main/dashboard.html'
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        html = f.read()

    old_entry = "'231000393': { name: 'Ahmed Hany', depts: ['electrical'], role: 'member', email: 'ahmed.hany@aeris-team.org' },"
    new_entry = "'231000393': { name: 'Ahmed Hany', depts: ['electrical'], role: 'member', email: 'ahani2026@gmail.com' },"

    if old_entry in html:
        html = html.replace(old_entry, new_entry, 1)
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print("Updated Ahmed Hany email to ahani2026@gmail.com successfully!")
    else:
        print("Target entry not found!")

if __name__ == '__main__':
    main()

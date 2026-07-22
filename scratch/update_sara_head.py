import sys
import os

def update_dashboard():
    dashboard_path = 'c:/Users/abdel/Desktop/aeris-website-main/dashboard.html'
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add '251010424' to HEADS
    old_heads = "const HEADS = new Set([\n      '251001377'"
    new_heads = "const HEADS = new Set([\n      '251010424', '251001377'"
    if old_heads in html:
        html = html.replace(old_heads, new_heads, 1)

    # 2. Update MEMBERS_DATABASE role for Sara Ahmed
    old_db = "'251010424': { name: 'Sara Ahmed', depts: ['software'], role: 'member', email: 'saragaber382007@gmail.com' },"
    new_db = "'251010424': { name: 'Sara Ahmed', depts: ['software'], role: 'head', email: 'saragaber382007@gmail.com' },"
    if old_db in html:
        html = html.replace(old_db, new_db, 1)

    # 3. Add activeTheme === 'sonic' to Division Head section of renderDashboardGuide
    target_head_guide = "else if (activeTheme === 'stitch') {"
    sonic_head_guide = """else if (activeTheme === 'sonic') {
          title = "🌀 Green Hill Zone Software Command Reference";
          welcome = "🦔 Gotta go fast, Head Sara Ahmed! Command the software division and optimize autonomous flight loops at supersonic speed! 🌀";
          items = [
            "<strong>Software Directives:</strong> Upload and delegate software directives using the <strong>Task Upload Form</strong>.",
            "<strong>Supersonic Matrix:</strong> Toggle the <strong>Progress Tracker (Excel)</strong> to audit software member progress, code commits, and task ratings.",
            "<strong>Loop Transition:</strong> Advance task loop phases (<code>▶ Start</code> / <code>✓ Done</code>) on software cards. Purge obsolete directives with <code>&times;</code>.",
            "<strong>Zone Broadcasts:</strong> Publish official announcements on the News Board for the software team.",
            hasFin ? "<strong>Ring Vault (Finances):</strong> Access complete financial controls (Budget & Funding Trackers) to manage EGP allocations and log payments." : "<strong>Ring Expenses (Finances):</strong> Access the Budget Tracker to monitor team spending logs and spent items. Net budget and total rings are hidden."
          ];
        } """ + target_head_guide

    if target_head_guide in html and "activeTheme === 'sonic'" not in html[html.find("role === 'head'"):html.find("role === 'member'")]:
        html = html.replace(target_head_guide, sonic_head_guide, 1)

    # 4. Update PERSONAL_GREETINGS for 251010424
    old_greeting = "'251010424': { name: 'Sara Ahmed', message: 'el dkah fi el ada2 kolha' },"
    new_greeting = "'251010424': { name: 'Sara Ahmed', message: '🦔 Welcome back, Software Head Sara Ahmed! El dkah fi el ada2 kolha! 🌀⚡' },"
    if old_greeting in html:
        html = html.replace(old_greeting, new_greeting, 1)

    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated dashboard.html successfully for Sara Ahmed!")

def update_about_and_team():
    files_to_check = [
        'c:/Users/abdel/Desktop/aeris-website-main/about.html',
        'c:/Users/abdel/Desktop/aeris-website-main/team.html',
        'c:/Users/abdel/Desktop/aeris-website-main/aeris-website-main/about.html',
        'c:/Users/abdel/Desktop/aeris-website-main/aeris-website-main/team.html'
    ]

    target_tbd = '<span class="board-card__role">Head of Software division</span>\n              <span class="board-card__name">TBD</span>'
    replace_name = '<span class="board-card__role">Head of Software division</span>\n              <span class="board-card__name">Sara Ahmed</span>'

    target_tbd_alt = '<span class="board-card__role">Head of Software division</span>\r\n              <span class="board-card__name">TBD</span>'
    replace_name_alt = '<span class="board-card__role">Head of Software division</span>\r\n              <span class="board-card__name">Sara Ahmed</span>'

    for file_path in files_to_check:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if target_tbd in content:
                content = content.replace(target_tbd, replace_name)
            elif target_tbd_alt in content:
                content = content.replace(target_tbd_alt, replace_name_alt)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file_path} successfully!")

if __name__ == '__main__':
    update_dashboard()
    update_about_and_team()

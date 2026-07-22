with open('dashboard.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert "'231000393': { name: 'Ahmed Hany', depts: ['electrical'], role: 'member', email: 'ahani2026@gmail.com' }" in html, "Email update check failed!"

print("Verification successful! Ahmed Hany's email address is updated to ahani2026@gmail.com.")

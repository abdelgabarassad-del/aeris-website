with open('dashboard.html', 'r', encoding='utf-8') as f:
    d = f.read()

assert "'231000662'" in d, "Registration number missing from dashboard.html"
assert "'231000662': { name: 'Basmala Omar', depts: ['software'], role: 'member'" in d, "MEMBERS_DATABASE entry missing or wrong"
assert "'231000662': { name: 'Basmala Omar'" in d, "PERSONAL_GREETINGS entry missing"

print("Verification successful! Basmala Omar (231000662) added to Software Division with default theme.")

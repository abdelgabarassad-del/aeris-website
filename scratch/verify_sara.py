with open('dashboard.html', 'r', encoding='utf-8') as f:
    d = f.read()
with open('about.html', 'r', encoding='utf-8') as f:
    a = f.read()
with open('team.html', 'r', encoding='utf-8') as f:
    t = f.read()

assert "'251010424': { name: 'Sara Ahmed', depts: ['software'], role: 'head'" in d, "Dashboard DB role check failed"
assert "Sara Ahmed" in a and "Head of Software division" in a, "About page check failed"
assert "Sara Ahmed" in t and "Head of Software division" in t, "Team page check failed"

print("Verification successful! Sara Ahmed is promoted to Software Head across dashboard.html, about.html, and team.html!")

with open('dashboard.html', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Rename jetMuted to mig25Muted
new_code = code.replace('jetMuted', 'mig25Muted')

# 2. Insert vostokMuted and mig29Muted states after let gforce = 1.0;
target_str = 'let gforce = 1.0;'
replacement_str = "let gforce = 1.0;\n      let vostokMuted = false;\n      let mig29Muted = false;"

if target_str in new_code:
    # We only replace the first occurrence (which is inside initSovietWidgets)
    new_code = new_code.replace(target_str, replacement_str, 1)
    print("Inserted vostokMuted and mig29Muted successfully")
else:
    print("Warning: Could not find target_str to insert mutes")

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(new_code)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

assert 'id="competitions"' not in html, "Competitions block still exists!"
assert "images/IMG_7617.png" in html, "Competition image missing!"
assert "background-image: url('images/IMG_7617.png');" in html, "Projects background image was not updated!"

print("Verification successful! Competitions block removed and image moved to Our Projects block on index.html.")

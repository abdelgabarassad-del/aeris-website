import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Possible Brave paths
brave_paths = [
    r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe")
]

brave_path = None
for path in brave_paths:
    if os.path.exists(path):
        brave_path = path
        break

if not brave_path:
    print("Brave browser not found in standard paths!")
    # Let's try default chrome/driver anyway, or print error
    print("Available paths checked:", brave_paths)

options = Options()
if brave_path:
    options.binary_location = brave_path
options.add_argument("--headless")
options.add_argument("--log-level=3")

# Enable logging of console errors
options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

try:
    driver = webdriver.Chrome(options=options)
    
    url = "file:///c:/Users/abdel/Desktop/aeris-website-main/dashboard.html"
    driver.get(url)
    
    print("Page Title:", driver.title)
    
    # Check for logs
    logs = driver.get_log('browser')
    print(f"\n--- Browser Logs ({len(logs)}) ---")
    for entry in logs:
        print(f"[{entry['level']}] {entry['timestamp']} - {entry['message']}")
        
    driver.quit()
except Exception as e:
    print("Error running Selenium:", e)

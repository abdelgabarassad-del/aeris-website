import urllib.request
import urllib.parse
import json

url = "https://script.google.com/macros/s/AKfycbwhJBeQL91cCpvvLTMDkkvyE-SZcNVgWMlta8HEBhZzZB6eTqpTxnVgVWdUi92bcH5F/exec"

data = urllib.parse.urlencode({
    "action": "sendEmail",
    "to": "abdelgabarassad@gmail.com",
    "subject": "Test Warning from Antigravity",
    "body": "This is a test warning email to verify the Google Apps Script integration."
}).encode("utf-8")

req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})

try:
    with urllib.request.urlopen(req) as response:
        content = response.read().decode("utf-8")
        print("HTTP Status:", response.status)
        print("Response Content:", content)
except Exception as e:
    print("Error:", e)

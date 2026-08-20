import urllib.request
import urllib.parse

url = "https://script.google.com/macros/s/AKfycbwhJBeQL91cCpvvLTMDkkvyE-SZcNVgWMlta8HEBhZzZB6eTqpTxnVgVWdUi92bcH5F/exec"

data = urllib.parse.urlencode({
    "fullName": "Test Applicant",
    "email": "abdelgabarassad@gmail.com",
    "phone": "+201000000000",
    "regNumber": "23100999",
    "universityId": "Aerospace Engineering",
    "academicYear": "3rd Year",
    "primaryDept": "Software",
    "secondaryDept": "Electrical",
    "subInterest": "Autonomous Navigation",
    "experience": "Python, C++, ROS2",
    "whyJoin": "Passionate about UAVs",
    "portfolioLink": "https://github.com/test",
    "promoCode": "AERIS2026TEST"
}).encode("utf-8")

req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})

try:
    with urllib.request.urlopen(req) as response:
        content = response.read().decode("utf-8")
        print("Form submission status:", response.status)
        print("Form submission response:", content)
except Exception as e:
    print("Error:", e)

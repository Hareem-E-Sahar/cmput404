import requests
import json
print(requests.__version__)
# 2.24.0

# Ref:https://note.nkmk.me/en/python-package-version/
# Also we could run this command on terminal
# pip show requests

url = "https://www.google.com"
res = requests.get(url).text
print (res)

#Q7
url = "https://raw.githubusercontent.com/Hareem-E-Sahar/cmput404/master/q2.py"
res = requests.get(url)
print (res.text)



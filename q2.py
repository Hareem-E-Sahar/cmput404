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

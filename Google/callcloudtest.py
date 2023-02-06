import json
import requests
url = "https://australia-southeast2-softbank-376302.cloudfunctions.net/hello-world"
param = {"name":"Testing"}

r = requests.post(url, json=param)
print(r.status_code)
print(r.text)

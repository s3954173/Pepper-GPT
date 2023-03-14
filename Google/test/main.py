import subprocess
import requests
import os

# Test values
api_key = os.getenv("OPENAI_API_KEY") 
language = "Chinese"
message = "Hello World"

# Curl Command

headers = {
            'Authorization': 'bearer $(gcloud auth print-identity-token)',
            'Content-Type': 'application/json',
            }
data = {"api_key": api_key, "language": language,"message": message}

response = requests.post('https://callgpt-gemqjtz7eq-ts.a.run.app', headers=headers, json=data)

print(response.text)

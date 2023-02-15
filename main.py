import os
import urllib
import urllib2
import json
api_key = os.getenv("OPENAI_API_KEY")

#TODO Pepper Listening

#TODO Speech to text

#TODO Run gcloud function from propmt

# To delete test variables language and message
language = "Chinese"
message = "Test message"

url = "https://callgpt-gemqjtz7eq-ts.a.run.app"
values = {"api_key": api_key,
        "language": language,
        "message": message}
headers = {"Authorization":"bearer $(gcloud auth print-identity-token)",
        "Content-Type": "application/json"}

data = json.dumps(values, indent=len(values))
req = urllib2.Request(url, data, headers)
url_response = urllib2.urlopen(req)
translated_message = url_response.read()
print(translated_message)
#TODO Return response to Pepper

#TODO Say to user

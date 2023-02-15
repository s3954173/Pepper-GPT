import urllib
import urllib2
import json

url = 'https://hello-world-gemqjtz7eq-km.a.run.app'
values = {"name":"Sasha"}
headers = {"Authorization":"bearer $(gcloud auth print-identity-token)",
        "Content-Type": "application/json"}

json_object = json.dumps(values, indent=len(values))
#data = urllib.urlencode(values)
req = urllib2.Request(url,json_object,headers)
response = urllib2.urlopen(req)
the_page = response.read()
print(the_page)

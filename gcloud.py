import urllib
import urllib2
import json

class GPTfunc:
    # Variables
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"Authorization":"bearer $(gcloud auth print-identity-token)", "Content-Type": "application/json"}

    # Methods

    def callgcloud(url, data, self.headers):
        req = urllib2.Request(url, data, self.headers)
        url_response = urllib2.urlopen(req)


    def translate(self, url, language, message):
        values = {"api_key": self.api_key,
                "language": language,
                "message": message}
        data = json.dumps(values, indent=len(values)) #Convert dictionary to JSON

        callgcloud(url,data,self.headers)
        # Call gcloud function
        #req = urllib2.Request(url, data, self.headers) 
        #url_response = urllib2.urlopen(req)

        # Return translated message
        return url_response.read()

    def callgpt(self, url, prompt):
        values = {"api_key": self.api_key,
                "language": language,
                "prompt": prompt}
        data = json.dumps(values, indent=len(values))

        #Call gcloud function
        #req = urllib2.Request(url, data, self.headers)
        #url_response = urllib2.urlopen(req)

        callgcloud(url,data,self.headers)

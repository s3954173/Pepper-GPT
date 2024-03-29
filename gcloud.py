import urllib
import urllib2
import json

class GPTfunc:
    # Variables
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"Authorization":"bearer $(gcloud auth print-identity-token)", "Content-Type": "application/json"}

    # Methods

    def callgcloud(self, url, data):
        req = urllib2.Request(url, data, self.headers)
        url_response = urllib2.urlopen(req)
        return url_response.read()


    # def translate(self, url, language, message):
    #     values = {"api_key": self.api_key,
    #             "language": language,
    #             "message": message}
    #     data = json.dumps(values, indent=len(values)) #Convert dictionary to JSON

    #     callgcloud(url,data)
    #     # Call gcloud function
    #     #req = urllib2.Request(url, data, self.headers) 
    #     #url_response = urllib2.urlopen(req)

    #     # Return translated message
    #     return url_response.read()

    def callgpt(self, prompt):
        values = {"api_key": self.api_key,
                "prompt": prompt}
        data = json.dumps(values, indent=len(values))
        return data
        


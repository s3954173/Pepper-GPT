import urllib
import urllib2

url = 'https://australia-southeast2-softbank-376302.cloudfunctions.net/hello-world'
values = {"name":"Michael Foord"}

url_values = urllib.urlencode(values)
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#the_page = response.read()

#Get Method
full_url = url + '?' + url_values
data = urllib2.urlopen(full_url)
print(data.read())

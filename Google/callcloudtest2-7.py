import urllib
import urllib2

url = 'https://australia-southeast2-softbank-376302.cloudfunctions.net/hello-world'
values = {"name":"Sasha"}

#Get Method
#url_values = urllib.urlencode(values)
#full_url = url + '?' + url_values
#data = urllib2.urlopen(full_url)
#print(data.read())

#POST METHOD
method = "POST"
handler = urllib2.HTTPHandler()
opener = urllib2.build_opener(handler)

data = urllib.urlencode(values)
request = urllib2.Request(url,data=data)
request.add_header("Content-Type","application/json")
request.get_method = lambda: method

try:
	connection = opener.open(request)
except urllib2.HTTPError,e:
	connection = e

if connection.code == 200:
    data = connection.read()
    print(data)
else:
    print("Error!")
    
#response = urllib2.urlopen(req)
#the_page = response.read()
#print(the_page)

req = Request(url, urlencode(data).encode())
response = urlopen(req).read().decode()
print(response)

from naoqi import ALProxy
import urllib
import urllib2

url = 'https://australia-southeast2-softbank-376302.cloudfunctions.net/hello-world'
values = {"name":"Tao"}

url_values = urllib.urlencode(values)
#Get Method
full_url = url + '?' + url_values
data = urllib2.urlopen(full_url)

phrase = data.read()
tts = ALProxy("ALTextToSpeech", "192.168.60.80", 9559)
tts.say(phrase)

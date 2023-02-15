import os
import naoqi
from naoqi import ALProxy

api_key = os.getenv("OPENAI_API_KEY")
tts = ALProxy("ALTextToSpeech", "192.168.60.80", 9559)
tts = ALProxy("ALSpeechToText", "192.168.60.80", 9559) # might not exist

#TODO Pepper Listening
speech_heard = False
while True:
    tts.say("Hi, my name is Pepper. Can I help you with anything?")
    # listen

    #TODO Speech to text
    if speech_heard == True:
        break
    else:
        # wait XX number of seconds
        x = 1 # filler code

#TODO Run gcloud function from propmt
output_from_GCloud = "Google cloud function complete."

#TODO Return response to Pepper
output = output_from_GCloud

#TODO Say to user
tts.say(output)
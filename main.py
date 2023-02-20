# import os
# import urllib
# import urllib2
# import json
# from naoqi import ALProxy
# import time

# api_key = os.getenv("OPENAI_API_KEY")
# tts = ALProxy("ALTextToSpeech", "192.168.60.80", 9559)
# stt = ALProxy("ALSpeechRecognition", "192.168.60.80", 9559) # might not exist

# stt.setLanguage("English")

# with open(r"C:\Users\Sasha\Documents\Uni\Extension_Programming\Softbank\Pepper-Translator\english3.txt") as f:
#     words = f.read().splitlines()

# stt.setVocabulary(words)





# ############################################################################################################################

# #TODO Pepper Listening
# start_time = time.time
# while True:
#     tts.say("Hi, my name is Pepper. Can I help you with anything?")
#     stt.subscribe("Test_STT")
#     while stt.SpeechDetected == True:
#         # listen
#         if stt.SpeechDetected == False:
#             stop_time = time.time

#     # when the user stops talking, the program waits for one second and if no more speech is heard, proceed to activating the google cloud function with whatever was heard


#     if (time.time - start_time)%10 == 0 and stt.SpeechDetected == True:
#         stt.unsubscribe("Test_STT")
#         break
#         # in a later update, the google cloud function may need to be called here
#     elif (time.time - start_time)%10==0:
#         continue

#     #TODO Speech to text
#     if speech_heard == True:
#         break
#     else:
#         # wait XX number of seconds
#         x = 1 # filler code

# ############################################################################################################################





# #TODO Run gcloud function from propmt
# # To delete test variables language and message
# language = "Chinese"
# message = "Test message"

# url = "https://callgpt-gemqjtz7eq-ts.a.run.app"
# values = {"api_key": api_key,
#         "language": language,
#         "message": message}
# headers = {"Authorization":"bearer $(gcloud auth print-identity-token)",
#         "Content-Type": "application/json"}

# data = json.dumps(values, indent=len(values))
# req = urllib2.Request(url, data, headers)
# url_response = urllib2.urlopen(req)
# translated_message = url_response.read()
# print(translated_message)

# #TODO Say to user
# tts.say(message + " translated into " + language + " is " + translated_message)







############################################################################

import os
import requests
import json
from naoqi import ALProxy
import speech_recognition as sr
import gcloud as gc

# Variables
api_key = os.getenv("OPENAI_API_KEY")
urls = {"gpt-translate": "https://callgpt-gemqjtz7eq-ts.a.run.app"}
callgpt = gc.GPTfunc(api_key)

tts = ALProxy("ALTextToSpeech", "192.168.60.80", 9559)

def speech_recognition(message):
    tts.say(message)
    # Initialize recognizer
    r = sr.Recognizer()

    # mic_name = 'Microphone (Arctis 5 Chat)' # for sasha PC system

    # Start listening
    try:
        with sr.Microphone(device_index=None) as source: # device_index=sr.Microphone.list_microphone_names().index(mic_name)
            # print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
    except:
        sr.WaitTimeoutError

    # print("Processing...")

    try:
        text = r.recognize_google(audio)
        # print("You said: ", text)
        return text
    except sr.UnknownValueError:
        # print("Could not understand audio")
        return None
    except sr.RequestError as e:
        # print("Could not request results; {0}".format(e))
        return None

# TODO Pepper Listening
functionality = speech_recognition("Hi, I'm Pepper. What can I do for you today?")
for word in functionality.split():
    if word.lower() == "translate":
        # Translate functionality
        message = speech_recognition("What message would you like me to translate?")
        language = speech_recognition("What language would you like your message translated into?")

        # Run gcloud function from propmt 
        translated_message = callgpt.translate(urls["gpt-translate"], language, message)

        # Output to user
        tts.say(message + " translated into " + language + " is " + translated_message) # has issues encoding chinese translations

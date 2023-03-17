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

tts = ALProxy("ALTextToSpeech", "192.168.152.13", 9559)

def speech_recognition(message):
    tts.say(message)

    r = sr.Recognizer()

    # Start listening
    try:
        with sr.Microphone(device_index=None) as source:
            r.pause_threshold = 1
            audio = r.listen(source)
    except:
        sr.WaitTimeoutError

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
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
        string_output = str(message) + " translated into " + str(language) + " is " + str(translated_message.strip("\n"))
        tts.say(string_output) # has issues encoding chinese translations

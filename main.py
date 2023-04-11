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
        string_output = str(message) + " translated into " + str(language) + " is " + str(translated_message.strip("\n"))
        tts.say(string_output) # has issues encoding chinese translations
    elif word.lower() == "story":
        # Story functionality
        topic = speech_recognition("What would you like the story to be about?")

        story = callgpt.story()
    elif word.lower() == "explain":
        # Explain functionality
        topic = speech_recognition("What would you like me to explain?")

        story = callgpt.explain()
    elif word.lower() == "who":
        # Who is functionality
        
        story = callgpt.who()

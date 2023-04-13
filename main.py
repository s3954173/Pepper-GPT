import os
import requests
import json
from naoqi import ALProxy
import speech_recognition as sr
import gcloud as gc

# Variables
api_key = os.getenv("OPENAI_API_KEY")
url = "https://callgpt-gemqjtz7eq-ts.a.run.app"
callgpt = gc.GPTfunc(api_key)

# tts = ALProxy("ALTextToSpeech", "192.168.152.13", 9559)

def speech_recognition(message):
    # tts.say(message)
    # Initialize recognizer
    r = sr.Recognizer()

    # mic_name = 'Microphone (Arctis 5 Chat)' # for sasha PC system
    # mic_name = 'Headset Microphone (Realtek High Definition Audio(SST))'

    # Start listening
    try:
        with sr.Microphone(device_index=None) as source: # device_index=sr.Microphone.list_microphone_names().index(mic_name)
            r.adjust_for_ambient_noise(source)
            print("Listening....")
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

# Send prompt to callgpt gcloud function and pepper outputs message
def OutputMessage(callgpt,prompt):
    data = callgpt.callgpt(prompt)
    message = callgpt.callgcloud(url,data)
    return message

# TODO Pepper Listening
functionality = speech_recognition("Hi, I'm Pepper. What can I do for you today?")
words = functionality.split()
for index, word in enumerate(words):
    if word.lower() == "translate":
        # Translate functionality
        message = speech_recognition("What message would you like me to translate?")
        language = speech_recognition("What language would you like your message translated into?")

        prompt = "Translate {message} into {language}."

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print("{message} translated into {language} is {output}.")

    elif word.lower() == "story":
        # Story functionality
        topic = speech_recognition("What would you like the story to be about?")

        prompt = "Tell me a story about {topic}."

        print("telling a story")

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print(output)

    elif word.lower() == "explain":
        # Explain functionality
        for value in words[index:]:
            if value == "something":
                topic = speech_recognition("What would you like me to explain?")
                prompt = "Explain {topic} in simple terms."
            else:
                prompt = ' '.join(words[index:])

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print(output)

    elif word.lower() == "who":
        # Who is functionality
        for value in words[index:]:
            if value == "someone":
                topic = speech_recognition("Who would you like me to tell you about?")
                prompt = "Who is {topic}?"
            else:
                prompt = ' '.join(words[index:])

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print(output)

    elif word.lower() == "what":
        # What is functionality
        for value in words[index:]:
            if value == "something":
                topic = speech_recognition("What would you like me to explain?")
                prompt = "What is {topic}?"
            else:
                prompt = ' '.join(words[index:])

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print(output)

    elif word.lower() == "where":
        # # Where is functionality
        for value in words[index:]:
            if value == "something":
                topic = speech_recognition("Where would you like me to tell you about?")
                prompt = "Where is {topic}?"
            else:
                prompt = ' '.join(words[index:])

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print(output)

    elif word.lower() == "when":
        # When is functionality
        for value in words[index:]:
            if value == "something":
                topic = speech_recognition("When would you like me to know about?")
                prompt = "When is {topic}?"
            else:
                prompt = ' '.join(words[index:])

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print(output)

    elif word.lower() == "why":
        # Why is functionality
        prompt = ' '.join(words[index:])

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print(output)
        






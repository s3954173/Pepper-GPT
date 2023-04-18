import os
import requests
import json
from naoqi import ALProxy
import speech_recognition as sr
import gcloud as gc
import time
import sys

# Variables
api_key = os.getenv("OPENAI_API_KEY")
url = "https://callgpt-gemqjtz7eq-ts.a.run.app"
callgpt = gc.GPTfunc(api_key)

tts = ALProxy("ALTextToSpeech", "192.168.111.80", 9559)

def speech_recognition(message):
    print(message)
    tts.say(message)
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

# TTS output message
def OutputTTS(callgpt, prompt):
    output = OutputMessage(callgpt,prompt)
    print(output)
    tts.say(str(output))


# Pepper functions/variables
functionlist = ["translate", "story", "explain", "who", "what", "where", "when", "why"]

def translate(callgpt,words):
    # Translate functionality
        message = speech_recognition("What message would you like me to translate?")
        language = speech_recognition("What language would you like your message translated into?")

        prompt = "Translate {} into {}.".format(message, language)

        # Calls output function
        output = OutputMessage(callgpt,prompt)
        print("{} translated into {} is {}.".format(message, language, output))
        tts.say(str("{} translated into {} is {}.".format(message, language, output)))


def story(callgpt, words):
     # Story functionality
    prompt_set = False
    word_list = words[index:]
    for idx, value in enumerate(word_list):
        if value == "about":
            word_list2 = words[idx:]
            something = False
            for thing in word_list2:
                if thing == "something":
                    something = True
                    break
            if something == False:
                info = []
                for first_token in words[:index]:
                    info.append(first_token)
                info.append("short")
                for second_token in words[index:]:
                    info.append(second_token)
                    prompt = ' '.join(info)
                    print(prompt)
                prompt_set = True
            else:
                break
    if prompt_set == False:
        topic = speech_recognition("What would you like the story to be about?")
        prompt = "Tell me a short story about {}.".format(topic)
    tts.say("Ok, let me think for a moment.")

    # Calls output function
    OutputTTS(callgpt,prompt)



def explain(callgpt, words):
    # Explain functionality
    prompt_set = False
    for value in words[index:]:
        if value == "something":
            topic = speech_recognition("What would you like me to explain?")
            prompt = "Explain {} in simple terms.".format(topic)
            prompt_set = True
            break
    if prompt_set == False:
        prompt = ' '.join(words[index:])

    # Calls output function
    output = OutputMessage(callgpt,prompt)
    print(output)
    tts.say(str(output))


def who(callgpt, words):
    # Who is functionality
    prompt_set = False
    for value in words[index:]:
        if value == "someone":
            topic = speech_recognition("Who would you like me to tell you about?")
            prompt = "Who is {}?".format(topic)
            prompt_set = True
            break
    if prompt_set == False:
        prompt = ' '.join(words[index:])

    # Calls output function
    OutputTTS(callgpt,prompt)


def what(callgpt, words):
    # What is functionality
    prompt_set = False
    for value in words[index:]:
        if value == "something":
            topic = speech_recognition("What would you like me to explain?")
            prompt = "What is {}?".format(topic)
            prompt_set = True
            break
    if prompt_set == False:
        prompt = ' '.join(words[index:])

     # Calls output function
    OutputTTS(callgpt,prompt)


def where(callgpt, words):
    # # Where is functionality
    prompt_set = False
    for value in words[index:]:
        if value == "something":
            topic = speech_recognition("Where would you like me to tell you about?")
            prompt = "Where is {}?".format(topic)
            prompt_set = True
            break
    if prompt_set == False:
        prompt = ' '.join(words[index:])

    # Calls output function
    OutputTTS(callgpt,prompt)


def when(callgpt, words):
    # When is functionality
    prompt_set = False
    for value in words[index:]:
        if value == "something":
            topic = speech_recognition("When would you like to know about?")
            prompt = "When is {}?".format(topic)
            prompt_set = True
            break
    if prompt_set == False:
        prompt = ' '.join(words[index:])

    # Calls output function
    OutputTTS(callgpt,prompt)


def why(callgpt, words):
    # Why is functionality
    prompt_set = False
    for value in words[index:]:
        if value == "something":
            topic = speech_recognition("What would you like to know about?")
            prompt = "Why is {}?".format(topic)
            prompt_set = True
            break
    if prompt_set == False:
        prompt = ' '.join(words[index:])
    prompt = ' '.join(words[index:])

    # Calls output function
    OutputTTS(callgpt,prompt)





# TODO Pepper Listening
listening = True
while listening:
    time.sleep(5)
    try:
        functionality = speech_recognition("Hi, I'm Pepper. What can I do for you today?")
        words = functionality.split()
        for index, word in enumerate(words):
            if word.lower() in functionlist:
                pepper_function = word.lower() + "(callgpt,words)"
                pepper_function = eval(pepper_function)


            # if word.lower() == "translate":
            #     translate(callgpt)

            # elif word.lower() == "story":
            #     story(callgpt,words)
              

            # elif word.lower() == "explain":
            #     explain(callgpt,words)

            # elif word.lower() == "who":
            #     who(callgpt,words)

            # elif word.lower() == "what":
            #     what(callgpt,words)

            # elif word.lower() == "where":
            #     where(callgpt,words)

            # elif word.lower() == "when":
            #     when(callgpt,words)

            # elif word.lower() == "why":
            #     why(callgpt,words)
      
    except:
        time.sleep(5)
    
        






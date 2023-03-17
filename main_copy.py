import os
import requests
import json
from naoqi import ALProxy
import speech_recognition as sr
import gcloud as gc
import time

# variables
api_key = os.getenv("OPENAI_API_KEY")
urls = {"gpt-translate": "https://callgpt-gemqjtz7eq-ts.a.run.app"}
callgpt = gc.GPTfunc(api_key)

robot_IP = "169.254.237.146"

tts = ALProxy("ALTextToSpeech", robot_IP, 9559)

# general vocab
all_word_asr = ALProxy("ALSpeechRecognition", robot_IP, 9559)
all_word_asr.setLanguage("English")
vocabulary = []  
with open('english3.txt', 'r') as file:
    for line in file:
        word = line.strip() 
        vocabulary.append(word) 
all_word_asr.setVocabulary(vocabulary, True)

# functions
# function_word_asr = ALProxy("ALSpeechRecognition", robot_IP, 9559)
# function_word_asr.setLanguage("English")
# functions = ["tell", "story", "explain", "translate"]  
# all_word_asr.setVocabulary(vocabulary, True)

# def function_recog():
#     function_word_asr.subscribe("Test_ASR")
#     print('Speech recognition engine started')
#     time.sleep(10)
#     function_word_asr.unsubscribe("Test_ASR")

#     return function_word_asr.WordRecognized

def all_recog():
    all_word_asr.subscribe("Test_ASR")
    print('Speech recognition engine started')
    time.sleep(10)
    all_word_asr.unsubscribe("Test_ASR")

    print(all_word_asr.WordRecognized)

    return all_word_asr.WordRecognized

# TODO Pepper Listening
# functionality = speech_recognition("Hi, I'm Pepper. What can I do for you today?")
# for word in functionality.split():
#     if word.lower() == "translate":
#         # Translate functionality
#         message = speech_recognition("What message would you like me to translate?")
#         language = speech_recognition("What language would you like your message translated into?")

#         # Run gcloud function from propmt 
#         translated_message = callgpt.translate(urls["gpt-translate"], language, message)

#         # Output to user
#         string_output = str(message) + " translated into " + str(language) + " is " + str(translated_message.strip("\n"))
#         tts.say(string_output) # has issues encoding chinese translations

while True:
    tts.say("I'm listening.")
    all_recog()
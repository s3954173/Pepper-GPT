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
prompt = "Tell me a story about Jack and Jill"

def OutputMessage(callgpt,prompt):
    data = callgpt.callgpt(prompt)
    message = callgpt.callgcloud(url,data)
    print(message)

OutputMessage(callgpt,prompt)


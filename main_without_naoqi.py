import os
import requests
import json
import speech_recognition as sr

def speech_recognition(message):
    print(message)
    # Initialize recognizer
    r = sr.Recognizer()

    # mic_name = 'Microphone (Arctis 5 Chat)' # for sasha PC system

    # Start listening
    try:
        with sr.Microphone(device_index=None) as source:
            print("Listening....")
            r.pause_threshold = 1
            audio = r.listen(source)
    except:
        sr.WaitTimeoutError

    print("Processing...")

    # try:
    #     with sr.Microphone(device_index=sr.Microphone.list_microphone_names().index(mic_name)) as source:
    #         print("Listening....")
    #         r.pause_threshold = 1
    #         audio = r.listen(source)
    # except:
    #     sr.WaitTimeoutError

    # print("Processing...")

    try:
        text = r.recognize_google(audio)
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

# TODO Pepper Listening
functionality = speech_recognition("Hi, I'm Pepper. What can I do for you today?")
for word in functionality.split():
    if word.lower() == "translate":
        # Translate functionality
        message = speech_recognition("What message would you like me to translate?")
        language = speech_recognition("What language would you like your message translated into?")

        # Run gcloud function from propmt 
        api_key = os.getenv("OPENAI_API_KEY")
        url = "https://callgpt-gemqjtz7eq-ts.a.run.app"
        values = {"api_key": api_key,
                "language": language,
                "message": message}
        headers = {"Authorization":"bearer $(gcloud auth print-identity-token)",
                "Content-Type": "application/json"}

        response = requests.post(url, headers=headers, json=values)
        translated_message = response.text

        # Output to user
        print(message + " translated into " + language + " is " + translated_message) # has issues encoding chinese translations

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def sentenceCheck(inputSentence):
    aiSentenceCheck = generate_response("Is " + splitResponse[0] + " a sentence?")
    charList = list(aiSentenceCheck)
    if (charList[0]+charList[1]).lower() == "no":
        isSentence = False
    elif (charList[0]+charList[1]+charList[2]).lower() == "yes":
        isSentence = True
    return isSentence

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = generate_response(user_input)
    



    splitResponse = response.split("\n", maxsplit=1)
    if len(splitResponse) == 1:
        print(1)

        print("Chatbot:", response)
    elif len(splitResponse) == 2:
        print(2)

        isSentence = sentenceCheck(splitResponse[0])
        if isSentence == True:
            print("isSentence=True")

            print("Chatbot:", response)
        elif isSentence == False:
            print("isSentence=False")

            print("[ " + splitResponse[0] + " ]")
            print("[ " + splitResponse[1] + " ]")
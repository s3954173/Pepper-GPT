import os

api_key = os.getenv("OPENAI_API_KEY")

# Speech to text function to get user input.
# For now:
while True:
    user_input = input("Speech input: ")
    if user_input.lower() == "exit":
        break

    #####

    # takes the place of calling from google cloud in this script
    absPath = os.getcwd()
    relPath = "\Python_Scripts"
    fullPath = absPath+relPath
    os.chdir(fullPath)
    os.system("python GPT_GC.py " + user_input)

    #####
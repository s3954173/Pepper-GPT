import functions_framework
import openai
import os

@functions_framework.http
def callgpt(request):
    """HTTP Cloud Function.
   Args:
       request (flask.Request): The request object.
       <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
   Returns:
       The response text, or any set of values that can be turned into a
       Response object using `make_response`
       <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
   """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'message' in request_json:
       openai_key = request_json['key']
       message = request_json['message']
    elif request_args and 'message' in request_args:
       openai_key = request_args['key']
       message = request_args['message']
    else:
       message = "I'm sorry could you repeat that again?"
       openai_key = request_args['key']
       
    # GPT Translate
    openai.api_key = openai_key
    language = "japanese"		
    model_engine = "text-davinci-003"
    prompt = f"Translate {message} into {language}."

    completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            )

    translated_message = completions.choices[0].text
    return translated_message

"""def translate(phrase, language, openai_key):
    
    model_engine = "test-davinci-003"
    prompt = (f"Translate {phrase} into {language}")

    completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            )

    message = completions.choices[0].text
    return message.strip() """

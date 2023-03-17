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

    if request_json and 'prompt' in request_json:
       openai_key = request_json['api_key']
       prompt = request_json['prompt']
    elif request_args and 'prompt' in request_args:
       openai_key = request_args['api_key']
       prompt = request_args['prompt']
    else:
       return "I'm sorry could you repeat that again?"
       
    # GPT Translate
    openai.api_key = openai_key		
    model_engine = "text-davinci-003"

    completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            )

    response = completions.choices[0].text
    return response

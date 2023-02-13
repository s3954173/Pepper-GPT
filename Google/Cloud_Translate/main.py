import functions_framework
import six
from google.cloud import translate_v2 as translate

@functions_framework.http
def cloud_translate(request):
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
   

   if request_json and 'phrase' in request_json:
       phrase = request_json['phrase']
     #key = request_json['key']
   elif request_args and 'phrase' in request_args:
       phrase = request_args['phrase']
       #key = request_json['key']
   else:
       phrase = "I'm sorry, could you repeat that?"

   translate_client = translate.Client()

   if isinstance(phrase, six.binary_type):
        phrase = text.decode("utf-8")
   result = translate_client.translate(phrase, target_language='zh')

   translated_phrase = result["translatedText"]
   return translated_phrase

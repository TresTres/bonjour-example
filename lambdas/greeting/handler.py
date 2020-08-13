import json

from translate import Translator


def hello(event, context):
    
    
    body = {
        "message": toIndonesian(event['message']),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def toIndonesian(msg):
    translator = Translator(to_lang="Indonesian")
    translation = translator.translate(msg)
    return translation
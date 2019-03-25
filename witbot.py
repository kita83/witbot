import os
import sys
import json

from wit import Wit
from mongo_client import MongoDB

WIT_APIKEY = os.getenv('WIT_API_TOKEN')


def get_response(message):
    wit_client = Wit(access_token=WIT_APIKEY)
    resp = wit_client.message(message)
    if 'entities' not in resp:
        return ''

    response = ''
    for key, values in resp['entities'].items():
        for value in values:
            score = round(value['confidence'], 2) * 100
            response += '{} ({}:{}%)\n'.format(value['value'], key, str(score))
            if key == 'intent':
                intent = value['value']
                if 'metadata' in value:
                    metadata = value['metadata']
            else:
                if key not in entities:
                    entities[key] = []
                entities[key].append(value['value'])

    if metadata and (metadata in key_list):
        entities_ = list(entities[metadata])

    mongo_client = MongoDB()
    mongo_resp = mongo_client.aggregate(intent, key_list)
    if mongo_resp:
        response += '------------------------------------------------------\n'
        response += '{}のガイドを始めます。\n'.format(mongo_resp[0]['name'])
        response += mongo_resp[0]['description']
    else:
        response += '何だそれ😇'
    return response


if __name__ == '__main__':
    message = sys.argv[1]
    resp = main(message)
    print(resp)


import os
import sys
import json

from wit import Wit
from mongo_client import MongoDB

WIT_APIKEY = os.getenv('WIT_API_TOKEN')


def get_response(message):
    wit_client = Wit(access_token=WIT_APIKEY)
    resp = wit_client.message(message)
    intent = {}
    metadata = ''
    response = ''
    entities = {}
    # entities = resp['entities']
    # if 'intent' in entities:
    #     intent = entities.pop('intent')
    print(resp)
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

    mongo_client = MongoDB()
    entities_ = []
    if metadata and (metadata in entities):
        entities_ = list(entities[metadata])
        print(entities_)
    mongo_resp = mongo_client.aggregate(intent, entities_)
    if mongo_resp:
        response += '{}のガイドを始めます。\n'.format(mongo_resp[0]['name'])
        response += mongo_resp[0]['description']
    else:
        response += 'レスポンスデータ該当なし'
    return response


if __name__ == '__main__':
    message = sys.argv[1]
    resp = main(message)
    print(resp)


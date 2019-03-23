import os
import sys
import json

from wit import Wit
from pymongo import MongoClient

WIT_APIKEY = os.environ['WIT_API_TOKEN']
mogno_client = MongoClient('localhost', 27017)


def get_response(message):
    wit_client = Wit(access_token=WIT_APIKEY)
    resp = wit_client.message(message)
    intent = ''
    metadata = ''
    response = ''
    entities = {}
    print(resp['entities'])
    for key, values in resp['entities'].items():
        for value in values:
            score = round(value['confidence'], 2) * 100
            response += '{} [{}] ({}%)\n'.format(value['value'], key, str(score))
            if key == 'intent':
                intent = value['value']
                if 'metadata' in value:
                    metadata = value['metadata']
            else:
                if key in entities:
                    entities[key].append(value['value'])
                else:
                    entities[key] = value['value']

    db = mogno_client['witbot']
    collection = db['guide']
    entities_ = []
    if metadata and (metadata in entities):
        entities_ = list(entities[metadata])
    result = list(collection.aggregate([
        {'$match':
            {'$and': [
                {'entities': {'$in': entities_}},
                {'intent': intent}
                ]
            }
        }
    ]))
    if result:
        response += '{}のガイドを初めます。\n'.format('test')
        response += result[0]['talk']

    return response


if __name__ == '__main__':
    message = sys.argv[1]
    resp = main(message)
    print(resp)


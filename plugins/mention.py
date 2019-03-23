import json

from pymongo import MongoClient
from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

from wit_ai import main


client = MongoClient('localhost', 27017)

@respond_to('')
def mention_func(message):
    resp = main(message.body['text'])
    resp_entities = resp['entities']
    response = ''
    intent = ''
    entities = {}
    for key, values in resp_entities.items():
        for value in values:
            score = round(value['confidence'], 2) * 100
            response += '{} [{}]({}%)\n'.format(value['value'], key, str(score))
            if key == 'intent':
                intent = value['value']
            else:
                if key in entities:
                    entities[key].append(value['value'])
                else:
                    entities[key] = value['value']

    db = client['witbot']
    collection = db['guide']
    result = collection.find_one({'intent': intent})
    response += '{}のガイドを初めます。\n'.format(entities.join(', '))
    response += result['talk']

    message.reply(response)


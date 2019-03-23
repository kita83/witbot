import json

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

from wit_ai import main


@respond_to('')
def mention_func(message):
    resp = main(message.body['text'])
    resp_entities = resp['entities']
    print(resp_entities)
    response = ''
    intent = ''
    entities = {}
    for key, values in resp_entities.items():
        for value in values:
            score = round(value['confidence'], 2) * 100
            response += '[{}] {}({}%)\n'.format(key, value['value'], str(score))
            if key == 'intent':
                intent = value['value']
            else:
                if key in entities:
                    entities[key].append(value['value'])
                else:
                    entities[key] = value['value']

    if (intent == 'guide_hotel') and ('hotel' in entities):
        print(entities)
        if 'はつしろ旅館' in entities['hotel']:
            response += 'はつしろ旅館のガイドを初めます。\n'
            response += 'はつしろ旅館とは...\n'

    message.reply(response)


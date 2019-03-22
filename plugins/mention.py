import json

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

from wit_ai import main


@respond_to('')
def mention_func(message):
    resp = main(message.body['text'])
    resp_entities = resp['entities']
    response = ''
    intent = ''
    entities = {}
    for key, value in resp_entities.items():
        score = round(value[0]['confidence'], 2) * 100
        response += '[{}] {}({}%)\n'.format(key, value[0]['value'], str(score))
        if key == 'intent':
            intent = value[0]['value']['value']
        else:
            entities['key'] = value[0]['value']

    if (intent == 'guide_hotel') and ('hotel' in entities):
        if entities['hotel'][0]['value']['value'] == '積善館':
            response += '積善館のガイドを初めます。\n'
            response += '積善館とは...\n'

    message.reply(response)


import json

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import listen_to      # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

from wit_ai import main


@respond_to('')
def mention_func(message):
    resp = main(message.body['text'])
    entities = resp['entities']
    response = ''
    for key, value in entities.items():
        score = round(value[0]['confidence'], 2) * 100
        response += '[{}] {}({}%)\n'.format(key, value[0]['value'], str(score))

    message.reply(response)


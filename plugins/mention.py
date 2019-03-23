import json

from slackbot.bot import respond_to
from witbot import get_response


@respond_to('')
def mention_func(message):
    resp = get_response(message.body['text'])
    response = resp if resp else 'それって何だっけ...'
    message.reply(response)

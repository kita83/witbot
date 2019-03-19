import os
import sys
import json
import configparser

from wit import Wit


conf = configparser.ConfigParser()
conf.read(os.path.join(os.path.dirname(__file__), './bot.conf'))
WIT_APIKEY = conf.get('WIT', 'APIKEY')

def main(message):
    client = Wit(access_token=WIT_APIKEY)
    resp = client.message(message)
    return resp


if __name__ == '__main__':
    message = sys.argv[1]
    resp = main(message)
    print(resp)


import os
import sys
import json

from wit import Wit


WIT_APIKEY = os.environ["WIT_API_TOKEN"]

def main(message):
    client = Wit(access_token=WIT_APIKEY)
    resp = client.message(message)
    return resp


if __name__ == '__main__':
    message = sys.argv[1]
    resp = main(message)
    print(resp)


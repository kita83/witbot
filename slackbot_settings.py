import os
import configparser

conf = configparser.ConfigParser()
conf.read(os.path.join(os.path.dirname(__file__), './bot.conf'))
API_TOKEN = conf.get('SLACK', 'APIKEY')

# どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "よかよか"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']


import os


API_TOKEN = os.getenv('SLACK_API_TOKEN')

# どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "よかよか"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']

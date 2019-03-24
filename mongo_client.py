import os

from pymongo import MongoClient


MONGO_URI = os.getenv('MONGODB_URI')
USER = os.getenv('MONGODB_USER')
PWD = os.getenv('MONGODB_PWD')

class MongoDB:
    MongoClient = None

    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.client['witbot'].authenticate(USER, PWD)
        db = self.client['witbot']
        self.collection = db['guide']

    def __exit__(self):
        self.client.close()

    def aggregate(self, intent:str, entities:list):
        result = list(self.collection.aggregate([
            {'$match':
                {'$and': [
                    {'name': {'$in': entities}},
                    {'intent': intent}
                    ]
                }
            }
        ]))
        return result

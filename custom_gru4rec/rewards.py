import random
import pymongo
import json
from bson import json_util


MONGODB_USER = 'utopr'
MONGODB_PASSWORD = 'capstone15'
MONGODB_URI = 'mongodb://%s:%s@13.209.65.64:27017' % (MONGODB_USER, MONGODB_PASSWORD)
MONGODB_DATABASE = 'utopr'
client = pymongo.MongoClient(MONGODB_URI)
db = client[MONGODB_DATABASE]
col = db['products']


def reward_to_mongo(pick_items_id):

    for i in range(len(pick_items_id)):
        item=list(col.find({'product_id':pick_items_id[i]}))
        
        reward=item[0]['product_reward']

        item_id=item[0]['product_id']
        
        update_reward = reward+1

        col.update_many(
                {
                "product_id":item_id,
                },
                {
                '$set':{
                'product_reward': update_reward
                }
            }
        )


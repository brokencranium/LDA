from pymongo import MongoClient
from Settings import Settings
import json

tips_file = Settings.TIPS_FILE
tips_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.TIPS_COLLECTION]
business_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.BUSINESS_COLLECTION]

with open(tips_file) as tips:
    next(tips)
    for tip in tips:
        try:
            data = json.loads(tip)
            if data["type"] == "tip" and \
                    business_collection.find({"business_id": data["business_id"]}).limit(1).count():
                tips_collection.insert({
                    "user_id": data["user_id"],
                    "business_id": data["business_id"],
                    "date":data["date"],
                    "text": data["text"]
                })
        except ValueError:
            print('Unable to parse' + tip)

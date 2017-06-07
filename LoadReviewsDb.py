from pymongo import MongoClient
from Settings import Settings
import json

reviews_file = Settings.REVIEWS_FILE
reviews_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.REVIEWS_COLLECTION]
business_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.BUSINESS_COLLECTION]

with open(reviews_file) as reviews:
    next(reviews)
    for review in reviews:
        try:
            data = json.loads(review)
            if data["type"] == "review" and \
                    business_collection.find({"business_id": data["business_id"]}).limit(1).count():
                reviews_collection.insert({
                    "review_id": data["review_id"],
                    "business_id": data["business_id"],
                    "text": data["text"]
                })
        except ValueError:
            print('Unable to parse' + review)

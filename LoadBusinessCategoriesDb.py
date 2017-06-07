from genericpath import exists

from pymongo import MongoClient
from Settings import Settings
import json

buss_file = Settings.BUSINESS_FILE
buss_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.BUSINESS_COLLECTION]


def load_categories():
    cats = set()
    with open('Categories.txt', 'rU') as f:
        for line in f:
            cats.add(line.strip())
    return cats


categories = load_categories()
# print(categories)
with open(buss_file) as buss:
    next(buss)
    for bus in buss:
        try:
            data = json.loads(bus)
            if data["categories"] is not None:
                if [cat for cat in categories if cat in data["categories"]]:
                    buss_collection.insert({
                        "_id": data["business_id"],
                        "categories": data["categories"]
                    })
        except ValueError:
            print('Unable to parse' + buss)

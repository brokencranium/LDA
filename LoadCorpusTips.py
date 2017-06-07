from pymongo import MongoClient
from Settings import Settings
from nltk.stem.wordnet import WordNetLemmatizer

tags_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.TAGS_TIPS_COLLECTION]
corpus_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.CORPUS_TIPS_COLLECTION]

tags_cursor = tags_collection.find()
tags_count = tags_cursor.count()
tags_cursor.batch_size(5000)

lemmas = WordNetLemmatizer()

for tag in tags_cursor:
    nouns = []
    words = [word for word in tag["words"] if word["pos"] in ["NN", "NNS"]]

    for word in words:
        nouns.append(lemmas.lemmatize(word["word"]))

    corpus_collection.insert({
        "user_id": tag["user_id"],
        "business_id": tag["business_id"],
        "text": tag["text"],
        "words": nouns
    })



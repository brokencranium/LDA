from pymongo import MongoClient
from Settings import Settings
from nltk.stem.wordnet import WordNetLemmatizer

tags_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.TAGS_REVIEWS_COLLECTION]
corpus_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
    Settings.CORPUS_REVIEWS_COLLECTION]

reviews_cursor = tags_collection.find()
reviews_count = reviews_cursor.count()
reviews_cursor.batch_size(5000)

lemmas = WordNetLemmatizer()

for review in reviews_cursor:
    nouns = []
    words = [word for word in review["words"] if word["pos"] in ["NN", "NNS"]]

    for word in words:
        nouns.append(lemmas.lemmatize(word["word"]))

    corpus_collection.insert({
        "review_id": review["review_id"],
        "business_id": review["business_id"],
        "text": review["text"],
        "words": nouns
    })



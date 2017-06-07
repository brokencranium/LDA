import string
from math import floor

from pymongo import MongoClient
from Settings import Settings
import nltk
import multiprocessing


def load_tags(size, start):
    tips_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
        Settings.TIPS_COLLECTION]    
    tags_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
        Settings.TAGS_TIPS_COLLECTION]

    stopwords = nltk.corpus.stopwords.words('english')
    puncs = set(string.punctuation)
    batch_size = 1000
    
    for batch in range(0, size, batch_size):
        tips_cursor = tips_collection.find().skip(start + batch).limit(batch_size)
        for tip in tips_cursor:
            words = []
            sentences = nltk.sent_tokenize(tip["text"].lower())

            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence)
                content = [token for token in tokens if token not in stopwords and token not in puncs]
                tags = nltk.pos_tag(content)

                for word, tag in tags:
                    words.append({"word": word, "pos": tag})
    
            tags_collection.insert({
                "user_id": tip["user_id"],
                "business_id": tip["business_id"],
                "text": tip["text"],
                "words": words
            })


def main():
    tips_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
        Settings.TIPS_COLLECTION]
    tips_cursor = tips_collection.find()
    count = tips_cursor.count()
    workers = 3
    batch = floor(count / workers)
    left = count % workers

    jobs = []
    for i in range(workers):
        size = floor(count / workers)
        if i == (workers - 1):
            size += left
        p = multiprocessing.Process(target=load_tags, args=(size, i * batch))
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()
        print('%s.exitcode = %s' % (j.name, j.exitcode))


if __name__ == '__main__':
    main()


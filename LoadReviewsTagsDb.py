import string
from math import floor

from pymongo import MongoClient
from Settings import Settings
import nltk
import multiprocessing


def load_tags(size, start):
    reviews_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
        Settings.REVIEWS_COLLECTION]
    tags_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
        Settings.TAGS_REVIEWS_COLLECTION]

    stopwords = nltk.corpus.stopwords.words('english')
    puncs = set(string.punctuation)

    batch_size = 1000
    for batch in range(0, size, batch_size):
        reviews_cursor = reviews_collection.find().skip(start + batch).limit(batch_size)
        for review in reviews_cursor:
            words = []
            sentences = nltk.sent_tokenize(review["text"].lower())

            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence)
                content = [token for token in tokens if token not in stopwords and token not in puncs]
                tags = nltk.pos_tag(content)

                for word, tag in tags:
                    words.append({"word": word, "pos": tag})

            tags_collection.insert({
                "review_id": review["review_id"],
                "business_id": review["business_id"],
                "text": review["text"],
                "words": words
            })


def main():
    reviews_collection = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.BUSINESS_DATABASE][
        Settings.REVIEWS_COLLECTION]
    reviews_cursor = reviews_collection.find()
    count = reviews_cursor.count()
    print("Count " + str(count))
    workers = 5
    batch = floor(count / workers)
    left = count % workers

    jobs = []
    for i in range(workers):
        size = floor(count / workers)
        print("Size " + str(size))
        if i == (workers - 1):
            size += left
        print("Count " + str(i) + " " + str(size) + " " + str(i*batch))
        p = multiprocessing.Process(target=load_tags, args=(size, i * batch))
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()
        print('%s.exitcode = %s' % (j.name, j.exitcode))


if __name__ == '__main__':
    main()

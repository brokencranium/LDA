class Settings:
    def __init__(self):
        pass

    TIPS_FILE = "/home/vicky/Documents/it/notes/AI/UW/Project/data/yelp_academic_dataset_tip.json"
    REVIEWS_FILE = "/home/vicky/Documents/it/notes/AI/UW/Project/data/yelp_academic_dataset_review.json"
    BUSINESS_FILE = "/home/vicky/Documents/it/notes/AI/UW/Project/data/yelp_academic_dataset_business.json"
    # TIPS_FILE = '/Users/vvennava/temp/yelp/tips.json'
    # REVIEWS_FILE = '/Users/vvennava/temp/yelp/reviews.json'
    # BUSINESS_FILE= "/Users/vvennava/temp/yelp/business.json"

    MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
    BUSINESS_DATABASE = "Business"

    TIPS_COLLECTION = "Tips"
    TAGS_TIPS_COLLECTION = "Tags_Tips"
    REVIEWS_COLLECTION = "Reviews"
    TAGS_REVIEWS_COLLECTION = "Tags_Reviews"
    CORPUS_REVIEWS_COLLECTION = "Corpus_Reviews"
    CORPUS_TIPS_COLLECTION = "Corpus_Tips"
    BUSINESS_COLLECTION = "Business_Cats"

    # DICTIONARY_TIPS_PATH = '/Users/vvennava/Documents/personal/it/python/LDA/model_tips/dictionary.dict'
    # DICTIONARY_REVIEWS_PATH = '/Users/vvennava/Documents/personal/it/python/LDA/model_reviews/dictionary.dict'
    DICTIONARY_TIPS_PATH = '/home/vicky/Code/LDA/model_tips/dictionary.dict'
    DICTIONARY_REVIEWS_PATH = '/home/vicky/Code/LDA/model_reviews/dictionary.dict'

    # CORPUS_TIPS_PATH = "/Users/vvennava/Documents/personal/it/python/LDA/model_tips/corpus.lda-c"
    # CORPUS_REVIEWS_PATH = "/Users/vvennava/Documents/personal/it/python/LDA/model_reviews/corpus.lda-c"
    CORPUS_TIPS_PATH = "/home/vicky/Code/LDA/model_tips/corpus.lda-c"
    CORPUS_REVIEWS_PATH = "/home/vicky/Code/LDA/model_reviews/corpus.lda-c"

    # MODEL_TIPS_PATH = "/Users/vvennava/Documents/personal/it/python/LDA/model_tips/lda_model_50_topics.lda"
    # MODEL_REVIEWS_PATH = "/Users/vvennava/Documents/personal/it/python/LDA/model_reviews/lda_model_50_topics.lda"
    MODEL_TIPS_PATH = "/home/vicky/Code/LDA/model_tips/lda_model_50_topics.lda"
    MODEL_REVIEWS_PATH = "/home/vicky/Code/LDA/model_reviews/lda_model_50_topics.lda"

    LDA_NUM_TOPICS = 50

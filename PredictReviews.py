from gensim.models import LdaModel
from gensim import corpora
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from Settings import Settings

new_review = "It's like eating with a big Italian family. " \
             "Great, authentic Italian food, good advice when asked, and terrific service. " \
             "With a party of 9, last minute on a Saturday night, we were sat within 15 minutes. " \
             "The owner chatted with our kids, and made us feel at home. " \
             "They have meat-filled raviolis, which I can never find. " \
             "The Fettuccine Alfredo was delicious. We had just about every dessert on the menu. " \
             "The tiramisu had only a hint of coffee, the cannoli was not overly sweet, " \
             "and they had this custard with wine that was so strangely good. " \
             "It was an overall great experience!"

dictionary_path = Settings.DICTIONARY_REVIEWS_PATH
lda_model_path = Settings.MODEL_REVIEWS_PATH
dictionary = corpora.Dictionary.load(dictionary_path)
lda = LdaModel.load(lda_model_path)
stopwords = nltk.corpus.stopwords.words('english')
words = []
nouns = []

sentences = nltk.sent_tokenize(new_review.lower())
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    text = [word for word in tokens if word not in stopwords]
    tagged_text = nltk.pos_tag(text)

    for word, tag in tagged_text:
        words.append({"word": word, "pos": tag})

lem = WordNetLemmatizer()

for word in words:
    if word["pos"] in ["NN", "NNS"]:
        nouns.append(lem.lemmatize(word["word"]))

new_review_bow = dictionary.doc2bow(nouns)
new_review_lda = lda[new_review_bow]
print(new_review_lda)
output = list(sorted(new_review_lda, key=lambda x: x[1]))
print(output[0])
print(output[-1])
print(lda.print_topic(output[0][0]))
print(lda.print_topic(output[-1][0]))
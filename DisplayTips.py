import logging
import matplotlib.pyplot as plt

from gensim.models import LdaModel
from gensim import corpora

from Settings import Settings
from wordcloud import WordCloud
from RandomColors import generate_new_colors


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary_path = Settings.DICTIONARY_TIPS_PATH
corpus_path = Settings.CORPUS_TIPS_PATH
lda_model_path = Settings.MODEL_TIPS_PATH
lda_num_topics = Settings.LDA_NUM_TOPICS

colors = generate_new_colors(pastel_factor=0.5, count=50)
color_count = 50

dictionary = corpora.Dictionary.load(dictionary_path)
corpus = corpora.BleiCorpus(corpus_path)
lda = LdaModel.load(lda_model_path)

i = 0
word_count = {}
topic_word = {}

def topic_color_func(word, font_size, position, orientation, random_state=None,
                     **kwargs):
    color_hsl = colors.__getitem__(topic_word.get(word))
    return "hsl(%d, %d%%, %d%%)" % (color_hsl[0] * 360, color_hsl[1] * 100, color_hsl[2] * 100)


for seq, topic in lda.show_topics(num_topics=lda_num_topics):
    topic = topic.replace('"', '')
    print('#' + str(seq) + ': ' + str(topic))
    sentences = (topic.split(sep='+'))
    i += 1
    for sentence in sentences:
        words = sentence.split(sep='*')
        freq = float(words[0]) * 1000
        word_count.update({words[1]: freq})
        topic_word.update({words[1]: seq})

# for (key, val) in word_count.items():
#     print(key, val)

word_cloud = WordCloud(relative_scaling=1.0).generate_from_frequencies(frequencies=word_count)
# plt.imshow(word_cloud)
plt.imshow(word_cloud.recolor(color_func=topic_color_func, random_state=3),
           interpolation="bilinear")
plt.axis("off")
plt.show()

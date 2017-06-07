import string

import nltk

from replacers import RegexpReplacer
from replacers import RepeatReplacer
from replacers import AntonymReplacer
from replacers import SpellingReplacer

# from pickle import dump
#
# output = open('t2.pkl', 'wb')
# dump(t2, output, -1)
# output.close()

test = "DO NOT GO THERE !!!\n\n1. I knew it was questionbale when i brought in oil i purchased for them to change out. He said they don't do this, because they like to purchase it. In other words, he needed to mark up the price for the same oil.\n\n2. He told me that our Shocks were blown out and said that we can't drive too far. Normally, when your shocks are blown out, your ride will be like a bouncing ball. I closely monitored my drive and i did not have a bumpy ride that indicated blown out shocks. I took it to two separate mechanics and they tested the car and said if the shocks were bad, the car would bounce up and down. \n\nBasically, the owner lied about the shocks to get me to pay to fix them. \n\n3. One of my light bulbs is going out. I looked up the model # to replace them and i went to autozone to purchase the ones for my car. The owner said that these are the wrong headlights and I needed a more expensive set. Now, mind you- the model's I had were based on Lexus' recommendation. \n\nHe then said that it would cost over $300 dollars to change out the bulbs. The bulbs he recommend was about $80 bucks, which means over 200 of labor. \n\nHe will over exaggerate everything to get you to pay more. \n\n\nBtw, I sent my wife in to see if he would try to run up maintenance. \n\nI would not recommend this place at all. He is not goood."
test = test.lower()

regex_replacer = RegexpReplacer()
repeat_replacer = RepeatReplacer()
spell_replacer = SpellingReplacer()
antonym_replacer = AntonymReplacer()

test = regex_replacer.replace(test)

# test = repeat_replacer.replace(test)
# tokens = antonym_replacer.replace_negations(sentence)
# tokens = repeat_replacer.replace(word)



# print(test)

sentences = nltk.sent_tokenize(test)
# # print(sentences)
stopwords = nltk.corpus.stopwords.words('english')
puncs = set(string.punctuation)
pattern = r'''(?x)          # set flag to allow verbose regexps
            (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
          | \w+(?:-\w+)*        # words with optional internal hyphens
          | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
          | \.\.\.              # ellipsis
          | [][.,;"'?():_`-]    # these are separate tokens; includes ], [
        '''
#
# tokens = nltk.regexp_tokenize(sentence, pattern)
words = []
for sentence in sentences:
    tokens = nltk.word_tokenize(sentence)
    content = [token for token in tokens if token not in stopwords and token not in puncs]
    tags = nltk.pos_tag(content)

    for word, tag in tags:
        words.append({"word": word, "pos": tag})

print(words)

import os
import re
import spacy
from headers import *

# Loading the POS tagger.
nlp = spacy.load('en_core_web_sm')

# engdata will store the corpus.
# engtags will store the POS tags for all the words in a sentence for all the senteces in the corpus.
# engtags = [{"word_tags": {"word": token, "POS_TAG": token.pos_}}] is the structure of engtags.
engdata = []
engtags = []

# Loading the corpus
f = open("../eng_conditional_sentences.txt", 'r')
for sentences in f:
    sentences = sentences.rstrip()
    engdata.append(sentences)

# Finding the POS tags of all the the words in a sentence for all sentences in the corpus.
for sentence in engdata:
    engdoc = nlp(sentence)
    bigtemp = {}
    tokens = []
    for token in engdoc:
        temp = {}
        temp["word"] = token
        temp["POS_TAG"] = token.pos_
        tokens.append(temp)
    bigtemp["word_tags"] = tokens
    engtags.append(bigtemp)

# Printing the sentences along with the POS tags.
g = open('data/eng_pos_tags.txt', 'w')
print_func(engtags, engdata, g)

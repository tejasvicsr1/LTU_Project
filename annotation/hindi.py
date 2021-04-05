import os
import re
import spacy
from headers import *
from helper_hindi import *

# hindata will store the corpus.
# hintags will store the POS tags for all the words in a sentence for all the senteces in the corpus.
# hintags = [{"word_tags": {"word": token, "POS_TAG": token.pos_}}] is the structure of engtags.
hindata = []
hintags = []

# Loading the corpus
f = open("../hin_conditional_sentences.txt", 'r')
for sentences in f:
    sentences = sentences.rstrip()
    hindata.append(sentences)

# Finding the POS tags of all the the words in a sentence for all sentences in the corpus.
for sentence in hindata:
    sentence = nlp_hi(sentence)
    tagged_sentence = get_pos_tags(sentence, 1)
    dep_sentence = get_dependencies(sentence, 1)
    sentence_len = len(tagged_sentence[0])
    bigtemp = {}
    tokens = []
    for i in range(sentence_len):
        temp = {}
        temp["word"] = dep_sentence[0][i][1]
        temp["POS_TAG"] = tagged_sentence[0][i]
        tokens.append(temp)
    bigtemp["word_tags"] = tokens
    hintags.append(bigtemp)

# Printing the sentences along with the POS tags.
g = open("data/hin_pos_tags.txt", 'w')
print_func(hintags, hindata, g)
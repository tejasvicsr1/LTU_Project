import os
import re
import spacy
import stanza

# stanza.download("te")
nlp_te = stanza.Pipeline('te')


def get_dependencies(doc, n):
    def getdeps(i):
        deps = []
        for head, rel, dep in doc.sentences[i].dependencies:
            deps.append((rel, dep.text))
        return deps

    return [getdeps(i) for i in range(n)]


def get_pos_tags(doc, n):
    def getpos(i):
        tokens = []
        for token in doc.sentences[i].words:
            tokens.append(token.upos)
        return tokens

    return [getpos(i) for i in range(n)]



teldata = []
teltags = []
def print_func(teltags, teldata, g):
    g.write("telugu sentences and their POS tags.\n\n\n")
    for i in range(len(teltags)):
        if i != 500:
            g.write(str(i + 1) + ". " + str(teldata[i]) + "\n\n")
        g.write("TAGS:\n\n")
        for j in range(len(teltags[i]["word_tags"])):
            g.write("\t" + str(j + 1) + ". " + str(teltags[i]["word_tags"][j]["word"]) + " -\t" + str(teltags[i]["word_tags"][j]["POS_TAG"]) + '\n')
            if j == len(teltags[i]["word_tags"]) - 1:
                g.write('\n')

# Loading the corpus
f = open("../conditional_sentences_telugu.txt", 'r')
# f = open("/content/drive/My Drive/conditional_sentences_telugu.txt", 'r')
for sentences in f:
    sentences = sentences.rstrip()
    teldata.append(sentences)

# Finding the POS tags of all the the words in a sentence for all sentences in the corpus.
for sentence in teldata:
    sentence = nlp_te(sentence)
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
    teltags.append(bigtemp)

# Printing the sentences along with the POS tags.
g = open("data/tel_pos_tags.txt", 'w')
# g = open("/content/drive/My Drive/tel_pos_tags.txt", 'w')
print_func(teltags, teldata, g)
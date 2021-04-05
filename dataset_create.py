import os
from nltk.corpus import gutenberg

'''
Uncomment the lines from 8 to 20 if you want to see the files again
'''

# texts = gutenberg.fileids()
# for text in texts:
#     f = open('data/' + text, 'w')
#     sentences = gutenberg.sents(text)
#     num_sentences = len(sentences)
#     for i in range(num_sentences):
#         temp = ""
#         for j in range(len(sentences[i])):
#             if j != len(sentences[i]) - 1:
#                 temp += sentences[i][j] + ' '
#             else:
#                 temp += sentences[i][j]
#         f.write(temp + '\n')

directory = 'data'
texts = os.listdir(directory)

final_data = []

for text in texts:
    f = open('data/' + text, 'r')
    sentences = f.readlines()
    sentences = [sentence.rstrip() for sentence in sentences]
    for tsentence in sentences:
        sentence = list(tsentence.split(" "))
        if sentence[0] == "If":
            final_data.append(tsentence)

f = open('conditional_sentences.txt', 'w')
for sentence in final_data:
    f.write(sentence + '\n')


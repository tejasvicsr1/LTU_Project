from google_trans_new import google_translator
translator = google_translator()

f = open("eng_conditional_sentences.txt", 'r')
sentences = f.readlines()
sentences = [sentence.rstrip() for sentence in sentences]

g = open("final_hindi_sens.txt", 'w')

for sentence in sentences:
    g.write(translator.translate(sentence, lang_src='en', lang_tgt='hi') + '\n')


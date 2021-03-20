# import nltk

# extract epub to text:
# https://github.com/kevinxiong/epub2txt

#
# text = "Bed and chair are types of furniture"
#
# print(text)
# #
# # DT is the determinant
# #
# # VBP is the verb
# #
# # JJ is the adjective
# #
# # IN is the preposition
# #
# # NN is the noun
#
# sentence = [("a", "DT"),("clever","JJ"),("fox","NN"),("was","VBP"),
#    ("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]
#
# grammar = "NP:{<DT>?<JJ>*<NN>}"
#
# parser_chunking = nltk.RegexpParser(grammar)
#
# parser_chunking.parse(sentence)
#
# output = parser_chunking.parse(sentence)
#
# output.draw()


import spacy
import ebooklib
from ebooklib import epub
# Spicy version, python version, en_core_web_sm version
# # Load English tokenizer, tagger, parser and NER
from MachineBookExtract.venv.epub2txt import main_method

nlp = spacy.load("en_core_web_sm")
print("Test1")
# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")
doc = nlp(text)

# Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
#
# # Find named entities, phrases and concepts
# for entity in doc.ents:
#     print(entity.text, entity.label_)

#book = epub.read_epub(r'C:\Users\pa-wo\Desktop\Studia\Magisterka\MachineBookExtract\MobyDick.epub')
# str = []

#main_method(r'C:\Users\pa-wo\Desktop\Studia\Magisterka\MachineBookExtract\MobyDick.epub')

str = open('test111.txt', 'r').read()

#print(str)

# text = ("When Sebastian Thrun started working on self-driving cars at "
#         "Google in 2007, few people outside of the company took him "
#         "seriously. “I can tell you very senior CEOs of major American "
#         "car companies would shake my hand and turn away because I wasn’t "
#         "worth talking to,” said Thrun, in an interview with Recode earlier "
#         "this week.")

info = (str[:975] + '..') if len(str) > 975 else str
info = info.replace('\n', '')
info = info.replace('        ## CHAPTER', '')
info = info.replace('�', '')

doc = nlp(info)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
#
# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)


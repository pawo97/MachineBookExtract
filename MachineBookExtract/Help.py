
# extract epub to text:
# https://github.com/kevinxiong/epub2txt

# import nltk
# from nameparser.parser import HumanName
#
# def get_human_names(text):
#     tokens = nltk.tokenize.word_tokenize(text)
#     pos = nltk.pos_tag(tokens)
#     sentt = nltk.ne_chunk(pos, binary = False)
#     person_list = []
#     person = []
#     name = ""
#     for subtree in sentt.subtrees(filter=lambda t: t.node == 'PERSON'):
#         for leaf in subtree.leaves():
#             person.append(leaf[0])
#         if len(person) > 1: #avoid grabbing lone surnames
#             for part in person:
#                 name += part + ' '
#             if name[:-1] not in person_list:
#                 person_list.append(name[:-1])
#             name = ''
#         person = []
#
#     return (person_list)
#
# text = """
# Some economists have responded positively to Bitcoin, including
# Francois R. Velde, senior economist of the Federal Reserve in Chicago
# who described it as "an elegant solution to the problem of creating a
# digital currency." In November 2013 Richard Branson announced that
# Virgin Galactic would accept Bitcoin as payment, saying that he had invested
# in Bitcoin and found it "fascinating how a whole new global currency
# has been created", encouraging others to also invest in Bitcoin.
# Other economists commenting on Bitcoin have been critical.
# Economist Paul Krugman has suggested that the structure of the currency
# incentivizes hoarding and that its value derives from the expectation that
# others will accept it as payment. Economist Larry Summers has expressed
# a "wait and see" attitude when it comes to Bitcoin. Nick Colas, a market
# strategist for ConvergEx Group, has remarked on the effect of increasing
# use of Bitcoin and its restricted supply, noting, "When incremental
# adoption meets relatively fixed supply, it should be no surprise that
# prices go up. And that’s exactly what is happening to BTC prices."
# """
#
# names = get_human_names(text)
# print("LAST, FIRST")
# for name in names:
#         last_first = HumanName(name).last + ', ' + HumanName(name).first
#         print(last_first)

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
# import nltk
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


##SPACY
# from collections import Counter
import re

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

# str = open('test111.txt',  encoding="utf8").read()
#
# #print(str)
#
# # text = ("When Sebastian Thrun started working on self-driving cars at "
# #         "Google in 2007, few people outside of the company took him "
# #         "seriously. “I can tell you very senior CEOs of major American "
# #         "car companies would shake my hand and turn away because I wasn’t "
# #         "worth talking to,” said Thrun, in an interview with Recode earlier "
# #         "this week.")
#
# info = (str[:999990] + '..') if len(str) > 999990 else str
# # info = info.replace('\n', '')
# # info = info.replace('        ## CHAPTER', '')
# # info = info.replace('�', '')
#
# doc = nlp(info)
#
# # Analyze syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
#
# # Find named entities, phrases and concepts
#
#
# for entity in doc.ents:
#         #if entity.label_ == 'PERSON':
#         #print(entity.text)
#         print(entity.text, entity.label_)

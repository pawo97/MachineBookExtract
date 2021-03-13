import nltk

text = "Bed and chair are types of furniture"

print(text)
#
# DT is the determinant
#
# VBP is the verb
#
# JJ is the adjective
#
# IN is the preposition
#
# NN is the noun

sentence = [("a", "DT"),("clever","JJ"),("fox","NN"),("was","VBP"),
   ("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]

grammar = "NP:{<DT>?<JJ>*<NN>}"

parser_chunking = nltk.RegexpParser(grammar)

parser_chunking.parse(sentence)

output = parser_chunking.parse(sentence)

output.draw()

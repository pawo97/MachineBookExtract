import spacy
import re
import time

from MachineBookExtract.ChaptersInBookTool import ChaptersInBookTool
from MachineBookExtract.DialogueTool import DialogueTool
from MachineBookExtract.PersonRate import PersonRate
from TestBook import TestBook


class BookAnalyzer:
        __doc__ = "Prepare book for analysie"
        def __init__(self, name):
                self.str = open(name,  encoding="utf8").read()
                self.chapters = ChaptersInBookTool()
                self.dialogues = DialogueTool()

                # self.str = open(r'Books/Alices Adventures in Wonderland by Lewis Carroll', encoding="utf8").read()
                # self.str = open(r'Books/A Christmas Carol by Charles Dickens',  encoding="utf8").read()
                # self.str = open(r'Books/Dracula by Bram Stoker', encoding="utf8").read()
                # self.str = open(r'Books/Moby Dick; Or, The Whale_Herman Melville',  encoding="utf8").read()
                # self.str = open(r'Books/Peter Pan by J. M. Barrie',  encoding="utf8").read()
                # self.str = open(r'Books/The Adventures of Sherlock Holmes by Arthur Conan Doyle',  encoding="utf8").read()
                # self.str = open(r'Books/The Castle of Otranto by Horace Walpole',  encoding="utf8").read()
                # self.str = open(r'Books/The Moonstone by Wilkie Collins',  encoding="utf8").read()
                # self.str = open(r'Books/The Odyssey by Homer',  encoding="utf8").read()
                # self.str = open(r'Books/Wuthering Heights by Emily Bronte',  encoding="utf8").read()

        def start(self):
                self.start = time.time()
                self.nlp = spacy.load("en_core_web_sm")
                self.nlp.max_length = 2_500_000
                str1 = self.str.split('PROJECT GUTENBERG EBOOK')
                str2 = str1[1].split('PROJECT GUTENBERG EBOOK')
                content = str2[0];
                # print("Book length: ", content.__len__())
                self.content = content
                self.doc = self.nlp(content)

        def getAvergeLengthOfSentenceInBook(self):
                workContent = self.content.replace('\n', ' ')
                sentences = re.split('[.!?]', workContent)
                sentencesCorrect = []
                for w in sentences:
                        if "Illustration" not in w and "CHAPTER" not in w and "BOOK" not in w:
                                sentencesCorrect.append(w)
                totalSum = len(workContent)
                sentencesRate = []
                for w in sentencesCorrect:
                        sentencesRate.append(w.__len__())

                averge = sum(sentencesRate) / len(sentences)
                print("Averge of sentence in book: ", averge, " chars")
                return averge

        def getAvergeWordInSentenceInBook(self):
                workContent = self.content.replace('\n', ' ')
                sentences = re.split('[.!?]', workContent)
                sentencesCorrect = []
                for w in sentences:
                        if "Illustration" not in w and "CHAPTER" not in w and "BOOK" not in w:
                                sentencesCorrect.append(w)
                totalSum = len(workContent)
                sentencesRate = []
                for w in sentencesCorrect:
                        words = w.split(' ')
                        sentencesRate.append(words.__len__())

                averge = sum(sentencesRate) / len(sentences)
                print("Averge of words in sentence in book: ", averge, " chars")
                return averge

        def getBookLength(self):
                workContent = self.content.replace('\n', ' ')
                print("Book length: ", workContent.__len__(), " chars")
                return workContent.__len__()

        def getAmountOfWords(self):
                words = self.content.split(' ')
                print("Words in book: ", words.__len__())
                return words.__len__()

        def getAmountOfDialogue(self):
                workContent = self.content.replace('\n', ' ')
                sentences = re.split('[.!?]', workContent)
                # for w in sentences:

        def getVerbsNow(self):
                print("Counting verbs")
                words = self.content.split(' ')
                pastVerbsSize = 0
                presentVerbsSize = 0
                for w in words:
                        doc = self.nlp(w)
                        if len(doc) > 0 and 'VBD' == doc[0].tag_:
                                pastVerbsSize += 1
                        if len(doc) > 0 and 'VB' == doc[0].tag_:
                                presentVerbsSize += 1

                total = presentVerbsSize + pastVerbsSize
                percentVerbsPresent = (presentVerbsSize * 100) / total
                percentVerbsPast = (pastVerbsSize * 100) / total

                print("Total verbs: " + str(total))
                print("Present: " + str(presentVerbsSize) + ' ' + str(percentVerbsPresent) + " %")
                print("Past: " + str(pastVerbsSize) + ' ' + str(percentVerbsPast) + " %")


        def getAmountOfAdjectives(self):
                words = self.content.split(' ')

                verbs = [token.lemma_ for token in self.doc if token.pos_ == "ADJ"]
                # adjectives = 0
                # for w in words:
                #         doc = self.nlp(w)
                #         if len(doc) > 0 and 'JJ' == doc[0].tag_:
                #                 adjectives += 1
                #         if len(doc) > 0 and 'JJR' == doc[0].tag_:
                #                 adjectives += 1
                #         if len(doc) > 0 and 'JJS' == doc[0].tag_:
                #                 adjectives += 1
                print(len(verbs))
                # print("Amount of adjectives " + str(adjectives))
                # return adjectives



        def getStatistics(self):
                # self.getAvergeLengthOfSentenceInBook()
                # self.getAvergeWordInSentenceInBook()
                # self.getBookLength()
                # self.getAmountOfWords()
                # self.getVerbsNow()
                self.dialogues.getAmountOfDialogues(self.content)
                # self.chapters.getAmountOfChaptersByTableOfContent(self.content)
                # self.chapters.getAmountOfChaptersByInsideOfContent(self.content )
                # self.getAmountOfAdjecti ves()

        def getCharactersInBook(self):
                #Words in all book
                blank = ' '
                words = self.content.split(' ')
                # print('compare words in book')
                # print(words)
                wordsSelected = []

                for w in words:
                        #blank
                        if w != '':
                                #Remove nonalphanumeric
                                alphanumeric = ""
                                for character in w:
                                        if character.isalnum():
                                                alphanumeric += character
                                wordsSelected.append(alphanumeric.lower())

                # print('compare words selected in book')
                # print(wordsSelected)

                # Nouns + Persons + Big literal
                # Nouns
                liNouns = [chunk.text for chunk in self.doc.noun_chunks]
                # z duzej litery

                # zaczyna sie na a, the
                liPrefix = []
                for s in liNouns:
                        sFinal = ''
                        if (s.startswith('a ') or s.startswith('A ')) and s[2].isupper() and 'CHAPTER' not in s:
                                sFinal = s[2:]
                                # print("LL", s[2:])
                                liPrefix.append(sFinal)
                        elif (s.startswith('the ') or s.startswith('The ')) and s[4].isupper() and 'CHAPTER' not in s:
                                sFinal = s[4:]
                                # print("LL", s[4:])
                                liPrefix.append(sFinal)

                #druga czesc wyrazu, gdyz nazwisko wazniejsze, albo white rabbit
                liPrefixNonSpace = []
                for i in liPrefix:
                        if ' ' in i:
                                j = i.split(' ')
                                if j.__len__() >= 2:
                                        liPrefixNonSpace.append(j[1])
                        else:
                                liPrefixNonSpace.append(i)

                #usuniecie alfanumerycznych znakow
                liPrefixNonAlphaNumeric = []
                for w in liPrefixNonSpace:
                        #blank
                        if w != '':
                                #Remove nonalphanumeric
                                alphanumeric = ""
                                for character in w:
                                        if character.isalnum():
                                                alphanumeric += character
                                liPrefixNonAlphaNumeric.append(alphanumeric.lower())

                #delete duplicates
                liPrefixNonAlphaNumeric = list(dict.fromkeys(liPrefixNonAlphaNumeric))
                # print(liPrefixNonAlphaNumeric)

                # Get persons
                liCharacters = []
                for entity in self.doc.ents:
                        if entity.label_ == 'PERSON':
                                if entity.text[0].isupper():
                                        liCharacters.append(entity.text)

                # Get persons
                liCharNotDuplicates = list(dict.fromkeys(liCharacters))
                # print("PERSONS")
                # print(liCharNotDuplicates)

                # Remove two words
                liCharPrefixNonSpace = []
                for i in liCharNotDuplicates:
                        i = i.replace('\n', ' ')
                        if ' ' in i:
                                j = i.split(' ')
                                if j.__len__() >= 2:
                                        liCharPrefixNonSpace.append(j[j.__len__() - 1])
                        else:
                                liCharPrefixNonSpace.append(i)

                # Remove 's
                liRemoveDotS = []
                # print(liCharPrefixNonSpace)
                for w in liCharPrefixNonSpace:
                        # blank
                        if w.endswith("’s"):
                                w = w[0:w.__len__() - 2]
                        liRemoveDotS.append(w)
                # print(liRemoveDotS)

                # Remove alphanumeric
                liCharNotAphaNumeric = []
                for w in liRemoveDotS:
                        #blank
                        if w != '':
                                #Remove nonalphanumeric
                                alphanumeric = ""
                                for character in w:
                                        if character.isalnum():
                                                alphanumeric += character
                                liCharNotAphaNumeric.append(alphanumeric.lower())

                # Remove duplicates
                liCharNotAphaNumeric = list(dict.fromkeys(liCharNotAphaNumeric))
                print(liCharNotAphaNumeric)

                # Two list togheter without duplicates
                liPersons = liCharNotAphaNumeric + liPrefixNonAlphaNumeric
                liPersons = list(dict.fromkeys(liPersons))
                # print(liPersons)
                # Delete verbs, adverbs, adjective
                # print("Verbs:", [token.lemma_ for token in self.doc if token.pos_ == "VERB"])

                # Create rating list
                # print(liPersons)
                liRatingPersons = []
                for p in liPersons:
                        if p != 'the' and p != 'a' and p.__len__() > 1:
                                # check spacy tag
                                doc = self.nlp(p)
                                # print(p, doc[0].tag_, end=" | ")
                                if 'NN' == doc[0].tag_:
                                        person = PersonRate()
                                        person.rate = 0
                                        person.word = p
                                        person.tag = doc[0].tag_
                                        liRatingPersons.append(person)
                                elif 'NNS' == doc[0].tag_:
                                        person = PersonRate()
                                        person.rate = 0
                                        person.word = p[0:p.__len__() - 1]
                                        person.tag = doc[0].tag_
                                        liRatingPersons.append(person)

                # print(wordsSelected)
                # for p in liRatingPersons:
                #         print(str(p.word) + ' ' + str(p.rate), end=' ')

                # Count in words
                for w in wordsSelected:
                        for p in liRatingPersons:
                                if p.word in w or p.word == w:
                                        p.rate += 1

                liRatingPersons.sort(key=lambda x: x.rate, reverse=True)
                del liRatingPersons[30:]
                # for p in liRatingPersons:
                #         print(str(p.word) + ' ' + str(p.tag) + ' ' + str(p.rate))

                return liRatingPersons

        def printExecutionTime(self):
                self.end = time.time()
                print("Execution time: ", self.end - self.start)

        def test(self):
                doc = self.nlp('Conrad')
                print(doc[0].tag_, end=" | ")



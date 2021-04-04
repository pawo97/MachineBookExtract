import spacy
import re
import time

from MachineBookExtract.PersonRate import PersonRate
from TestBook import TestBook


class BookAnalyzer:
        __doc__ = "Prepare book for analysie"
        def __init__(self, name):
                self.str = open(name,  encoding="utf8").read()

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

        def getAmountOfDialogues(self):
                dialouge = 0
                words = self.content.split(' ')
                for w in words:
                        if '“' in w:
                                dialouge += 1

                if dialouge < 20:
                        for w in words:
                                if '"' in w:
                                        dialouge += 1
                print("Amount of dialogue " + str(dialouge))
                return dialouge

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


        def getAmountOfChapters(self, name):
                chapter = 0
                words = self.content.split(' ')
                for w in words:
                        if name in w:
                                chapter += 1
                print("Amount of chapters " + str(int(chapter / 2)))
                return int(chapter / 2)

        def getStatistics(self):
                # self.getAvergeLengthOfSentenceInBook()
                # self.getAvergeWordInSentenceInBook()
                # self.getBookLength()
                # self.getAmountOfWords()
                # self.getVerbsNow()
                self.getAmountOfDialogues()
                self.getAmountOfChapters('CHAPTER')
                self.getAmountOfAdjectives()

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


if __name__ == "__main__":
        # analyzer = BookAnalyzer()
        # analyzer.start()
        # # analyzer.getAvergeOfSentenceInBook()
        # analyzer.getCharactersInBook()
        # analyzer.mainCharactersCheck()
        # # analyzer.printExecutionTime()

        #=======================================================================================

        # # Method test Alice
        # b = BookAnalyzer(r'Books/Alices Adventures in Wonderland by Lewis Carroll')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["rabbit", "queen", "king", "cat", "duchess", "hatter", "hare", "dormouse", "gryphon"], b, 'Alice Test')

        # # Method test Christmas Carol
        # b = BookAnalyzer(r'Books/A Christmas Carol by Charles Dickens')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["scrooge", "marley", "cratchit", "ghost", "tim", "fred", "fezziwig", "marta"], b, 'Christmas Test')
        #
        # # Method test Drakula
        # b = BookAnalyzer(r'Books/Dracula by Bram Stoker')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["lucy", "dracula", "harker", "lucy", "helsing", "renfield", "seward", "morris"], b,
        #                       'Dracula Test')
        #
        # Method test Moby
        # b = BookAnalyzer(r'Books/Moby Dick; Or, The Whale_Herman Melville')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["ahab", "dick", "ishmael", "queequeg", "mapple", "sam", "boomer", "sturbuck", "stubb", "elijah"], b,
        #                       'Moby Test')

        #=========================================================================================

        #Method test Peter
        # b = BookAnalyzer(r'Books/Peter Pan by J. M. Barrie')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["peter", "wendy", "hak", "darling", "lilia", "smee", "nibs", "rabbit", "bell"], b,
        #                       'Peter Test')
        #
        # Method test Sherlock
        # b = BookAnalyzer(r'Books/The Adventures of Sherlock Holmes by Arthur Conan Doyle')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["holmes", "watson", "lestrade", "bohemia", "adler", "wilson", "sutherland", "mccarthy"], b,
        #                       'Sherlock Test')
        #
        # Method test Castle
        # b = BookAnalyzer(r'Books/The Castle of Otranto by Horace Walpole')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["manfred", r"hippolita", "conrad", "matilda", r"isabella", "theodore", "jerome", "diego"], b,
        #                       'Castle Test')
        #
        # Method test Moonstone
        b = BookAnalyzer(r'Books/The Moonstone by Wilkie Collins')
        b.start()
        b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["verinder", "blake", "ablewhite", "betteredge", "jennings", "cuff", "clack", "bruff", "candy"], b,
        #                       'Moonstone Test')
        #
        # # Method test Odyssey
        b = BookAnalyzer(r'Books/The Odyssey by Homer')
        b.start()
        b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck([r"odysseus", r"apollo", r"penelope", r"agamemnon", r"queen", "zeus", r"neptune", "eurymachus", r"amphinomus"], b,
        #                       'Odyssey Test')
        #
        # # Method test Wuthering
        b = BookAnalyzer(r'Books/Wuthering Heights by Emily Bronte')
        b.start()
        b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["heathcliff", "catherine", "linton", "dean", "lockwood", "earnshaw", "linton", "joseph"], b,
        #                       'Wuthering Test')



# print("Noun phrases:", [chunk.text for chunk in self.doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in self.doc if token.pos_ == "VERB"])

# Nazwa książki	                Bohaterowie 	        Dopasowanie     max       Dopasowanie   min
# Alicja w krainie czarów     	9	                    9               69        9             30
# Chrismas Carol	            8	                    7               92        7             30
# Dracula	                    8                       7               249       4             30
# Moby Dick                     10                      6               678       1             30
# Peter Pan                     9                       4               57        4             30
# Sherlock Holmes               8                       7               211       1             30
# Castle of Othrando            8                       3               71        3             30
# Moonstone                     9                       7               287       5             30
# Odyssey                       9                       7               212       1             30
# Wuthering                     8                       8               73        8             30

#=================================================================================================
#Dlugosc zdan, ilosc slow, ilosc dialogow, stosunek czasow, podział na rozdziały
#=================================================================================================
# Nazwa książki                 Srednia dl zdan         Srednia ilosc slow w zdaniu     Ilosc znakow            Ilosc slow
# Alicja w krainie czarów       85                      17                              144787                  24643
# Chrismas Carol                73                      14                              164528                  26550
# Dracula                       87                      18                              846165                  153522
# Moby Dick                     112                     21                              1218971                 194862
# Peter Pan                     74                      15                              255622                  42847
# Sherlock Holmes               76                      15                              562425                  95606
# Castle of Othrando            93                      17                              210802                  33646
# Moonstone                     75                      15                              1073519                 177787
# Odyssey                       142                     28                              678977                  119465
# Wuthering                     87                      17                              645594                  105731
#=================================================================================================
# Nazwa książki               ilosc czaswonikow       czas teraz      present %       czas przeszly   past %
# Alicja w krainie czarów     3518                    1273            36              2245            63
# Chrismas Carol              3318                    1088            32              2230            67
# Dracula                     18699                   8651            46              10048           53
# Moby Dick                   17117                   8280            48              8837            51
# Peter Pan                   6360                    2131            33              4229            66
# Sherlock Holmes             11385                   4628            40              6757            59
# Castle of Othrando          4106                    1675            40              2431            59
# Moonstone                   21962                   8781            39              13181           60
# Odyssey                     14304                   6685            46              7619            53
# Wuthering                   13571                   6010            44              7561            55
#=================================================================================================
# Nazwa książki                 ilosc dialogow          rozdziały       przymiotniki
# Alicja w krainie czarów       1115                    12              1438
# Chrismas Carol                1127                    0               2193
# Dracula                       2516                    27              10004
# Moby Dick                     1606                    142             18065
# Peter Pan                     1424                    0               2568
# Sherlock Holmes               2703                    0               6656
# Castle of Othrando            1051                    2 (5)           2065
# Moonstone                     3109                    44              11295
# Odyssey                       1243                    0               6441
# Wuthering                     2303                    17              6821
# =================================================================================================
# Nazwa książki                 Czas akcji (oszacowany)         srednia dialogowa (znaki | slowa)      dlugie %    krotkie %
# Alicja w krainie czarów
# Chrismas Carol
# Dracula
# Moby Dick
# Peter Pan
# Sherlock Holmes
# Castle of Othrando
# Moonstone
# Odyssey
# Wuthering
# =================================================================================================
# Jesli ktos zaznaczy wlasciwych bohaterow i rozdzialy -> po rozdzialach bedziemy sprawdzali statystyke
# Rozdzial      Ktory Bohater w nim byl         Pozytywne Opis      Negatywne Opis      Czas w rozdziale        Nazwy geograficzne
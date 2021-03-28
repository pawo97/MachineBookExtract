import spacy
import re
import time

class BookAnalyzer:
        __doc__ = "Prepare book for analysie"
        def __init__(self):
                # self.str = open(r'Books/A Christmas Carol by Charles Dickens',  encoding="utf8").read()
                self.str = open(r'Books/Alices Adventures in Wonderland by Lewis Carroll',  encoding="utf8").read()
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
                print("Book length: ", content.__len__())
                self.doc = self.nlp(content)

        def getAvergeOfSentenceInBook(self):
                blank = ' '
                sentencesSum = 0
                counter = 0
                averge = 0
                special_characters = r"!@#$%^&*()-+?_=,<>/"

                for sent in self.doc.sents:
                        string_check = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
                        if string_check.search(sent.__str__()) == None:
                                if sent.__str__() != blank and '\n\n' not in sent.__str__():
                                        sentencesSum += len(sent)
                                        counter += 1
                                        #print(sent.__len__())
                if counter != 0:
                        averge = sentencesSum / counter
                print("Averge of sentence in book: ", averge, " chars")


        def getCharactersInBook(self):
                # print("Main")
                # Analyze syntax
                liNouns = [chunk.text for chunk in self.doc.noun_chunks]

                for s in liNouns:
                        s = s.replace(r'\n', ' ')

                print("Noun phrases:", [chunk.text for chunk in self.doc.noun_chunks])
                # print("Verbs:", [token.lemma_ for token in self.doc if token.pos_ == "VERB"])
                liCharacters = []

                for entity in self.doc.ents:
                        if entity.label_ == 'PERSON':
                                # print("Persons: [", end=" ")
                                # print(entity.text, end= " ")
                                # print("]")
                                if entity.text[0].isupper():
                                        liCharacters.append(entity.text)

                # Remove duplicates
                liCharNotDuplicates = list(dict.fromkeys(liCharacters))

                # attach nouns
                liPrefix = []
                print("The a :")
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

                # Remove duplicates
                liPrefix = list(dict.fromkeys(liPrefix))
                print(liPrefix)

                # Check is in Nouns
                liNounPerson = []
                for s in liCharNotDuplicates:
                        if s in liNouns:
                                liNounPerson.append(s)

                for s in liPrefix:
                        liNounPerson.append(s)

                # Count amount of apperiance in book
                liNounPerson = list(dict.fromkeys(liNounPerson))
                print(liNounPerson)
                blank = ' '

                liCharactersRates = []
                for s in liNounPerson:
                        p = PersonRate()
                        p.rate = 0
                        p.word = s
                        liCharactersRates.append(p)



                # Get words in sentence
                for sent in self.doc.sents:
                        string_check = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
                        if string_check.search(sent.__str__()) == None:
                                if sent.__str__() != blank and '\n\n' not in sent.__str__():
                                        words = sent.__str__().split(' ')
                                        for w in words:
                                                for s in liCharactersRates:
                                                        if s.word == w:
                                                                s.rate += 1

                liCharactersRates.sort(key=lambda x: x.rate, reverse=True)
                count = 0
                for s in liCharactersRates:
                        print(s)
                        count += 1
                        if count >= 10:
                                break

                # Get only 10 values with main character
                # The White Rabbit
                # The Queen of Hearts
                # The King of Hearts
                # The Cheshire Cat
                # The Duchess
                # The Duchess
                # The Mad Hatter
                # The March Hare
                # The Dormouse
                # The Gryphon
                # The Mock Turtle
                # Alice’s sister
                # Main characters:



        def printExecutionTime(self):
                self.end = time.time()
                print("Execution time: ", self.end - self.start)

class PersonRate:
        def __init__(self):
                self.rate = 0
                self.word = ''

        def __str__(self):
                return str(self.word) + " : " + str(self.rate)


if __name__ == "__main__":
        analyzer = BookAnalyzer()
        analyzer.start()
        #analyzer.getAvergeOfSentenceInBook()
        analyzer.getCharactersInBook()
        analyzer.printExecutionTime()


import spacy

import time

from MachineBookExtract.BookTools.BasicStatisticsTool import BasicStatisticsTool
from MachineBookExtract.BookTools.ChaptersInBookTool import ChaptersInBookTool
from MachineBookExtract.BookTools.CharactersTool import CharactersTool
from MachineBookExtract.BookTools.DialogueTool import DialogueTool
from MachineBookExtract.BookTools.TimeStatistics import TimeStatistics


class BookAnalyzer:
        __doc__ = "Prepare book for analysie"
        def __init__(self, name):
                self.str = open(name,  encoding="utf8").read()
                self.dialogues = DialogueTool()
                self.characters = CharactersTool()
                self.basicStatistics = BasicStatisticsTool()
                self.timeStatistics = TimeStatistics();

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

                self.chapters = ChaptersInBookTool(self.doc)

        def getAmountOfAdjectives(self):
                words = self.content.split(' ')

                adj = [token.lemma_ for token in self.doc if token.pos_ == "ADJ"]
                # adjectives = 0
                # for w in words:
                #         doc = self.nlp(w)
                #         if len(doc) > 0 and 'JJ' == doc[0].tag_:
                #                 adjectives += 1
                #         if len(doc) > 0 and 'JJR' == doc[0].tag_:
                #                 adjectives += 1
                #         if len(doc) > 0 and 'JJS' == doc[0].tag_:
                #                 adjectives += 1
                return adj
                # print("Amount of adjectives " + str(adjectives))
                # return adjectives



        def getStatistics(self):
                # self.getAvergeLengthOfSentenceInBook()
                # self.getAvergeWordInSentenceInBook()
                # self.getBookLength()
                # self.basicStatistics.getAmountOfWords(self.content)
                # self.basicStatistics.getBookLength(self.content)
                # self.basicStatistics.getAvergeLengthOfSentenceInBook(self.content)
                # self.basicStatistics.getAvergeWordInSentenceInBook(self.content)
                # self.timeStatistics.getVerbsNow(self.content, self.nlp)
                # self.dialogues.getAmountOfDialogues(self.content)
                # self.chapters.getAmountOfChaptersByTableOfContent(self.content)
                self.chapters.getAmountOfChaptersByInsideOfContent(self.content)
                # self.getAmountOfAdjecti ves()


        def printExecutionTime(self):
                self.end = time.time()
                print("Execution time: ", self.end - self.start)


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
        # # Method test Moby
        b = BookAnalyzer(r'Books/Moby Dick; Or, The Whale_Herman Melville')
        b.start()
        b.getStatistics()
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
        # # Method test Sherlock
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
        # Method test Methamorphios
        # b = BookAnalyzer(r'Books/Metamorphosis by Franz Kafka')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["verinder", "blake", "ablewhite", "betteredge", "jennings", "cuff", "clack", "bruff", "candy"], b,
        #                       'Moonstone Test')
        #
        # # Method test Pride
        # b = BookAnalyzer(r'Books/Pride and Prejudice by Jane Austen')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck([r"odysseus", r"apollo", r"penelope", r"agamemnon", r"queen", "zeus", r"neptune", "eurymachus", r"amphinomus"], b,
        #                       'Odyssey Test')
        #
        # # Method test Wuthering
        # b = BookAnalyzer(r'Books/Wuthering Heights by Emily Bronte')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["heathcliff", "catherine", "linton", "dean", "lockwood", "earnshaw", "linton", "joseph"], b,
        #                       'Wuthering Test')




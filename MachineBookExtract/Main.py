import math

import pandas as pd
import spacy
from spacy_syllables import SpacySyllables
import time

from MachineBookExtract.BookTools.AdjectiveTool import AdjectiveTool
from MachineBookExtract.BookTools.BasicStatisticsTool import BasicStatisticsTool
from MachineBookExtract.BookTools.ChaptersInBookTool import ChaptersInBookTool
from MachineBookExtract.BookTools.CharactersTool import CharactersTool
from MachineBookExtract.BookTools.DialogueTool import DialogueTool
from MachineBookExtract.BookTools.Redability import Readability
from MachineBookExtract.BookTools.TimeStatistics import TimeStatistics


class BookAnalyzer:
        __doc__ = "Prepare book for analysie"
        def __init__(self, name):
                self.str = open(name,  encoding="utf8").read()
                self.dialogues = DialogueTool()
                self.characters = CharactersTool()

        def start(self):
                self.start = time.time()
                self.nlp = spacy.load("en_core_web_sm")
                self.nlp.max_length = 2_500_000
                str1 = self.str.split('PROJECT GUTENBERG EBOOK')
                str2 = str1[1].split('PROJECT GUTENBERG EBOOK')
                content = str2[0];
                # print("Book length: ", content.__len__())
                self.content = content
                self.syllables = SpacySyllables(self.nlp, "en_US")
                self.nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})
                self.doc = self.nlp(content)

                self.chapters = ChaptersInBookTool(self.doc)
                self.basicStatistics = BasicStatisticsTool(self.content)

        def getStatistics(self):
                # TOTAL
                print('=============================')
                present, past = self.getTimeStatisticsTotal()
                print('=============================')
                self.getReadabilityTotal()
                print('=============================')
                self.getAdjectivesTotal()
                print('=============================')
                self.getBasicStatisticsTotal()
                print('=============================')
                self.getDialogesTotal()
                print('=============================')
                self.getChaptersAmount(present, past)
                print('=============================')
                # HEROES LIST AND AMOUNT
                print('=============================')

                # REST
                self.printExecutionTime()

        def getChaptersAmount(self, present, past):
                print("CHAPTERS AMOUNT", self.chapters.getAmountOfChaptersByInsideOfContent(self.content))
                # LOCAL
                f = self.chapters.getFragmentsOfBook()

                # BASIC
                df1 = self.chapters.getLengthWordCharsByChapter(f)

                # DIALOGES
                df2 = self.chapters.getStatisticsDialogByChapter(f)

                # ADJ
                df3 = self.chapters.getStatisticsAdjectiveByChapter(f, self.doc)

                # TIME STATISTICS
                df4 = self.chapters.getTimeStatisticsByChapter(f, self.doc, present, past)

                # HEROES

                # CONNECT
                # print(df1)
                # print(df2)
                # print(df3)
                # print(df4)

                # df5 = pd.DataFrame()
                # df1.append(df1)
                dat1 = pd.concat([df1, df2, df3, df4], axis=1)

                #EXCEL
                dat1.to_excel("newoutput.xlsx")

        def getCharactersTotal(self):
                pass

        def getDialogesTotal(self):
                dialoges = self.dialogues.getAmountOfDialogues(self.content, 'GLOBAL')
                dialogesAvergeWords = self.dialogues.dialougeAvergeWords(dialoges, len(dialoges))
                dialogesAvergeChars = self.dialogues.dialougeAvergeChars(dialoges, len(dialoges))
                longDialogueAmount, shortDialogueAmount = self.dialogues.dialogueLongShort(dialoges, dialogesAvergeWords)
                longDialoguePercent, shortDialoguePercent = self.dialogues.dialougeLongShortPercent(longDialogueAmount, shortDialogueAmount, dialoges)
                print("DIALGOES TOTAL ", len(dialoges))
                print("DIALGOES AVERGE WORDS", dialogesAvergeWords)
                print("DIALOGES AVERGE CHARS", dialogesAvergeChars)
                print("LONG DIALOGES WORDS ", longDialogueAmount)
                print("SHORT DIALOGES WORDS ", shortDialogueAmount)
                print("LONG DIALOGES PERCENT ", longDialoguePercent)
                print("SHORT DIALOGES PERCENT ", shortDialoguePercent)

        def getBasicStatisticsTotal(self):
                print("SENTENCES AMOUNT ", len(self.basicStatistics.sentences))
                print("SENTENCES AVERGE BY CHARS ", self.basicStatistics.getAvergeLengthOfSentenceInBook(self.content))
                print("SENTENCES AVERGE BY WORDS ", self.basicStatistics.getAvergeWordInSentenceInBook())
                print("BOOK LENGTH CHARS", self.basicStatistics.getBookLength(self.content))
                print("BOOK LENGTH WORDS ", self.basicStatistics.getAmountOfWords(self.content))

        def getAdjectivesTotal(self):
                self.adjectives = AdjectiveTool(self.doc)
                print("ADJECTIVES AMOUNT", self.adjectives.getAmountOfAdjectivesTotal())

        def getReadabilityTotal(self):
                self.readability = Readability(self.doc, self.basicStatistics, self.content)
                print("FRE Readability", self.readability.getMcLaughlinFRERedability())
                print("SMOG Readability", self.readability.getMcLaughlinSMOGRedability())
                print("FOG Readability", self.readability.getMcLaughlinFOGRedability())

        def getTimeStatisticsTotal(self):
                self.timeStatistics = TimeStatistics()
                present = self.timeStatistics.getVerbsNowAmount(self.doc)
                past = self.timeStatistics.getVerbsPastAmount(self.doc)

                print("TOTAL AMOUNT", len(present) + len(past))
                print("PRESENT AMOUNT", len(present))
                print("PRESENT PERCENT", self.timeStatistics.getVerbsNowPercent(self.doc))
                print("PAST AMOUNT", len(past))
                print("PAST PERCENT", self.timeStatistics.getVerbsPastPercent(self.doc))

                return present, past

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
        b = BookAnalyzer(r'Books/Alices Adventures in Wonderland by Lewis Carroll')
        b.start()
        b.getStatistics()
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




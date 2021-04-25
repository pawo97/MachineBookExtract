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

        # PODZIELIĆ NA SAVE, OUTPUT, GUI
        # WYGENEROWAĆ DLA WSZYSTKICH
        # ANALIZA DANYCH
        # OTESTOWAĆ TO
        def getStatisticsOutput(self, name):
                # TOTAL
                # print('=============================')
                present, past, s1 = self.getTimeStatisticsTotal()
                # print('=============================')
                s2 = self.getReadabilityTotal()
                # print('=============================')
                s3 = self.getAdjectivesTotal()
                # print('=============================')
                s4 = self.getBasicStatisticsTotal()
                # print('=============================')
                s5 = self.getDialogesTotal()
                # print('=============================')
                li, s6 = self.getCharactersTotal(self.content, self.doc, self.nlp)
                # print('=============================')
                self.getChaptersAmount(present, past, li, name)
                # print('=============================')

                # REST
                s7 = self.printExecutionTime()

                # SAVE
                s0 = s1 + '\n' + s2 + '\n' + s3 + '\n' + s4 + '\n' + s5 + '\n' + s6 + '\n' + s7
                text_file = open(r'MachineBookExtract/Output/' + str(name) + " BASIC.txt", "w")
                text_file.write(s0)
                text_file.close()

        def getStatisticsPrint(self, name):
                # TOTAL
                # print('=============================')
                present, past, s1 = self.getTimeStatisticsTotal()
                # print('=============================')
                s2 = self.getReadabilityTotal()
                # print('=============================')
                s3 = self.getAdjectivesTotal()
                # print('=============================')
                s4 = self.getBasicStatisticsTotal()
                # print('=============================')
                s5 = self.getDialogesTotal()
                # print('=============================')
                li, s6 = self.getCharactersTotal(self.content, self.doc, self.nlp)
                # print('=============================')
                # self.getChaptersAmount(present, past, li, name)
                # print('=============================')

                # REST
                s7 = self.printExecutionTime()

                # SAVE
                s0 = s1 + '\n' + s2 + '\n' + s3 + '\n' + s4 + '\n' + s5 + '\n' + s6 + '\n' + s7
                print(s0)

        def getChaptersAmount(self, present, past, characters, name):
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
                df5 = self.chapters.getCharactersInChapters(f, characters)

                # CONNECT
                # print(df1)
                # print(df2)
                # print(df3)
                # print(df4)

                # df5 = pd.DataFrame()
                # df1.append(df1)
                dat1 = pd.concat([df1, df2, df3, df4, df5], axis=1)

                #EXCEL
                dat1.to_excel(r'MachineBookExtract/Output/' + str(name) + " CHAPTERS.xlsx")

        def getCharactersTotal(self, content, doc, nlp):
                chT = CharactersTool()
                li = chT.getCharactersInBook(content, doc, nlp)
                # print(li)
                return li, li.__str__()

        def getDialogesTotal(self):
                dialoges = self.dialogues.getAmountOfDialogues(self.content, 'GLOBAL')
                dialogesAvergeWords = self.dialogues.dialougeAvergeWords(dialoges, len(dialoges))
                dialogesAvergeChars = self.dialogues.dialougeAvergeChars(dialoges, len(dialoges))
                longDialogueAmount, shortDialogueAmount = self.dialogues.dialogueLongShort(dialoges, dialogesAvergeWords)
                longDialoguePercent, shortDialoguePercent = self.dialogues.dialougeLongShortPercent(longDialogueAmount, shortDialogueAmount, dialoges)

                s1 = "DIALGOES TOTAL " + str(len(dialoges)) + "\n"
                s2 = "DIALGOES AVERGE WORDS " + str(dialogesAvergeWords)+ "\n"
                s3 = "DIALOGES AVERGE CHARS " + str(dialogesAvergeChars)+ "\n"
                s4 = "LONG DIALOGES WORDS " + str(longDialogueAmount)+ "\n"
                s5 = "SHORT DIALOGES WORDS " + str(shortDialogueAmount)+ "\n"
                s6 = "LONG DIALOGES PERCENT "+ str(longDialoguePercent)+ "\n"
                s7 = "SHORT DIALOGES PERCENT "+ str(shortDialoguePercent)+ "\n"
                s0 = s1 + s2 + s3 + s4 + s5 + s6 + s7

                # print("DIALGOES TOTAL ", len(dialoges))
                # print("DIALGOES AVERGE WORDS", dialogesAvergeWords)
                # print("DIALOGES AVERGE CHARS", dialogesAvergeChars)
                # print("LONG DIALOGES WORDS ", longDialogueAmount)
                # print("SHORT DIALOGES WORDS ", shortDialogueAmount)
                # print("LONG DIALOGES PERCENT ", longDialoguePercent)
                # print("SHORT DIALOGES PERCENT ", shortDialoguePercent)

                return s0


        def getBasicStatisticsTotal(self):
                s1 = "SENTENCES AMOUNT " + str(len(self.basicStatistics.sentences))+ "\n"
                s2 = "SENTENCES AVERGE BY CHARS "+ str( self.basicStatistics.getAvergeLengthOfSentenceInBook(self.content))+ "\n"
                s3 = "SENTENCES AVERGE BY WORDS "+ str(self.basicStatistics.getAvergeWordInSentenceInBook())+ "\n"
                s4 = "BOOK LENGTH CHARS "+ str( self.basicStatistics.getBookLength(self.content))+ "\n"
                s5 = "BOOK LENGTH WORDS "+ str( self.basicStatistics.getAmountOfWords(self.content))+ "\n"
                s0 = s1 + s2 + s3 + s4 + s5
                # print("SENTENCES AMOUNT ", len(self.basicStatistics.sentences))
                # print("SENTENCES AVERGE BY CHARS ", self.basicStatistics.getAvergeLengthOfSentenceInBook(self.content))
                # print("SENTENCES AVERGE BY WORDS ", self.basicStatistics.getAvergeWordInSentenceInBook())
                # print("BOOK LENGTH CHARS", self.basicStatistics.getBookLength(self.content))
                # print("BOOK LENGTH WORDS ", self.basicStatistics.getAmountOfWords(self.content))
                return s0

        def getAdjectivesTotal(self):
                self.adjectives = AdjectiveTool(self.doc)
                # print("ADJECTIVES AMOUNT", self.adjectives.getAmountOfAdjectivesTotal())
                s1 = "ADJECTIVES AMOUNT " + str(self.adjectives.getAmountOfAdjectivesTotal()) + "\n"
                return s1

        def getReadabilityTotal(self):
                self.readability = Readability(self.doc, self.basicStatistics, self.content)
                # print("FRE Readability", self.readability.getMcLaughlinFRERedability())
                # print("SMOG Readability", self.readability.getMcLaughlinSMOGRedability())
                # print("FOG Readability", self.readability.getMcLaughlinFOGRedability())

                s1 = "FRE Readability " + str(self.readability.getMcLaughlinFRERedability()) + "\n"
                s2 = "SMOG Readability "+ str(self.readability.getMcLaughlinSMOGRedability()) + "\n"
                s3 = "FOG Readability "+ str(self.readability.getMcLaughlinFOGRedability()) + "\n"
                s0 = s1 + s2 + s3
                return s0

        def getTimeStatisticsTotal(self):
                self.timeStatistics = TimeStatistics()
                present = self.timeStatistics.getVerbsNowAmount(self.doc)
                past = self.timeStatistics.getVerbsPastAmount(self.doc)

                # print("TOTAL AMOUNT", len(present) + len(past))
                # print("PRESENT AMOUNT", len(present))
                # print("PRESENT PERCENT", self.timeStatistics.getVerbsNowPercent(self.doc))
                # print("PAST AMOUNT", len(past))
                # print("PAST PERCENT", self.timeStatistics.getVerbsPastPercent(self.doc))

                s1 = "TOTAL AMOUNT " + str(len(present)) + str(len(past))+ "\n"
                s2 = "PRESENT AMOUNT "+ str(len(present))+ "\n"
                s3 = "PRESENT PERCENT "+ str(self.timeStatistics.getVerbsNowPercent(self.doc))+ "\n"
                s4 = "PAST AMOUNT "+ str(len(past))+ "\n"
                s5 = "PAST PERCENT "+ str(self.timeStatistics.getVerbsPastPercent(self.doc))+ "\n"
                s0 = s1 + s2 + s3 + s4 + s5

                return present, past, s0

        def printExecutionTime(self):
                self.end = time.time()
                print("Execution time: ", self.end - self.start)
                s1 = "Execution time: " + str((self.end - self.start))
                return s1


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
        # b.getStatisticsOutput("Alices")
        # t = TestBook()
        # t.mainCharactersCheck(["rabbit", "queen", "king", "cat", "duchess", "hatter", "hare", "dormouse", "gryphon"], b, 'Alice Test')

        # # Method test Christmas Carol
        # b = BookAnalyzer(r'Books/A Christmas Carol by Charles Dickens')
        # b.start()
        # b.getStatisticsOutput("Christmas")
        # t = TestBook()
        # t.mainCharactersCheck(["scrooge", "marley", "cratchit", "ghost", "tim", "fred", "fezziwig", "marta"], b, 'Christmas Test')
        #
        # # Method test Drakula
        # b = BookAnalyzer(r'Books/Dracula by Bram Stoker')
        # b.start()
        # b.getStatisticsOutput("Dracula")
        # b.getStatisticsPrint("Dracula")
        # t = TestBook()
        # t.mainCharactersCheck(["lucy", "dracula", "harker", "lucy", "helsing", "renfield", "seward", "morris"], b,
        #                       'Dracula Test')
        #
        # # Method test Moby
        # b = BookAnalyzer(r'Books/Moby Dick; Or, The Whale_Herman Melville')
        # b.start()
        # b.getStatisticsOutput("Moby")
        # t = TestBook()
        # t.mainCharactersCheck(["ahab", "dick", "ishmael", "queequeg", "mapple", "sam", "boomer", "sturbuck", "stubb", "elijah"], b,
        #                       'Moby Test')

        # Method test Peter
        b = BookAnalyzer(r'MachineBookExtract/Books/Peter Pan by J. M. Barrie')
        b.start()
        b.getStatisticsOutput("Peter")
        # t = TestBook()
        # t.mainCharactersCheck(["peter", "wendy", "hak", "darling", "lilia", "smee", "nibs", "rabbit", "bell"], b,
        #                       'Peter Test')
        #=========================================================================================

        # # Method test Sherlock
        # b = BookAnalyzer(r'MachineBookExtract/Books/The Adventures of Sherlock Holmes by Arthur Conan Doyle')
        # b.start()
        # b.getStatisticsOutput("Sherlock")
        # t = TestBook()
        # t.mainCharactersCheck(["holmes", "watson", "lestrade", "bohemia", "adler", "wilson", "sutherland", "mccarthy"], b,
        #                       'Sherlock Test')
        #
        # Method test Castle
        # b = BookAnalyzer(r'Books/The Castle of Otranto by Horace Walpole')
        # b.start()
        # b.getStatisticsOutput("Castle")
        # t = TestBook()
        # t.mainCharactersCheck(["manfred", r"hippolita", "conrad", "matilda", r"isabella", "theodore", "jerome", "diego"], b,
        #                       'Castle Test')
        #
        # Method test Methamorphios
        # b = BookAnalyzer(r'Books/Metamorphosis by Franz Kafka')
        # b.start()
        # b.getStatisticsOutput("Metamorphosis")
        # t = TestBook()
        # t.mainCharactersCheck(["verinder", "blake", "ablewhite", "betteredge", "jennings", "cuff", "clack", "bruff", "candy"], b,
        #                       'Moonstone Test')
        #
        # # Method test Pride
        # b = BookAnalyzer(r'Books/Pride and Prejudice by Jane Austen')
        # b.start()
        # b.getStatisticsOutput("Pride")
        # t = TestBook()
        # t.mainCharactersCheck([r"odysseus", r"apollo", r"penelope", r"agamemnon", r"queen", "zeus", r"neptune", "eurymachus", r"amphinomus"], b,
        #                       'Odyssey Test')
        #
        # # Method test Wuthering
        # b = BookAnalyzer(r'Books/Wuthering Heights by Emily Bronte')
        # b.start()
        # b.getStatisticsOutput("Wuthering")
        # t = TestBook()
        # t.mainCharactersCheck(["heathcliff", "catherine", "linton", "dean", "lockwood", "earnshaw", "linton", "joseph"], b,
        #                       'Wuthering Test')




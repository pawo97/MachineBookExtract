import pandas as pd
import spacy
from spacy_syllables import SpacySyllables
import time

from book_tools.adjective_tool import adjective_tool
from book_tools.basic_statistics_tool import basic_statistics_tool
from book_tools.ChaptersInBookTool import ChaptersInBookTool
from book_tools.CharactersTool import CharactersTool
from book_tools.DialogueTool import DialogueTool
from book_tools.Redability import Readability
from book_tools.TimeStatistics import TimeStatistics


class BookAnalyzer:
    __doc__ = "Prepare book for analysie"

    def __init__(self, content):
        self.str = content
        self.dialogues = DialogueTool()
        self.characters = CharactersTool()

    # =========================================================================================================================
    # Start function
    # =========================================================================================================================
    def start(self):
        self.start = time.time()
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.max_length = 2_500_000
        str1 = self.str.split('PROJECT GUTENBERG EBOOK')
        str2 = str1[1].split('PROJECT GUTENBERG EBOOK')
        content = str2[0]

        self.content = content
        self.syllables = SpacySyllables(self.nlp, "en_US")
        self.nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})

        self.doc = self.nlp(content)
        self.chapters = ChaptersInBookTool(self.doc)
        self.basicStatistics = basic_statistics_tool(self.content)


    # =========================================================================================================================
    # Print function
    # =========================================================================================================================
    def getCharactersTotal(self, content, doc, nlp):
        chT = CharactersTool()
        li = chT.getCharactersInBook(content, doc, nlp)
        li1 = chT.getPercentStatisticsInBook(content, li)
        return li, str(len(li)), li1

    def getDialogesTotal(self):
        dialoges = self.dialogues.getAmountOfDialogues(self.content)
        dialogesAvergeWords = self.dialogues.dialougeAvergeWords(dialoges, len(dialoges))
        dialogesAvergeChars = self.dialogues.dialougeAvergeChars(dialoges, len(dialoges))
        longDialogueAmount, shortDialogueAmount = self.dialogues.dialoguesLongShortAmount(dialoges, dialogesAvergeWords)
        longDialoguePercent, shortDialoguePercent = self.dialogues.dialoguesLongShortPercent(longDialogueAmount,
                                                                                             shortDialogueAmount,
                                                                                             dialoges)
        s1 = "DIALGOES TOTAL " + str(len(dialoges)) + "\n"
        s2 = "DIALGOES AVERGE WORDS " + str(dialogesAvergeWords) + "\n"
        s3 = "DIALOGES AVERGE CHARS " + str(dialogesAvergeChars) + "\n"
        s4 = "LONG DIALOGES WORDS " + str(longDialogueAmount) + "\n"
        s5 = "SHORT DIALOGES WORDS " + str(shortDialogueAmount) + "\n"
        s6 = "LONG DIALOGES PERCENT " + str(longDialoguePercent) + "\n"
        s7 = "SHORT DIALOGES PERCENT " + str(shortDialoguePercent) + "\n"
        s0 = s1 + s2 + s3 + s4 + s5 + s6 + s7

        return s0

    def getAdjectivesTotal(self):
        self.adjectives = adjective_tool(self.doc)
        s1 = "ADJECTIVES AMOUNT " + str(self.adjectives.get_amount_of_adjectives()) + "\n"
        return s1

    def getReadabilityTotal(self):
        self.readability = Readability(self.doc, self.basicStatistics, self.content)

        s1 = "FRE Readability " + str(self.readability.getMcLaughlinFRERedability()) + "\n"
        s2 = "SMOG Readability " + str(self.readability.getMcLaughlinSMOGRedability()) + "\n"
        s3 = "FOG Readability " + str(self.readability.getMcLaughlinFOGRedability()) + "\n"
        s0 = s1 + s2 + s3
        return s0

    def getTimeStatisticsTotal(self):
        self.timeStatistics = TimeStatistics()
        present = self.timeStatistics.getVerbsNowAmount(self.doc)
        past = self.timeStatistics.getVerbsPastAmount(self.doc)

        s1 = "TOTAL AMOUNT " + str(len(present)) + str(len(past)) + "\n"
        s2 = "PRESENT AMOUNT " + str(len(present)) + "\n"
        s3 = "PRESENT PERCENT " + str(self.timeStatistics.getVerbsNowPercent(self.doc)) + "\n"
        s4 = "PAST AMOUNT " + str(len(past)) + "\n"
        s5 = "PAST PERCENT " + str(self.timeStatistics.getVerbsPastPercent(self.doc)) + "\n"
        s0 = s1 + s2 + s3 + s4 + s5

        return present, past, s0

    def printExecutionTime(self):
        self.end = time.time()
        # print("Execution time: ", self.end - self.start)
        s1 = "Execution time: " + str((self.end - self.start))
        return s1

    def getBasicStatisticsTotal(self):
        s1 = "SENTENCES AMOUNT " + str(len(self.basicStatistics.sentences)) + "\n"
        s2 = "SENTENCES AVERGE BY CHARS " + str(
            self.basicStatistics.get_average_chars_of_sentence(self.content)) + "\n"
        s3 = "SENTENCES AVERGE BY WORDS " + str(self.basicStatistics.get_average_words_in_sentence()) + "\n"
        s4 = "BOOK LENGTH CHARS " + str(self.basicStatistics.get_book_length_chars(self.content)) + "\n"
        s5 = "BOOK LENGTH WORDS " + str(self.basicStatistics.get_book_length_words(self.content)) + "\n"
        s0 = s1 + s2 + s3 + s4 + s5
        return s0

    # =========================================================================================================================
    # Output print function
    # =========================================================================================================================
    def getStatisticsPrint(self):
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
        li, s6, li1 = self.getCharactersTotal(self.content, self.doc, self.nlp)
        # print('=============================')
        self.getChaptersAmountPrint(present, past, li)
        # print('=============================')

        # REST
        s7 = self.printExecutionTime()

        # SAVE
        s0 = s1 + '\n' + s2 + '\n' + s3 + '\n' + s4 + '\n' + s5 + '\n' + s6 + '\n' + s7 + '\n' + str(li1)
        print(s0)

    def getChaptersAmountPrint(self, present, past, characters):
        self.chapters.getAmountOfChaptersByInsideOfContent(self.content)
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
        dat1 = pd.concat([df1, df2, df3, df4, df5], axis=1)

    # =========================================================================================================================
    # Output save function
    # =========================================================================================================================
    def getChaptersAmountOutput(self, present, past, characters, name):
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

        # EXCEL
        dat1.to_excel(r'output/' + str(name) + " CHAPTERS.xlsx")

    def getStatisticsOutput(self, name):
        # TOTAL
        # print('=============================')
        present, past, s1 = self.getTimeStatisticsTotal()
        # print('=============================')
        s2 = self.getReadabilityTotal()
        # self.progressBar.setValue(30)
        # print('=============================')
        s3 = self.getAdjectivesTotal()
        # self.progressBar.setValue(40)
        # print('=============================')
        s4 = self.getBasicStatisticsTotal()
        # self.progressBar.setValue(50)
        # print('=============================')
        s5 = self.getDialogesTotal()
        # self.progressBar.setValue(60)
        # print('=============================')
        li, s6, li1 = self.getCharactersTotal(self.content, self.doc, self.nlp)
        # self.progressBar.setValue(70)
        # print('=============================')
        self.getChaptersAmountOutput(present, past, li, name)
        # print('=============================')

        # REST
        s7 = self.printExecutionTime()
        # self.progressBar.setValue(100)
        # SAVE
        s0 = s1 + '\n' + s2 + '\n' + s3 + '\n' + s4 + '\n' + s5 + '\n' + s6 + '\n' + s7 + '\n' + str(li1)
        text_file = open(r'output/' + str(name) + "_BASIC.txt", "w")
        text_file.write(s0)
        text_file.close()

    # =========================================================================================================================
    # GUI controllers
    # =========================================================================================================================

    def getBookLengthChars(self):
        return str(self.basicStatistics.get_book_length_chars(self.content))

    def getBookLengthWords(self):
        return str(self.basicStatistics.get_book_length_words(self.content))

    def getBookSentenceAmount(self):
        return str(len(self.basicStatistics.sentences))

    def getBookSentenceAverageChars(self):
        return str(int(self.basicStatistics.get_average_chars_of_sentence(self.content)))

    def getBookSentenceAverageWords(self):
        return str(int(self.basicStatistics.get_average_words_in_sentence()))

    def getTotalVerbsStatisticsAmount(self):
        present = len(self.timeStatistics.getVerbsNowAmount(self.doc))
        past = len(self.timeStatistics.getVerbsPastAmount(self.doc))
        total = present + past
        presentPercent = self.timeStatistics.getVerbsNowPercent(self.doc)
        pastPercent = self.timeStatistics.getVerbsPastPercent(self.doc)
        return str(total), str(present), str(past), presentPercent, pastPercent

    def getFRESMOGFOGReadability(self):
        self.readability = Readability(self.doc, self.basicStatistics, self.content)

        s1 = str(round(self.readability.getMcLaughlinFRERedability(), 2))
        s2 = str(round(self.readability.getMcLaughlinSMOGRedability(), 2))
        s3 = str(round(self.readability.getMcLaughlinFOGRedability(), 2))
        return s1, s2, s3

    def getAdjectivesAmount(self):
        self.adjectives = adjective_tool(self.doc)
        return str(self.adjectives.get_amount_of_adjectives())

    def getDialogesAmounts(self):
        dialoges = self.dialogues.getAmountOfDialogues(self.content)
        dialogesAvergeWords = self.dialogues.dialougeAvergeWords(dialoges, len(dialoges))
        dialogesAvergeChars = self.dialogues.dialougeAvergeChars(dialoges, len(dialoges))
        longDialogueAmount, shortDialogueAmount = self.dialogues.dialoguesLongShortAmount(dialoges, dialogesAvergeWords)
        longDialoguePercent, shortDialoguePercent = self.dialogues.dialoguesLongShortPercent(longDialogueAmount,
                                                                                             shortDialogueAmount,
                                                                                             dialoges)

        s1 = str(len(dialoges))
        s2 = str(round(dialogesAvergeWords, 2))
        s3 = str(round(dialogesAvergeChars, 2))
        s4 = str(longDialogueAmount)
        s5 = str(shortDialogueAmount)
        return s1, s2, s3, s4, s5, longDialoguePercent, shortDialoguePercent

    def getCharactersList(self, content, doc, nlp):
        chT = CharactersTool()
        li = chT.getCharactersInBook(content, doc, nlp)
        return li

    def getFragmentsAndChapters(self):
        amount = self.chapters.getAmountOfChaptersByInsideOfContent(self.content)
        f = self.chapters.getFragmentsOfBook()
        # BASIC
        df1 = self.chapters.getLengthWordCharsByChapter(f)

        # DIALOGES
        df2 = self.chapters.getStatisticsDialogByChapter(f)

        # ADJ
        df3 = self.chapters.getStatisticsAdjectiveByChapter(f, self.doc)

        # TIME STATISTICS
        present, past, s1 = self.getTimeStatisticsTotal()
        df4 = self.chapters.getTimeStatisticsByChapter(f, self.doc, present, past)

        # HEROES
        characters, s6, li1 = self.getCharactersTotal(self.content, self.doc, self.nlp)
        df5 = self.chapters.getCharactersInChapters(f, characters)

        dat1 = pd.concat([df1, df2, df3, df4, df5], axis=1)
        return amount, f, dat1

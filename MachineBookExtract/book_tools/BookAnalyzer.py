import traceback

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

    def __init__(self, content):
        """Prepare book for analyse"""
        # fields other
        self.content_clean = None
        self.content = None

        self.start_time = 0
        self.end_time = 0
        self.analyse_time = 0

        # fields analyse
        self.book_chars_amount = None
        self.book_words_amount = None

        self.book_sentences = None
        self.book_sentences_amount = None
        self.book_sentences_average_chars = None
        self.book_sentences_average_words = None

        self.fre = None
        self.fog = None
        self.smog = None

        self.total_vb = None
        self.present_vb = None
        self.past_vb = None
        self.present_vb_p = None
        self.past_vb_p = None

        self.dialogues = None
        self.dialogues_amount = None
        self.dialogues_long_a = None
        self.dialogues_short_a = None
        self.dialogues_long_p = None
        self.dialogues_short_p = None
        self.dialogues_average_chars = None
        self.dialogues_average_words = None

        self.total_adj = None
        self.characters = []

        # books
        self.str = content

    # =========================================================================================================================
    # Start function
    # =========================================================================================================================
    def start(self):
        self.start_time = time.time()
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.max_length = 2_500_000

        if 'PROJECT GUTENBERG EBOOK' in self.str:
            str1 = self.str.split('PROJECT GUTENBERG EBOOK')
            str2 = str1[1].split('PROJECT GUTENBERG EBOOK')
            content = str2[0]

        else:
            content = self.str

        self.content = content
        self.syllables = SpacySyllables(self.nlp, "en_US")
        self.nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})

        # create analyse classes
        self.basic_s_tool = basic_statistics_tool()
        self.read_s_tool = Readability()
        self.time_s_tool = TimeStatistics()
        self.dial_s_tool = DialogueTool()
        self.adj_s_tool = adjective_tool()
        self.char_s_tool = CharactersTool()

        # clean txt
        content_clean = self.basic_s_tool.clean_text(content)

        # start analyse
        self.doc = self.nlp(content_clean)
        self.chapters = ChaptersInBookTool(self.doc)

        # fill fields
        self.book_chars_amount = self.basic_s_tool.get_book_length_chars(self.doc.text)
        self.book_words_amount = self.basic_s_tool.get_book_length_words(self.doc.text)

        self.book_sentences = self.basic_s_tool.get_sentences(self.doc.text)
        self.book_sentences_amount = len(self.basic_s_tool.get_sentences(self.doc.text))
        self.book_sentences_average_chars = round(self.basic_s_tool.get_average_chars_of_sentence(self.book_sentences), 2)
        self.book_sentences_average_words = round(self.basic_s_tool.get_average_words_in_sentence(self.book_sentences), 2)

        self.fre = round(self.read_s_tool.getMcLaughlinFRERedability(self.doc, self.book_words_amount, self.book_sentences_amount), 2)
        self.fog = round(self.read_s_tool.getMcLaughlinFOGRedability(self.doc, self.book_words_amount, self.book_sentences_amount), 2)
        self.smog = round(self.read_s_tool.getMcLaughlinSMOGRedability(self.doc, self.book_sentences_amount), 2)

        self.present_vb = len(self.time_s_tool.getVerbsPresentAmount(self.doc))
        self.past_vb = len(self.time_s_tool.getVerbsPastAmount(self.doc))
        self.total_vb = int(self.present_vb) + int(self.past_vb)
        self.present_vb_p = self.time_s_tool.getVerbsNowPercent(self.present_vb, self.past_vb)
        self.past_vb_p = self.time_s_tool.getVerbsPastPercent(self.present_vb, self.past_vb)

        self.dialogues = self.dial_s_tool.getAmountOfDialogues(self.content)
        self.dialogues_amount = len(self.dialogues)
        self.dialogues_average_chars = round(self.dial_s_tool.dialougeAvergeChars(self.dialogues, self.dialogues_amount), 2)
        self.dialogues_average_words = round(self.dial_s_tool.dialougeAvergeWords(self.dialogues, self.dialogues_amount), 2)
        self.dialogues_long_a = self.dial_s_tool.dialoguesLongAmount(self.dialogues, self.dialogues_average_words)
        self.dialogues_short_a = self.dial_s_tool.dialoguesShortAmount(self.dialogues, self.dialogues_average_words)
        self.dialogues_long_p = round(self.dial_s_tool.dialoguesLongPercent(self.dialogues_long_a, self.dialogues), 2)
        self.dialogues_short_p = round(self.dial_s_tool.dialoguesLongPercent(self.dialogues_short_a, self.dialogues), 2)

        self.total_adj = self.adj_s_tool.get_amount_of_adjectives(self.doc)

        self.characters = self.char_s_tool.getCharactersInBook(self.doc.text, self.doc, self.nlp)

        self.end_time = time.time()
        self.analyse_time = round((self.end_time - self.start_time), 2)



    def getChaptersAmountPrint(self, present, past, characters):
        try:
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

        except Exception as e:
            print(traceback.format_exc())

    # =========================================================================================================================
    # Output save function
    # =========================================================================================================================
    def getChaptersAmountOutput(self, present, past, characters, name):
        # print("CHAPTERS AMOUNT", self.chapters.getAmountOfChaptersByInsideOfContent(self.content))
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


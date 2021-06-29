import traceback

import pandas as pd
import spacy
from spacy_syllables import SpacySyllables
import time

from book_tools.adjective_tool import adjective_tool
from book_tools.basic_statistics_tool import basic_statistics_tool
from book_tools.chapters_tool import chapters_tool
from book_tools.characters_tool import characters_tool
from book_tools.dialogue_tool import dialogue_tool
from book_tools.readability_tool import readability_tool
from book_tools.time_statistics_tool import time_statistics_tool

class book_analyser_global:

    def __init__(self, content):
        """Prepare book for analyse"""
        # fields other
        self.content_clean = None
        self.content = None
        self.old_content = content

        self.start_time = 0
        self.end_time = 0
        self.analyse_time = 0

        # fields analyse
        self.book_chars_amount = None
        self.book_words = None
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

        self.present_vb_list = []
        self.past_vb_list = []

        self.dialogues = None
        self.dialogues_amount = None
        self.dialogues_long_a = None
        self.dialogues_short_a = None
        self.dialogues_long_p = None
        self.dialogues_short_p = None
        self.dialogues_average_chars = None
        self.dialogues_average_words = None

        self.total_adj = None
        self.adj_list = []

        self.characters = []
        self.chap_value = 0
        self.chap_inside = True
        self.fragments = []
        self.fragments_s = []

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
        self.read_s_tool = readability_tool()
        self.time_s_tool = time_statistics_tool()
        self.dial_s_tool = dialogue_tool()
        self.adj_s_tool = adjective_tool()
        self.char_s_tool = characters_tool()
        self.chap_s_tool = chapters_tool()

        # clean txt
        content_clean = self.basic_s_tool.clean_text(content)

        # start analyse
        self.doc = self.nlp(content_clean)

        # fill fields
        self.book_chars_amount = self.basic_s_tool.get_book_length_chars(self.doc.text)
        self.book_words = self.basic_s_tool.get_book_words(self.doc.text)
        self.book_words_amount = len(self.basic_s_tool.get_book_words(self.doc.text))

        self.book_sentences = self.basic_s_tool.get_sentences(self.doc.text)
        self.book_sentences_amount = len(self.basic_s_tool.get_sentences(self.doc.text))
        self.book_sentences_average_chars = round(self.basic_s_tool.get_average_chars_of_sentence(self.book_sentences), 2)
        self.book_sentences_average_words = round(self.basic_s_tool.get_average_words_in_sentence(self.book_sentences), 2)

        self.fre = round(self.read_s_tool.get_McL_FRE_readability(self.doc, self.book_words_amount, self.book_sentences_amount), 2)
        self.fog = round(self.read_s_tool.get_McL_FOG_readability(self.doc, self.book_words_amount, self.book_sentences_amount), 2)
        self.smog = round(self.read_s_tool.get_McL_SMOG_readability(self.doc, self.book_sentences_amount), 2)

        self.present_vb_list = self.time_s_tool.get_present_verbs(self.doc)
        self.past_vb_list = self.time_s_tool.get_past_verbs(self.doc)

        self.present_vb = len(self.present_vb_list)
        self.past_vb = len(self.past_vb_list)
        self.total_vb = int(self.present_vb) + int(self.past_vb)
        self.present_vb_p = self.time_s_tool.get_present_verbs_percent(self.present_vb, self.past_vb)
        self.past_vb_p = self.time_s_tool.get_past_verbs_percent(self.present_vb, self.past_vb)

        self.dialogues = self.dial_s_tool.get_dialogues(self.doc.text)
        self.dialogues_amount = len(self.dialogues)
        self.dialogues_average_chars = round(self.dial_s_tool.dialogue_average_chars(self.dialogues, self.dialogues_amount), 2)
        self.dialogues_average_words = round(self.dial_s_tool.dialogue_average_words(self.dialogues, self.dialogues_amount), 2)
        self.dialogues_long_a = self.dial_s_tool.dialogues_long_amount(self.dialogues, self.dialogues_average_words)
        self.dialogues_short_a = self.dial_s_tool.dialogues_short_amount(self.dialogues, self.dialogues_average_words)
        self.dialogues_long_p = round(self.dial_s_tool.dialogues_long_percent(self.dialogues_long_a, self.dialogues), 2)
        self.dialogues_short_p = round(self.dial_s_tool.dialogues_long_percent(self.dialogues_short_a, self.dialogues), 2)

        self.adj_list = self.adj_s_tool.get_amount_of_adjectives(self.doc)
        self.total_adj = len(self.adj_list)

        self.characters = self.char_s_tool.get_characters(self.book_words, self.doc, self.nlp)

        self.fragments = self.chap_s_tool.get_chapters_content(self.content)
        self.chap_value = len(self.fragments)
        if self.chap_value != 0 and self.chap_value != 1:
            self.chap_inside = True
        else:
            self.chap_inside = False

        self.end_time = time.time()
        self.analyse_time = round((self.end_time - self.start_time), 2)

        self.fragments_s = self.chap_s_tool.get_local_statistics(self.fragments, self.present_vb_list, self.past_vb_list, self.adj_list, self.characters)



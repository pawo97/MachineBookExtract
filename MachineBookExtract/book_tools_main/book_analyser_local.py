from book_tools.adjective_tool import adjective_tool
from book_tools.basic_statistics_tool import basic_statistics_tool
# from book_tools.ChaptersInBookTool import ChaptersInBookTool
from book_tools.characters_tool import characters_tool
from book_tools.dialogue_tool import dialogue_tool
from book_tools import read_statistics_tool
from book_tools.time_statistics_tool import time_statistics_tool

class book_analyser_local:

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
        self.book_words = []

        self.book_sentences = None
        self.book_sentences_amount = None
        self.book_sentences_average_chars = None
        self.book_sentences_average_words = None

        self.total_vb = None
        self.present_vb = None
        self.past_vb = None

        self.dialogues = None
        self.dialogues_amount = None
        self.dialogues_average_words = None
        self.dialogues_long_a = None
        self.dialogues_short_a = None

        self.total_adj = None
        self.characters = []

        # books
        self.str = content

    # =========================================================================================================================
    # Start function
    # =========================================================================================================================
    def start_chapter(self, content, vb_present, vb_past, adjs, characters):

        # create analyse classes
        self.basic_s_tool = basic_statistics_tool()
        self.time_s_tool = time_statistics_tool()
        self.dial_s_tool = dialogue_tool()
        self.adj_s_tool = adjective_tool()
        self.char_s_tool = characters_tool()

        # clean txt
        self.content_clean = self.basic_s_tool.clean_text(content)

        # fill fields
        self.book_chars_amount = self.basic_s_tool.get_book_length_chars(self.content_clean)
        self.book_words_amount = len(self.basic_s_tool.get_book_words(self.content_clean))
        self.book_words = self.basic_s_tool.get_book_words(self.content_clean)

        self.book_sentences = self.basic_s_tool.get_sentences(self.content_clean)
        self.book_sentences_amount = len(self.basic_s_tool.get_sentences(self.content_clean))
        self.book_sentences_average_chars = round(self.basic_s_tool.get_average_chars_of_sentence(self.book_sentences), 2)
        self.book_sentences_average_words = round(self.basic_s_tool.get_average_words_in_sentence(self.book_sentences), 2)

        self.dialogues = self.dial_s_tool.get_dialogues(self.content_clean)
        self.dialogues_amount = len(self.dialogues)
        self.dialogues_average_words = round(self.dial_s_tool.dialogue_average_words(self.dialogues, self.dialogues_amount), 2)

        self.dialogues_long_a = self.dial_s_tool.dialogues_long_amount(self.dialogues, self.dialogues_average_words)
        self.dialogues_short_a = self.dial_s_tool.dialogues_short_amount(self.dialogues, self.dialogues_average_words)

        # set of verbs present, past and adj
        vb_present = list(set(vb_present))
        vb_past = list(set(vb_past))
        adjs = list(set(adjs))

        # get amounts
        self.present_vb = self.get_present_verbs_l(self.book_words, vb_present)
        self.past_vb = self.get_past_verbs_l(self.book_words, vb_past)
        self.total_vb = self.present_vb + self.past_vb

        self.total_adj = self.get_adj_amount_l(self.book_words, adjs)

        self.characters = self.get_characters(self.book_words, characters)


    def get_present_verbs_l(self, words, present):
        present = list(set(present))
        counter = 0
        for w in words:
            if w in present:
                counter += 1

        return counter

    def get_past_verbs_l(self, words, past):
        counter = 0
        for w in words:
            if w in past:
                counter += 1

        return counter

    def get_adj_amount_l(self, words, adjs):
        counter = 0
        for w in words:
            if w in adjs:
                counter += 1

        return counter

    def get_characters(self, words, characters):
        heroes_list = []
        for c in characters:
            if c in words:
                heroes_list.append(c)

        return heroes_list
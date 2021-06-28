import unittest
import spacy
from spacy_syllables import SpacySyllables

from book_tools.adjective_tool import adjective_tool
from book_tools.basic_statistics_tool import basic_statistics_tool
from book_tools.readability_tool import readability_tool


class adjective_tool_test(unittest.TestCase):

    def test_get_syllables(self):
        str_test = 'I see pretty and old cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000

        syllables = SpacySyllables(nlp, "en_US")
        nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})

        doc = nlp(str_test)
        readability_tool_t = readability_tool()
        syllables = readability_tool_t.get_syllables(doc)
        self.assertEqual(syllables, 9)

    def test_get_poli_syllables(self):
        str_test = 'I see pretty and attractive cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000

        syllables = SpacySyllables(nlp, "en_US")
        nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})

        doc = nlp(str_test)
        readability_tool_t = readability_tool()
        syllables = readability_tool_t.get_poli_syllables(doc)
        self.assertEqual(syllables, 3)

    def test_get_poli_syllables_not_noun(self):
        str_test = 'I see pretty and attractive cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000

        syllables = SpacySyllables(nlp, "en_US")
        nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})

        doc = nlp(str_test)
        readability_tool_t = readability_tool()
        syllables = readability_tool_t.get_poli_syllables_not_noun(doc)
        self.assertEqual(syllables, 3)

    def test_get_McL_FRE_readability(self):
        str_test = 'I see pretty and attractive cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000

        syllables = SpacySyllables(nlp, "en_US")
        nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})

        doc = nlp(str_test)
        readability_tool_t = readability_tool()
        syllables = readability_tool_t.get_poli_syllables_not_noun(doc)

        basic_statistics = basic_statistics_tool()
        sentences = basic_statistics.get_sentences(doc.text)
        words = basic_statistics.get_book_words(doc.text)

        fre_factor = readability_tool_t.get_McL_FRE_readability(doc, len(words), len(sentences))

        self.assertEqual(fre_factor, 82.39)

    def test_get_McL_SMOG_readability(self):
        str_test = 'I see pretty and attractive cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000

        syllables = SpacySyllables(nlp, "en_US")
        nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})

        doc = nlp(str_test)
        readability_tool_t = readability_tool()
        syllables = readability_tool_t.get_poli_syllables_not_noun(doc)

        basic_statistics = basic_statistics_tool()
        sentences = basic_statistics.get_sentences(doc.text)
        words = basic_statistics.get_book_words(doc.text)

        fre_factor = readability_tool_t.get_McL_SMOG_readability(doc, len(sentences))

        self.assertEqual(fre_factor, 4.94)

    def test_get_McL_FOG_readability(self):
        str_test = 'I see pretty and attractive cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000

        syllables = SpacySyllables(nlp, "en_US")
        nlp.add_pipe("syllables", after="tagger", config={"lang": "en_US"})

        doc = nlp(str_test)
        readability_tool_t = readability_tool()
        syllables = readability_tool_t.get_poli_syllables_not_noun(doc)

        basic_statistics = basic_statistics_tool()
        sentences = basic_statistics.get_sentences(doc.text)
        words = basic_statistics.get_book_words(doc.text)

        fre_factor = readability_tool_t.get_McL_FOG_readability(doc, len(words), len(sentences))

        self.assertEqual(fre_factor, 18.2)
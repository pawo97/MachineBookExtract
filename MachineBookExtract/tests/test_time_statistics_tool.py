import unittest

import spacy

# For unitpycharmtest use this import
# from MachineBookExtract.book_tools.TimeStatistics import TimeStatistics

# For test coverage use this import
from book_tools.time_statistics_tool import time_statistics_tool


class test_time_statistics_tool(unittest.TestCase):

    def test_get_present_verbs(self):
        str_test = 'I see pretty and old cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        time_statistics_tool_t = time_statistics_tool()
        verbs = time_statistics_tool_t.get_present_verbs(doc)
        self.assertEqual(verbs, ['see'])

    def test_get_past_verbs(self):
        str_test = 'I saw pretty and old cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        time_statistics_tool_t = time_statistics_tool()
        verbs = time_statistics_tool_t.get_past_verbs(doc)
        self.assertEqual(verbs, ['saw'])

    def test_get_total_verbs(self):
        str_test = 'I saw pretty and I see cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        time_statistics_tool_t = time_statistics_tool()
        verbs_amount = time_statistics_tool_t.get_total_verbs(doc)
        self.assertEqual(verbs_amount, 2)

    def test_get_present_verbs_percent(self):
        str_test = 'I saw pretty and I see cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        time_statistics_tool_t = time_statistics_tool()
        verbs_present = time_statistics_tool_t.get_present_verbs(doc)
        verbs_past = time_statistics_tool_t.get_past_verbs(doc)
        present_percent = time_statistics_tool_t.get_present_verbs_percent(len(verbs_present), len(verbs_past))
        self.assertEqual(present_percent, 50.0)

    def test_get_past_verbs_percent(self):
        str_test = 'I saw pretty and I see cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        time_statistics_tool_t = time_statistics_tool()
        verbs_present = time_statistics_tool_t.get_present_verbs(doc)
        verbs_past = time_statistics_tool_t.get_past_verbs(doc)
        present_percent = time_statistics_tool_t.get_past_verbs_percent(len(verbs_present), len(verbs_past))
        self.assertEqual(present_percent, 50.0)

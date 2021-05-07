import unittest

import spacy

# For unitpycharmtest use this import
# from MachineBookExtract.book_tools.TimeStatistics import TimeStatistics

# For test coverage use this import
from book_tools.TimeStatistics import TimeStatistics


class test_time_statistics(unittest.TestCase):

    def test_getVerbsPastAmount(self):
        str = 'I was in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str)
        time_s = TimeStatistics()
        verbs_now = len(time_s.getVerbsPastAmount(doc))
        self.assertEqual(verbs_now, 1)

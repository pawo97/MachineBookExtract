import unittest

import spacy

# For unitpycharmtest use this import
# from MachineBookExtract.book_tools.AdjectiveTool import AdjectiveTool

# For test coverage use this import
from book_tools.AdjectiveTool import AdjectiveTool


class TestBasicMethods(unittest.TestCase):

    def test_adj_amount(self):
        str = 'I have a nice car'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str)
        adj = AdjectiveTool(doc)
        adjLen = adj.getAmountOfAdjectivesTotal()
        self.assertEqual(adjLen, 1)

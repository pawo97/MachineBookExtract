import unittest

import spacy

# For unitpycharmtest use this import
# from MachineBookExtract.book_tools.AdjectiveTool import AdjectiveTool

# For test coverage use this import
from book_tools.adjective_tool import adjective_tool


class TestBasicMethods(unittest.TestCase):

    def test_adj_amount(self):
        str = 'I have a nice car'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str)
        adj = adjective_tool(doc)
        adjLen = adj.get_amount_of_adjectives()
        self.assertEqual(adjLen, 1)

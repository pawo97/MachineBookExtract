import unittest
import spacy
from book_tools.adjective_tool import adjective_tool


class adjective_tool_test(unittest.TestCase):

    def test_adjectives_amount(self):
        pass
        str_test = 'I see pretty and old cat in school'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        adjective_tool_test = adjective_tool(doc)
        adj = adjective_tool_test.get_amount_of_adjectives()
        self.assertEqual(adj, 2)
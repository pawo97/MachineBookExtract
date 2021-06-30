import unittest

import spacy

from book_tools.characters_tool import characters_tool
from book_tools.characters_person_rate import characters_person_rate


class test_characters_tool(unittest.TestCase):

    def test_get_list_non_alpha_numeric(self):
        str_test = 'I& see^& pretty& and old ,cat. in* school'
        words = str_test.split(' ')
        characters_tool_t = characters_tool()

        words_output = characters_tool_t.get_list_non_alpha_numeric(words)

        words_expected = ['i', 'see', 'pretty', 'and', 'old', 'cat', 'in', 'school']
        self.assertEqual(words_expected, words_output)

    def test_get_second_word(self):
        characters_tool_t = characters_tool()
        words_input = ['Tom Johnson', 'Adam', 'Adam Smith', 'Isa']

        words_output = characters_tool_t.get_second_word(words_input)

        words_expected = ['Johnson', 'Adam', 'Smith', 'Isa']
        self.assertEqual(words_expected, words_output)

    def test_get_words_with_prefix(self):
        characters_tool_t = characters_tool()
        words_input = ['a Johnson', 'the Adam', 'A Smith', 'The Isa']

        words_output = characters_tool_t.get_words_with_prefix(words_input)

        words_expected = ['Johnson', 'Adam', 'Smith', 'Isa']
        self.assertEqual(words_expected, words_output)

    def test_get_persons_no_duplicates(self):
        str_test = 'I saw Tom in school. He is a friend of mine. I like playing football with him.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        characters_tool_t = characters_tool()

        words_output = characters_tool_t.get_persons_no_duplicates(doc)

        words_expected = ['Tom']
        self.assertEqual(words_expected, words_output)

    def test_get_last_word(self):
        characters_tool_t = characters_tool()
        words_input = ['a Smith Johnson', 'the Adam', 'A John Smith', 'Isa']

        words_output = characters_tool_t.get_last_word(words_input)

        words_expected = ['Johnson', 'Adam', 'Smith', 'Isa']
        self.assertEqual(words_expected, words_output)

    def test_remove_dot_s(self):
        characters_tool_t = characters_tool()
        words_input = ['Johnson’s', 'Adam’s', 'Smith’s', 'Isa’s']

        words_output = characters_tool_t.remove_dot_s(words_input)

        words_expected = ['Johnson', 'Adam', 'Smith', 'Isa']
        self.assertEqual(words_expected, words_output)

    def test_check_spacy_tags(self):
        words = ['I', 'saw', 'Tom', 'in', 'school.', 'He', 'is', 'a', 'friend', 'of', 'mine.', 'I', 'like', 'playing', 'football', 'with', 'Tom']
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        persons = ['Tom']
        characters_tool_t = characters_tool()

        words_output = characters_tool_t.check_spacy_tags(nlp, words, persons)

        p = characters_person_rate()
        p.word = 'Tom'
        p.rate = 2
        p.tag = 'NNP'

        words_expected = [p]

        self.assertEqual(words_expected[0].word, words_output[0].word)
        self.assertEqual(words_expected[0].rate, words_output[0].rate)
        self.assertEqual(words_expected[0].tag, words_output[0].tag)

    def test_capital_letter_and_not_empty_str_list(self):
        characters_tool_t = characters_tool()
        persons = ['adam', '', 'ewa', 'isa', 'alice', '', 'rose']

        persons_output = characters_tool_t.capital_letter_and_not_empty_str_list(persons)

        persons_expected = ['Adam', 'Ewa', 'Isa', 'Alice', 'Rose']
        self.assertEqual(persons_expected, persons_output)

    def test_sum_lists_rates(self):
        characters_tool_t = characters_tool()
        persons_v1 = ['Adam', 'Tom', 'Smith', 'Alice', 'Mary']
        persons_v2 = ['Adam', 'Ewa', 'Isa', 'Alice', 'Rose']
        persons_v3 = ['Adam', 'Marie', 'Izak', 'Anabel', 'Dad']

        persons_output = characters_tool_t.sum_lists_rates(persons_v1, persons_v2, persons_v3)

        persons_expected = ['adam', 'tom', 'smith', 'alice', 'mary', 'ewa', 'isa', 'rose', 'marie', 'izak', 'anabel', 'dad']
        self.assertEqual(persons_expected, persons_output)

    def test_get_characters(self):
        words = ['I', 'saw', 'Tom', 'in', 'school.', 'He', 'is', 'a', 'friend', 'of', 'mine.', 'I', 'like', 'playing',
                 'football', 'with', 'Tom']
        str_test = 'I saw Tom in school. He is a friend of mine. I like playing football with him.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        characters_tool_t = characters_tool()

        persons_output = characters_tool_t.get_characters(words, doc, nlp)

        persons_expected = ['Tom']

        self.assertEqual(persons_expected, persons_output)

import unittest

import spacy

from book_tools.basic_statistics_tool import basic_statistics_tool


class test_basic_statistics_tool(unittest.TestCase):

    def test_get_sentences(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool()
        sentences = basic_statistics.get_sentences(doc.text)
        correct_sentences = ['I see pretty and old cat in school', 'My lessons was very boring today']
        self.assertEqual(sentences, correct_sentences)

    def test_get_correct_sentences(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today. [Illustration].'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool()
        sentences = basic_statistics.get_sentences(doc.text)
        correct_sentences = basic_statistics.get_correct_sentences(sentences)
        correct_sentences_expected = ['I see pretty and old cat in school', 'My lessons was very boring today']
        self.assertEqual(correct_sentences_expected, correct_sentences)

    def test_get_average_chars_of_sentence(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool()
        sentences = basic_statistics.get_sentences(doc.text)
        average_char_sentences = basic_statistics.get_average_chars_of_sentence(sentences)
        average_char_sentences_correct = 33.0
        self.assertEqual(average_char_sentences, average_char_sentences_correct)

    def test_get_average_words_in_sentence(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool()

        sentences = basic_statistics.get_sentences(doc.text)
        average_word_sentences = basic_statistics.get_average_words_in_sentence(sentences)
        average_word_sentences_correct = 7
        self.assertEqual(average_word_sentences, average_word_sentences_correct)

    def test_get_book_length_chars(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool()

        book_length = basic_statistics.get_book_length_chars(str_test)
        book_length_correct = len(str_test)
        self.assertEqual(book_length, book_length_correct)

    def test_get_book_words(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool()

        book_words = basic_statistics.get_book_words(str_test)
        book_words_correct = ['I', 'see', 'pretty', 'and', 'old', 'cat', 'in', 'school.', 'My', 'lessons', 'was', 'very', 'boring', 'today.']
        self.assertEqual(book_words, book_words_correct)

    def test_clean_text(self):
        str_test = 'I *see pretty* and [old] cat in school.\n My* [lessons] was--very* boring today.\n\'illustration\''
        str_expected = 'I see pretty and old cat in school. My lessons was very boring today. '

        basic_statistics = basic_statistics_tool()

        str_test_method = basic_statistics.clean_text(str_test)
        self.assertEqual(str_test_method, str_expected)
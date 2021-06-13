import unittest

import spacy

from book_tools.basic_statistics_tool import basic_statistics_tool


class AdjectiveToolTest(unittest.TestCase):

    def test_get_sentences(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool(str_test)
        sentences = basic_statistics.get_sentences()
        correct_sentences = ['I see pretty and old cat in school', 'My lessons was very boring today']
        self.assertEqual(sentences, correct_sentences)

    def test_get_correct_sentences(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today. [Illustration].'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool(str_test)
        sentences = basic_statistics.get_sentences()
        correct_sentences = ['I see pretty and old cat in school', 'My lessons was very boring today']
        self.assertEqual(sentences, correct_sentences)

    def test_get_average_char_in_sentence_in_book(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool(str_test)

        average_char_sentences = basic_statistics.get_average_chars_of_sentence()
        average_char_sentences_correct = 33.0
        self.assertEqual(average_char_sentences, average_char_sentences_correct)

    def test_get_average_word_in_sentence_in_book(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool(str_test)

        average_word_sentences = basic_statistics.get_average_words_in_sentence()
        average_word_sentences_correct = 7
        self.assertEqual(average_word_sentences, average_word_sentences_correct)

    def test_get_book_length(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool(str_test)

        book_length = basic_statistics.get_book_length_chars(str_test)
        book_length_correct = len(str_test)
        self.assertEqual(book_length, book_length_correct)

    def test_get_get_amount_of_words(self):
        str_test = 'I see pretty and old cat in school. My lessons was very boring today.'
        nlp = spacy.load("en_core_web_sm")
        nlp.max_length = 2_500_000
        doc = nlp(str_test)
        basic_statistics = basic_statistics_tool(str_test)

        book_words = basic_statistics.get_book_length_words(str_test)
        book_words_correct = 14
        self.assertEqual(book_words, book_words_correct)


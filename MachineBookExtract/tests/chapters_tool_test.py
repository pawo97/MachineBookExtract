import unittest

import spacy

# For unitpycharmtest use this import
# from MachineBookExtract.book_tools.AdjectiveTool import AdjectiveTool

# For test coverage use this import
from book_tools.adjective_tool import adjective_tool
from book_tools.chapters_tool import chapters_tool


class chapters_tool_test(unittest.TestCase):

    def test_get_chapters_position(self):
        pass

    def test_get_fragments(self):
        lines = ['CHAPTER 1', 'My friends like go to school.', 'CHAPTER 2', 'My name is Tom.', 'I am 14', 'CHAPTER 3', 'My dog like playing football.']
        numbers_list = [0, 2, 5]
        fragments_correct = ['My friends like go to school.\n', 'My name is Tom.\nI am 14\n', 'My dog like playing football.\n']

        chapters_tool_t = chapters_tool()
        fragments = chapters_tool_t.get_fragments(numbers_list, lines)
        self.assertEqual(fragments, fragments_correct)

    def test_get_chapters_content(self):
        pass

    def test_sort_and_order(self):
        pass

    def test_get_local_statistics(self):
        pass

    def test_check_if_roman_numeral_true(self):
        chapters_tool_t = chapters_tool()
        is_roman = chapters_tool_t.check_if_roman_numeral('VII')
        self.assertEqual(is_roman, True)

    def test_check_if_roman_numeral_false(self):
        chapters_tool_t = chapters_tool()
        is_roman = chapters_tool_t.check_if_roman_numeral('V123II')
        self.assertEqual(is_roman, False)

    def test_decimal_to_roman(self):
        chapters_tool_t = chapters_tool()
        decimal_number = chapters_tool_t.decimal_to_roman('V')
        self.assertEqual(decimal_number, 5)

    def test_decimal_to_roman_str(self):
        chapters_tool_t = chapters_tool()
        roman_number = chapters_tool_t.decimal_to_roman_str('III')
        self.assertEqual(roman_number, 3)

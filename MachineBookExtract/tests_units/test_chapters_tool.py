import unittest

import pandas as pd

# For test coverage use this import
from pandas._testing import assert_frame_equal

from book_tools.chapters_tool import chapters_tool


# For unitpycharmtest use this import
# from MachineBookExtract.book_tools.AdjectiveTool import AdjectiveTool

class test_chapters_tool(unittest.TestCase):

    def test_get_chapters_position_roman_dot(self):
        content = '\n\n\nChapter I.\n\n\n' \
                  'My friends like go to school.\n' \
                  'I like walking around house.' \
                  '\n\n\nChapter II.\n\n\n' \
                  'My name is Tom.\n' \
                  'I am 14' \
                  '\n\n\nChapter III.\n\n\n' \
                  'My dog like playing football.' \
                  '\n\n\n'
        fragments_correct = [3, 10, 17]
        lines_correct = ['',
                         '',
                         '',
                         'Chapter I.',
                         '',
                         '',
                         'My friends like go to school.',
                         'I like walking around house.',
                         '',
                         '',
                         'Chapter II.',
                         '',
                         '',
                         'My name is Tom.',
                         'I am 14',
                         '',
                         '',
                         'Chapter III.',
                         '',
                         '',
                         'My dog like playing football.',
                         '',
                         '',
                         '']

        chapters_tool_t = chapters_tool()
        fragments = chapters_tool_t.get_chapters_position(content)
        self.assertEqual((lines_correct, fragments_correct), fragments)

    def test_get_chapters_position_roman(self):
        content = '\n\n\nChapter I\n\n\n' \
                  'My friends like go to school.\n' \
                  'I like walking around house.' \
                  '\n\n\nChapter II\n\n\n' \
                  'My name is Tom.\n' \
                  'I am 14' \
                  '\n\n\nChapter III\n\n\n' \
                  'My dog like playing football.' \
                  '\n\n\n'
        fragments_correct = [3, 10, 17]
        lines_correct = ['',
                         '',
                         '',
                         'Chapter I',
                         '',
                         '',
                         'My friends like go to school.',
                         'I like walking around house.',
                         '',
                         '',
                         'Chapter II',
                         '',
                         '',
                         'My name is Tom.',
                         'I am 14',
                         '',
                         '',
                         'Chapter III',
                         '',
                         '',
                         'My dog like playing football.',
                         '',
                         '',
                         '']

        chapters_tool_t = chapters_tool()
        fragments = chapters_tool_t.get_chapters_position(content)
        self.assertEqual((lines_correct, fragments_correct), fragments)

    def test_get_chapters_position_roman_only(self):
        content = '\n\n\nI\n\n\n' \
                  'My friends like go to school.\n' \
                  'I like walking around house.' \
                  '\n\n\nII\n\n\n' \
                  'My name is Tom.\n' \
                  'I am 14' \
                  '\n\n\nIII\n\n\n' \
                  'My dog like playing football.' \
                  '\n\n\n'
        fragments_correct = [3, 10, 17]
        lines_correct = ['',
                         '',
                         '',
                         'I',
                         '',
                         '',
                         'My friends like go to school.',
                         'I like walking around house.',
                         '',
                         '',
                         'II',
                         '',
                         '',
                         'My name is Tom.',
                         'I am 14',
                         '',
                         '',
                         'III',
                         '',
                         '',
                         'My dog like playing football.',
                         '',
                         '',
                         '']

        chapters_tool_t = chapters_tool()
        fragments = chapters_tool_t.get_chapters_position(content)
        self.assertEqual((lines_correct, fragments_correct), fragments)

    def test_get_chapters_position_number(self):
        content = '\n\n\nChapter 1\n\n\n' \
                  'My friends like go to school.\n' \
                  'I like walking around house.' \
                  '\n\n\nChapter 2\n\n\n' \
                  'My name is Tom.\n' \
                  'I am 14' \
                  '\n\n\nChapter 3\n\n\n' \
                  'My dog like playing football.' \
                  '\n\n\n'
        fragments_correct = [3, 10, 17]
        lines_correct = ['',
                         '',
                         '',
                         'Chapter 1',
                         '',
                         '',
                         'My friends like go to school.',
                         'I like walking around house.',
                         '',
                         '',
                         'Chapter 2',
                         '',
                         '',
                         'My name is Tom.',
                         'I am 14',
                         '',
                         '',
                         'Chapter 3',
                         '',
                         '',
                         'My dog like playing football.',
                         '',
                         '',
                         '']

        chapters_tool_t = chapters_tool()
        fragments = chapters_tool_t.get_chapters_position(content)
        self.assertEqual((lines_correct, fragments_correct), fragments)

    def test_get_chapters_position_number_dot(self):
        content = '\n\n\nChapter 1.\n\n\n' \
                  'My friends like go to school.\n' \
                  'I like walking around house.' \
                  '\n\n\nChapter 2.\n\n\n' \
                  'My name is Tom.\n' \
                  'I am 14' \
                  '\n\n\nChapter 3.\n\n\n' \
                  'My dog like playing football.' \
                  '\n\n\n'
        fragments_correct = [3, 10, 17]
        lines_correct = ['',
                         '',
                         '',
                         'Chapter 1.',
                         '',
                         '',
                         'My friends like go to school.',
                         'I like walking around house.',
                         '',
                         '',
                         'Chapter 2.',
                         '',
                         '',
                         'My name is Tom.',
                         'I am 14',
                         '',
                         '',
                         'Chapter 3.',
                         '',
                         '',
                         'My dog like playing football.',
                         '',
                         '',
                         '']

        chapters_tool_t = chapters_tool()
        fragments = chapters_tool_t.get_chapters_position(content)
        self.assertEqual((lines_correct, fragments_correct), fragments)

    def test_get_fragments(self):
        lines = ['CHAPTER 1', 'My friends like go to school.', 'CHAPTER 2', 'My name is Tom.', 'I am 14', 'CHAPTER 3',
                 'My dog like playing football.']
        numbers_list = [0, 2, 5]
        fragments_correct = ['My friends like go to school.\n', 'My name is Tom.\nI am 14\n',
                             'My dog like playing football.\n']

        chapters_tool_t = chapters_tool()
        fragments = chapters_tool_t.get_fragments(numbers_list, lines)
        self.assertEqual(fragments, fragments_correct)

    def test_get_chapters_content(self):
        content = '\n\n\nChapter 1.\n\n\n' \
                  'My friends like go to school.\n' \
                  'I like walking around house.' \
                  '\n\n\nChapter 2.\n\n\n' \
                  'My name is Tom.\n' \
                  'I am 14' \
                  '\n\n\nChapter 3.\n\n\n' \
                  'My dog like playing football.' \
                  '\n\n\n'

        fragemnts_correct = ['\n\nMy friends like go to school.\nI like walking around house.\n\n\n',
                             '\n\nMy name is Tom.\nI am 14\n\n\n',
                             '\n\nMy dog like playing football.\n\n\n\n']

        chapters_tool_t = chapters_tool()
        fragments = chapters_tool_t.get_chapters_content(content)
        self.assertEqual(fragments, fragemnts_correct)

    def test_sort_and_order(self):
        correct_dict = [10, 22, 31, 43, 45, 76]
        input_dict = {5: 45, 6: 76, 4: 43, 3: 31, 2: 22, 1: 10, 87: 5}

        chapters_tool_t = chapters_tool()
        output_dict = chapters_tool_t.sort_and_order(input_dict)

        self.assertEqual(correct_dict, output_dict)

    def test_get_local_statistics(self):
        verbs_present = ['like', 'go', 'walking', 'is']
        verbs_past = ['was']
        adjs = ['pretty']
        characters = ['Tom']

        fragemnts = ['\n\nMy friends like go to school.\nI like walking around house.\n\n\n',
                     '\n\nMy name is Tom.\nI am 14\n\n\n',
                     '\n\nMy dog like playing football.\n\n\n\n']

        chapters_tool_t = chapters_tool()

        df = pd.DataFrame()
        df['WordsAmount'] = [12, 8, 6]
        df['CharsAmount'] = [59, 24, 30]
        df['SentencesAmount'] = [3, 2, 2]
        df['SentencesAvgChars'] = [18.33, 10.50, 14.00]
        df['SentencesAvgWords'] = [4.0, 3.5, 3.0]
        df['DialoguesAmount'] = [0, 0, 0]
        df['DialoguesLongAmount'] = [0, 0, 0]
        df['DialoguesShortAmount'] = [0, 0, 0]
        df['VerbsAmount'] = [4, 1, 1]
        df['VerbsPresentAmount'] = [4, 1, 1]
        df['VerbsPastAmount'] = [0, 0, 0]
        df['AdjectivesAmount'] = [0, 0, 0]
        df['Characters'] = [[], [], []]

        df_output = chapters_tool_t.get_local_statistics(fragemnts, verbs_present, verbs_past, adjs, characters)

        assert_frame_equal(df_output, df)

    def test_check_if_roman_numeral_true(self):
        chapters_tool_t = chapters_tool()
        is_roman = chapters_tool_t.check_if_roman_numeral('VII')
        self.assertEqual(is_roman, True)

    def test_check_if_roman_numeral_false(self):
        chapters_tool_t = chapters_tool()
        is_roman = chapters_tool_t.check_if_roman_numeral('V123II')
        self.assertEqual(is_roman, False)

    def test_decimal_to_roman_V(self):
        chapters_tool_t = chapters_tool()
        decimal_number = chapters_tool_t.decimal_to_roman('V')
        self.assertEqual(decimal_number, 5)

    def test_decimal_to_roman_X(self):
        chapters_tool_t = chapters_tool()
        decimal_number = chapters_tool_t.decimal_to_roman('X')
        self.assertEqual(decimal_number, 10)

    def test_decimal_to_roman_L(self):
        chapters_tool_t = chapters_tool()
        decimal_number = chapters_tool_t.decimal_to_roman('L')
        self.assertEqual(decimal_number, 50)

    def test_decimal_to_roman_C(self):
        chapters_tool_t = chapters_tool()
        decimal_number = chapters_tool_t.decimal_to_roman('C')
        self.assertEqual(decimal_number, 100)

    def test_decimal_to_roman_D(self):
        chapters_tool_t = chapters_tool()
        decimal_number = chapters_tool_t.decimal_to_roman('D')
        self.assertEqual(decimal_number, 500)

    def test_decimal_to_roman_M(self):
        chapters_tool_t = chapters_tool()
        decimal_number = chapters_tool_t.decimal_to_roman('M')
        self.assertEqual(decimal_number, 1000)

    def test_decimal_to_roman_str(self):
        chapters_tool_t = chapters_tool()
        roman_number = chapters_tool_t.decimal_to_roman_str('III')
        self.assertEqual(roman_number, 3)

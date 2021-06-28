import unittest

from book_tools.dialogue_tool import dialogue_tool


class test_dialogue_tool(unittest.TestCase):

    def test_get_dialogues_aps_type(self):
        str_test = '“I see pretty and old cat in school” - said Adam. “Ok nice” - answered Sam.'
        dialogue_tool_t = dialogue_tool()
        dialogues = dialogue_tool_t.get_dialogues(str_test)
        dialogues_expected = ["“I see pretty and old cat in school” ", "“Ok nice” "]
        self.assertEqual(dialogues, dialogues_expected)

    def test_get_dialogues_normal_type(self):
        str_test = '"I see pretty and old cat in school" - said Adam. "Ok nice" - answered Sam.'
        dialogue_tool_t = dialogue_tool()
        dialogues = dialogue_tool_t.get_dialogues(str_test)
        dialogues_expected = ["I see pretty and old cat in school ", "Ok nice "]
        self.assertEqual(dialogues, dialogues_expected)

    def test_dialogue_average_words(self):
        dialogues_expected = ["I see pretty and old cat in school", "Ok nice"]
        dialogue_tool_t = dialogue_tool()
        dial_average_words = dialogue_tool_t.dialogue_average_words(dialogues_expected, len(dialogues_expected))

        self.assertEqual(dial_average_words, 5.0)

    def test_dialogue_average_chars(self):
        dialogues_expected = ["I see pretty and old cat in school", "Ok nice"]
        dialogue_tool_t = dialogue_tool()
        dial_average_words = dialogue_tool_t.dialogue_average_chars(dialogues_expected, len(dialogues_expected))

        self.assertEqual(dial_average_words, 20.5)

    def test_dialogues_long_amount(self):
        dialogues_expected = ["I see pretty and old cat in school", "Ok nice"]
        dialogue_tool_t = dialogue_tool()
        dial_average_words = dialogue_tool_t.dialogue_average_words(dialogues_expected, len(dialogues_expected))
        dial_long_amount = dialogue_tool_t.dialogues_long_amount(dialogues_expected, dial_average_words)

        self.assertEqual(dial_long_amount, 1)

    def test_dialogues_short_amount(self):
        dialogues_expected = ["I see pretty and old cat in school", "Ok nice"]
        dialogue_tool_t = dialogue_tool()
        dial_average_words = dialogue_tool_t.dialogue_average_words(dialogues_expected, len(dialogues_expected))
        dial_long_amount = dialogue_tool_t.dialogues_short_amount(dialogues_expected, dial_average_words)

        self.assertEqual(dial_long_amount, 1)

    def test_dialogues_long_percent(self):
        dialogues_expected = ["I see pretty and old cat in school", "Ok nice"]
        dialogue_tool_t = dialogue_tool()
        dial_average_words = dialogue_tool_t.dialogue_average_words(dialogues_expected, len(dialogues_expected))
        dial_long_amount = dialogue_tool_t.dialogues_long_amount(dialogues_expected, dial_average_words)
        dial_long_percent = dialogue_tool_t.dialogues_long_percent(dial_long_amount, dialogues_expected)

        self.assertEqual(dial_long_percent, 50)

    def test_dialogues_short_percent(self):
        dialogues_expected = ["I see pretty and old cat in school", "Ok nice"]
        dialogue_tool_t = dialogue_tool()
        dial_average_words = dialogue_tool_t.dialogue_average_words(dialogues_expected, len(dialogues_expected))
        dial_short_amount = dialogue_tool_t.dialogues_short_amount(dialogues_expected, dial_average_words)
        dial_short_percent = dialogue_tool_t.dialogues_long_percent(dial_short_amount, dialogues_expected)

        self.assertEqual(dial_short_percent, 50)

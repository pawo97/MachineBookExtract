import re


class basic_statistics_tool:

    def __init__(self, content):
        """Init basic statistics"""
        work_content = content.replace('\n', ' ')
        sentences = re.split('[.!?]', work_content)
        self.sentences = self.get_correct_sentences(sentences)

    def get_sentences(self):
        """Get sentences from book"""
        return self.sentences

    def get_correct_sentences(self, sentences):
        """Get correct in sentences in book"""
        sentences_correct = []
        for w in sentences:
            if "Illustration" not in w and "CHAPTER" not in w and "BOOK" not in w:
                if w != '':
                    sentences_correct.append(w.strip())

        return sentences_correct

    def get_average_chars_of_sentence(self, content=None):
        """Get average of char in sentences in book"""
        sentences_rate = []
        for w in self.sentences:
            sentences_rate.append(len(w))

        average = sum(sentences_rate) / len(self.sentences)
        return average

    def get_average_words_in_sentence(self):
        """Get average of word in sentences in book"""
        sentences_rate = []
        for w in self.sentences:
            words = w.split(' ')
            sentences_rate.append(len(words))

        average = sum(sentences_rate) / len(self.sentences)
        return average

    def get_book_length_chars(self, content):
        """Get amount of char in book"""
        work_content = content.replace('\n', ' ')
        return len(work_content)

    def get_book_length_words(self, content):
        """Get amount of words in book"""
        words = content.split(' ')
        return len(words)

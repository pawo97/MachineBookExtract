import re


class basic_statistics_tool:

    def __init__(self):
        pass

    def get_sentences(self, work_content):
        """Get sentences from book"""
        sentences = re.split('[.!?]', work_content)
        sentences_correct = self.get_correct_sentences(sentences)
        return sentences_correct

    def get_correct_sentences(self, sentences):
        """Get correct in sentences in book"""
        sentences_correct = []
        for w in sentences:
            if "Illustration" not in w and "CHAPTER" not in w and "BOOK" not in w:
                if w != '':
                    sentences_correct.append(w.strip())

        return sentences_correct

    def get_average_chars_of_sentence(self, sentences):
        """Get average of char in sentences in book"""
        sentences_rate = []
        for w in sentences:
            sentences_rate.append(len(w))

        average = sum(sentences_rate) / len(sentences)
        return average

    def get_average_words_in_sentence(self, sentences):
        """Get average of word in sentences in book"""
        sentences_rate = []
        for w in sentences:
            words = w.split(' ')
            sentences_rate.append(len(words))

        average = sum(sentences_rate) / len(sentences)
        return average

    def get_book_length_chars(self, content):
        """Get amount of char in book"""
        work_content = content.replace('\n', ' ')
        return len(work_content)

    def get_book_words(self, content):
        """Get amount of words in book"""
        words = content.split(' ')
        return words

    def clean_text(self, content):
        content_to_clean = content.split('\n')
        clean_text_value = ''
        for l in content_to_clean:
            line = l.strip().replace('*', '').replace('_', ' ').replace(']', '').replace('[', '').replace('--', ' ')
            if line.lower() != '' and 'illustration' not in line.lower() and 'http://' not in line.lower():
                clean_text_value += line + str(' ')

        return clean_text_value

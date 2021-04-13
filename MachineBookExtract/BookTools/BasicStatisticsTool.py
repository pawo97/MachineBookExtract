import re
class BasicStatisticsTool():
    def getAvergeLengthOfSentenceInBook(self, content):
        workContent = content.replace('\n', ' ')
        sentences = re.split('[.!?]', workContent)
        sentencesCorrect = []
        for w in sentences:
            if "Illustration" not in w and "CHAPTER" not in w and "BOOK" not in w:
                sentencesCorrect.append(w)
        totalSum = len(workContent)
        sentencesRate = []
        for w in sentencesCorrect:
            sentencesRate.append(w.__len__())

        averge = sum(sentencesRate) / len(sentences)
        print("Averge of sentence in book: ", averge, " chars")
        return averge

    def getAvergeWordInSentenceInBook(self, content):
        workContent = content.replace('\n', ' ')
        sentences = re.split('[.!?]', workContent)
        sentencesCorrect = []
        for w in sentences:
            if "Illustration" not in w and "CHAPTER" not in w and "BOOK" not in w:
                sentencesCorrect.append(w)
        totalSum = len(workContent)
        sentencesRate = []
        for w in sentencesCorrect:
            words = w.split(' ')
            sentencesRate.append(words.__len__())

        averge = sum(sentencesRate) / len(sentences)
        print("Averge of words in sentence in book: ", averge, " chars")
        return averge

    def getBookLength(self, content):
        workContent = content.replace('\n', ' ')
        print("Book length: ", workContent.__len__(), " chars")
        return workContent.__len__()

    def getAmountOfWords(self, content):
        words = content.split(' ')
        print("Words in book: ", words.__len__())
        return words.__len__()
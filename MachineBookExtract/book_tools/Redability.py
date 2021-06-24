import math
class Readability():
    def __init__(self):
        pass

    def getSylabes(self, doc):
        totalSylabesSum = 0
        for token in doc:
            if token._.syllables_count != None:
                totalSylabesSum += token._.syllables_count
        return totalSylabesSum

    def getPoliSylabes(self, doc):
        totalSylabesSum = 0
        for token in doc:
            if token._.syllables_count != None:
                if token._.syllables_count >= 3:
                    totalSylabesSum += token._.syllables_count
        return totalSylabesSum

    def getPoliSylabesNotNoun(self, doc):
        totalSylabesSum = 0
        for token in doc:
            if token._.syllables_count != None:
                if token._.syllables_count >= 3 and token.tag_[0] != 'N':
                    totalSylabesSum += token._.syllables_count
        return totalSylabesSum

    def getMcLaughlinFRERedability(self, doc, words, sentences):
        # y - liczna sylab
        # w - liczba słów
        # s - liczba zdań
        # 1 - 100, 30 - universitiy, 80 - school
        y = self.getSylabes(doc)
        r = 206.835 - 84.6 * (y / words) - 1.015 * words / sentences
        if r >= 100:
            r = 100
        return r

    def getMcLaughlinSMOGRedability(self, doc, sentences):
        # p - > 3 sylab
        # w - liczba słów
        # s - liczba zdań
        # r - lata w szkole zeby przeczytac ta ksiazke
        pS = self.getPoliSylabes(doc)

        r = 1.043 * math.sqrt((pS / sentences)) + 3.1291

        return r

    def getMcLaughlinFOGRedability(self, doc, words, sentences):
        # p - > 3 sylab
        # w - liczba słów
        # s - liczba zdań
        # r - lata w szkole zeby przeczytac ta ksiazke
        # według tabelki fog miał wyższe za każym razem (koło 8-9)
        pSN = self.getPoliSylabesNotNoun(doc)
        r = 0.4 * (words / sentences + 100 * pSN / words)
        return r
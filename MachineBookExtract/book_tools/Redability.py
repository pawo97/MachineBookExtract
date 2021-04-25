import math
class Readability():
    def __init__(self, doc, basicStatistics, content):
        self.content = content
        self.basicStatistics = basicStatistics
        self.doc = doc
        self.w = self.basicStatistics.getAmountOfWords(self.content)
        self.s = len(self.basicStatistics.getSentences())
        self.y = self.getSylabes()
        self.pS = self.getPoliSylabes()
        self.pSN = self.getPoliSylabesNotNoun()


    def getSylabes(self):
        totalSylabesSum = 0
        for token in self.doc:
            if token._.syllables_count != None:
                totalSylabesSum += token._.syllables_count
        return totalSylabesSum

    def getPoliSylabes(self):
        totalSylabesSum = 0
        for token in self.doc:
            if token._.syllables_count != None:
                if token._.syllables_count >= 3:
                    totalSylabesSum += token._.syllables_count
        return totalSylabesSum

    def getPoliSylabesNotNoun(self):
        totalSylabesSum = 0
        for token in self.doc:
            if token._.syllables_count != None:
                if token._.syllables_count >= 3 and token.tag_[0] != 'N':
                    totalSylabesSum += token._.syllables_count
        return totalSylabesSum

    def getMcLaughlinFRERedability(self):
        # y - liczna sylab
        # w - liczba słów
        # s - liczba zdań
        # 1 - 100, 30 - universitiy, 80 - school
        r = 206.835 - 84.6 * (self.y / self.w) - 1.015 * self.w / self.s
        return r

    def getMcLaughlinSMOGRedability(self):
        # p - > 3 sylab
        # w - liczba słów
        # s - liczba zdań
        # r - lata w szkole zeby przeczytac ta ksiazke
        w = self.basicStatistics.getAmountOfWords(self.content)
        s = len(self.basicStatistics.getSentences())
        pS = self.getPoliSylabes()

        r = 1.043 * math.sqrt((self.pS / self.s)) + 3.1291

        return r

    def getMcLaughlinFOGRedability(self):
        # p - > 3 sylab
        # w - liczba słów
        # s - liczba zdań
        # r - lata w szkole zeby przeczytac ta ksiazke
        # według tabelki fog miał wyższe za każym razem (koło 8-9)
        r = 0.4 * (self.w / self.s + 100 * self.pSN / self.w)
        return r
class TimeStatistics():
    def getVerbsNowAmount(self, doc):
        verbsPresent = []
        for token in doc:
            if token.tag_ == 'VB':
                verbsPresent.append(token.text)

        return len(verbsPresent)

    def getVerbsPastAmount(self, doc):
        verbsPast = []
        for token in doc:
            if token.tag_ == 'VBD':
                verbsPast.append(token.text)

        return len(verbsPast)

    def getVerbsTotal(self, doc):
        return self.getVerbsNowAmount(doc) + self.getVerbsPastAmount(doc)

    def getVerbsNowPercent(self, doc):
        present = self.getVerbsNowAmount(doc)
        past = self.getVerbsPastAmount(doc)
        total = present + past
        percentVerbsPresent = (present * 100) / total
        return percentVerbsPresent

    def getVerbsPastPercent(self, doc):
        present = self.getVerbsNowAmount(doc)
        past = self.getVerbsPastAmount(doc)
        total = present + past
        pastVerbsPresent = (past * 100) / total
        return pastVerbsPresent

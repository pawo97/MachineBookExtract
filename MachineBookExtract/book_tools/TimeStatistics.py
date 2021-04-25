class TimeStatistics():
    def getVerbsNowAmount(self, doc):
        verbsPresent = []
        for token in doc:
            if token.tag_ == 'VB':
                verbsPresent.append(token.text)

        return verbsPresent

    def getVerbsPastAmount(self, doc):
        verbsPast = []
        for token in doc:
            if token.tag_ == 'VBD':
                verbsPast.append(token.text)

        return verbsPast

    def getVerbsTotal(self, doc):
        return len(self.getVerbsNowAmount(doc)) + len(self.getVerbsPastAmount(doc))

    def getVerbsNowPercent(self, doc):
        present = len(self.getVerbsNowAmount(doc))
        past = len(self.getVerbsPastAmount(doc))
        total = present + past
        percentVerbsPresent = (present * 100) / total
        return percentVerbsPresent

    def getVerbsPastPercent(self, doc):
        present = len(self.getVerbsNowAmount(doc))
        past = len(self.getVerbsPastAmount(doc))
        total = present + past
        pastVerbsPresent = (past * 100) / total
        return pastVerbsPresent

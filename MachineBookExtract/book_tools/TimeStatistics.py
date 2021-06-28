class TimeStatistics():
    def getVerbsPresentAmount(self, doc):
        verbsPresent = []
        for token in doc:
            if token.tag_ == 'VB' or token.tag_ == 'VBP' or token.tag_ == 'VBZ':
                verbsPresent.append(token.text)

        return verbsPresent

    def getVerbsPastAmount(self, doc):
        verbsPast = []
        for token in doc:
            if token.tag_ == 'VBD' or token.tag_ == 'VBN':
                verbsPast.append(token.text)

        return verbsPast

    def getVerbsTotal(self, doc):
        return len(self.getVerbsPresentAmount(doc)) + len(self.getVerbsPastAmount(doc))

    def getVerbsNowPercent(self, present, past):
        total = present + past
        percentVerbsPresent = (present * 100) / total
        return percentVerbsPresent

    def getVerbsPastPercent(self, present, past):
        total = present + past
        pastVerbsPresent = (past * 100) / total
        return pastVerbsPresent

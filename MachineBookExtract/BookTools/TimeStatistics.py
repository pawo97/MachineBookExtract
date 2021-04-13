class TimeStatistics():
    def getVerbsNow(self, content, nlp):
        print("Counting verbs")
        words = content.split(' ')
        pastVerbsSize = 0
        presentVerbsSize = 0
        for w in words:
            doc = nlp(w)
            if len(doc) > 0 and 'VBD' == doc[0].tag_:
                pastVerbsSize += 1
            if len(doc) > 0 and 'VB' == doc[0].tag_:
                presentVerbsSize += 1

        total = presentVerbsSize + pastVerbsSize
        percentVerbsPresent = (presentVerbsSize * 100) / total
        percentVerbsPast = (pastVerbsSize * 100) / total

        print("Total verbs: " + str(total))
        print("Present: " + str(presentVerbsSize) + ' ' + str(percentVerbsPresent) + " %")
        print("Past: " + str(pastVerbsSize) + ' ' + str(percentVerbsPast) + " %")
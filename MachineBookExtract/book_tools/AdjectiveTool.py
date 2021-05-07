class AdjectiveTool():
    def __init__(self, doc):
        self.doc = doc

    def getAmountOfAdjectivesTotal(self):
        adj = []
        for token in self.doc:
            if token.pos_ == 'ADJ':
                adj.append(token.text)

        return len(adj)

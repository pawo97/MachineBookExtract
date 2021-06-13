class adjective_tool:
    def __init__(self, doc):
        """Init basic statistics"""
        self.doc = doc

    def get_amount_of_adjectives(self):
        """Get amount of adjectives in book"""
        adj = []
        for token in self.doc:
            if token.pos_ == 'ADJ':
                adj.append(token.text)

        return len(adj)

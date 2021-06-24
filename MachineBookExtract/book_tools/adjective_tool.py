class adjective_tool:
    def __init__(self):
        pass

    def get_amount_of_adjectives(self, doc):
        """Get amount of adjectives in book"""
        adj = []
        for token in doc:
            if token.pos_ == 'ADJ':
                adj.append(token.text)

        return len(adj)

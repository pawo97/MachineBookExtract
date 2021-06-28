class time_statistics_tool:

    def get_present_verbs(self, doc):
        """Get list of present verbs in text"""
        present_verbs = []
        for token in doc:
            if token.tag_ == 'VB' or token.tag_ == 'VBP' or token.tag_ == 'VBZ':
                present_verbs.append(token.text)

        return present_verbs

    def get_past_verbs(self, doc):
        """Get list of past verbs in text"""
        past_verbs = []
        for token in doc:
            if token.tag_ == 'VBD' or token.tag_ == 'VBN':
                past_verbs.append(token.text)

        return past_verbs

    def get_total_verbs(self, doc):
        """Get total verbs in text"""
        return len(self.get_present_verbs(doc)) + len(self.get_past_verbs(doc))

    def get_present_verbs_percent(self, present, past):
        """Get present verbs percentage in text"""
        total = present + past
        if total != 0:
            present_verbs_percent = (present * 100) / total
        else:
            present_verbs_percent = 0
        return present_verbs_percent

    def get_past_verbs_percent(self, present, past):
        """Get past verbs percentage in text"""
        total = present + past
        if total != 0:
            past_verbs_percent = (past * 100) / total
        else:
            past_verbs_percent = 0
        return past_verbs_percent

import math


class readability_tool:

    def __init__(self):
        pass

    def get_syllables(self, doc):
        """Amount of syllables in text"""
        syllables_sum = 0
        for token in doc:
            if token._.syllables_count != None:
                syllables_sum += token._.syllables_count
        return syllables_sum

    def get_poli_syllables(self, doc):
        """Amount of poli syllables in text"""
        syllables_sum = 0
        for token in doc:
            if token._.syllables_count != None:
                if token._.syllables_count >= 3:
                    syllables_sum += token._.syllables_count
        return syllables_sum

    def get_poli_syllables_not_noun(self, doc):
        """Amount of poli syllables not noun in text"""
        syllables_sum = 0
        for token in doc:
            if token._.syllables_count != None:
                if token._.syllables_count >= 3 and token.tag_[0] != 'N':
                    syllables_sum += token._.syllables_count
        return syllables_sum

    def get_McL_FRE_readability(self, doc, words, sentences):
        """Mclaughlin FRE factor"""
        # y - amount of syllables
        # w - amount of words
        # s - amount of sentences
        # 1 - 100, 30 - university, 80 - school
        try:
            y = self.get_syllables(doc)
            r = 206.835 - 84.6 * (y / words) - 1.015 * words / sentences
            if r >= 100:
                r = 100
        except Exception as e:
            r = 0
        return round(r, 2)

    def get_McL_SMOG_readability(self, doc, sentences):
        """Mclaughlin SMOG factor"""
        # p - > 3 syllables
        # w - amount of words
        # s - amount of sentences
        # r - years in school to read book
        pS = self.get_poli_syllables(doc)
        try:
            r = 1.043 * math.sqrt((pS / sentences)) + 3.1291
        except Exception as e:
            r = 0
        return round(r, 2)

    def get_McL_FOG_readability(self, doc, words, sentences):
        """Mclaughlin FOG factor"""
        # p - > 3 syllables
        # w - amount of words
        # s - amount of sentences
        # r - years in school to read book
        # 2 times more
        pSN = self.get_poli_syllables_not_noun(doc)
        try:
            r = 0.4 * (words / sentences + 100 * pSN / words)
        except Exception as e:
            r = 0
        return round(r, 2)
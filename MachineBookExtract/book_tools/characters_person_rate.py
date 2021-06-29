class characters_person_rate:
    def __init__(self):
        self.rate = 0
        self.word = ''
        self.tag = ''

    def __str__(self):
        return str(self.word) + " : " + str(self.rate)
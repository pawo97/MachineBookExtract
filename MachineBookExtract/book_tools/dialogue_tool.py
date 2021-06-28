class dialogue_tool:
    def __init__(self):
        pass

    def get_dialogues(self, content):
        """Dialogues list"""
        dialogue = 0
        content = content.replace('\n', ' ')
        words = content.split(' ')
        start = False
        first_type = True
        dialogues = []
        pom = ''
        for w in words:
            if '“' in w:
                start = True
            if start:
                pom += w + ' '
            if '”' in w:
                start = False
                dialogues.append(pom)
                pom = ''
                dialogue += 1

        if dialogue < 20:
            first_type = False
            for w in words:
                if w.startswith('"') and w.endswith('"'):
                    dialogues.append(w)
                    continue
                if '"' in w:
                    start = not start
                    if pom != '':
                        pom += w + ' '
                        dialogues.append(pom)
                        dialogue += 1
                        pom = ''
                if start:
                    pom += w + ' '
                    continue

        # Change dialogues
        if first_type:
            for i in range(len(dialogues)):
                dialogues[i] = dialogues[i].replace('“', '')
                dialogues[i] = dialogues[i].replace('”', '')
        else:
            for i in range(len(dialogues)):
                dialogues[i] = dialogues[i].replace('"', '')
        return dialogues

    def dialogue_average_words(self, dialogues, dial_amount):
        """Average of words in dialogues"""
        dial_sum = 0
        for i in range(len(dialogues)):
            words_inside = dialogues[i].split(' ')
            dial_sum += len(words_inside)
        dial_average_words = 0

        try:
            dial_average_words = dial_sum / dial_amount
        except:
            dial_average_words = 0

        return dial_average_words

    def dialogue_average_chars(self, dialogues, dialogue):
        """Average of chars in dialogues"""
        dial_sum = 0
        for i in range(len(dialogues)):
            for j in dialogues[i]:
                dial_sum += len(j)

        dial_average_chars = 0
        try:
            dial_average_chars = dial_sum / dialogue
        except:
            dial_average_chars = 0

        return dial_average_chars

    def dialogues_long_amount(self, dialogues, dial_average_value):
        """Amount of long dialogues"""
        dial_long = 0

        for i in range(len(dialogues)):
            words_inside = dialogues[i].split(' ')
            if len(words_inside) > dial_average_value:
                dial_long += 1

        return dial_long

    def dialogues_short_amount(self, dialogues, dial_average_value):
        """Amount of short dialogues"""
        dial_short = 0

        for i in range(len(dialogues)):
            words_inside = dialogues[i].split(' ')
            if len(words_inside) < dial_average_value:
                dial_short += 1

        return dial_short

    def dialogues_long_percent(self, dial_long, dialogues):
        """Amount of long dialogues percent"""
        dial_long_percent = 0
        try:
            dial_long_percent = (dial_long * 100) / len(dialogues)
        except:
            dial_long_percent = 0

        return dial_long_percent

    def dialogues_short_percent(self, dial_short, dialogues):
        """Amount of short dialogues percent"""
        dial_short_percent = 0
        try:
            dial_short_percent = (dial_short * 100) / len(dialogues)
        except:
            dial_short_percent = 0

        return dial_short_percent

class DialogueTool:
    def __init__(self):
        pass

    def getAmountOfDialogues(self, content):
        """Number of dialogues"""
        dialogue = 0
        content = content.replace('\n', ' ')
        words = content.split(' ')
        start = False
        firstType = True
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
            firstType = False
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
        if firstType:
            for i in range(len(dialogues)):
                dialogues[i] = dialogues[i].replace('“', '')
                dialogues[i] = dialogues[i].replace('”', '')
        else:
            for i in range(len(dialogues)):
                dialogues[i] = dialogues[i].replace('"', '')
        return dialogues

    def dialougeAvergeWords(self, dialogues, dialogue):
        """Number of words in dialogues"""
        dialougesCounterSum = 0
        for i in range(len(dialogues)):
            wordsDialog = dialogues[i].split(' ')
            dialougesCounterSum += len(wordsDialog)
        dialougesAvergeWords = 0
        try:
            dialougesAvergeWords = dialougesCounterSum / dialogue
        except:
            dialougesAvergeWords = 0
        return dialougesAvergeWords

    def dialougeAvergeChars(self, dialogues, dialogue):
        """Number of chars in dialogues"""
        dialougesCounterCharSum = 0
        for i in range(len(dialogues)):
            wordsDialog = dialogues[i].split(' ')
            for j in wordsDialog:
                dialougesCounterCharSum += len(j)

        dialougesAvergeChars = 0
        try:
            dialougesAvergeChars = dialougesCounterCharSum / dialogue
        except:
            dialougesAvergeChars = 0

        return dialougesAvergeChars

    def dialoguesLongAmount(self, dialogues, dialougesAvergeWords):
        longDialougeCount = 0

        for i in range(len(dialogues)):
            wordsDialog = dialogues[i].split(' ')
            if len(wordsDialog) > dialougesAvergeWords:
                longDialougeCount += 1

        return longDialougeCount

    def dialoguesShortAmount(self, dialogues, dialougesAvergeWords):
        shortDialougeCount = 0

        for i in range(len(dialogues)):
            wordsDialog = dialogues[i].split(' ')
            if len(wordsDialog) < dialougesAvergeWords:
                shortDialougeCount += 1

        return shortDialougeCount

    def dialoguesLongPercent(self, longDialougeCount, dialogues):
        percentLongDialogue = 0
        try:
            percentLongDialogue = (longDialougeCount * 100) / len(dialogues)
        except:
            percentLongDialogue = 0

        return percentLongDialogue

    def dialoguesShortPercent(self, shortDialougeCount, dialogues):
        percentShortDialogue = 0
        try:
            percentShortDialogue = (shortDialougeCount * 100) / len(dialogues)
        except:
            percentShortDialogue = 0

        return percentShortDialogue

class DialogueTool():
    def getAmountOfDialogues(self, content):
        dialouge = 0
        content = content.replace('\n', ' ')
        words = content.split(' ')
        start = False
        firstType = True
        dialoges = []
        pom = ''
        for w in words:
            if '“' in w:
                start = True
            if start:
                pom += w + ' '
            # print(w,' ', start)
            if '”' in w:
                start = False
                dialoges.append(pom)
                pom = ''
                dialouge += 1

        if dialouge < 20:
            firstType = False
            # print('new type')
            for w in words:
                if w.startswith('"') and w.endswith('"'):
                    dialoges.append(w)
                    continue
                if '"' in w:
                    start = not start
                    if pom != '':
                        pom += w + ' '
                        dialoges.append(pom)
                        dialouge += 1
                        pom = ''
                # print(w, start)
                if start:
                    pom += w + ' '
                    continue

        # for i in range(dialoges.__len__()):
        #         print(i,' ',dialoges[i])
        #         if i > 10:
        #                 break

        # Change dialoge
        if firstType:
            for i in range(dialoges.__len__()):
                dialoges[i] = dialoges[i].replace('“', '')
                dialoges[i] = dialoges[i].replace('”', '')
        else:
            for i in range(dialoges.__len__()):
                dialoges[i] = dialoges[i].replace('"', '')

        # Amount of words in dialoges (averge)
        dialougesCounterSum = 0
        for i in range(dialoges.__len__()):
            wordsDialog = dialoges[i].split(' ')
            dialougesCounterSum += len(wordsDialog)

        dialougesAvergeWords = dialougesCounterSum / dialouge
        print('Averge words in dialoge: ', dialougesAvergeWords)

        # Amount of chars in dialoges (averge)
        dialougesCounterCharSum = 0
        for i in range(dialoges.__len__()):
            wordsDialog = dialoges[i].split(' ')
            for j in wordsDialog:
                dialougesCounterCharSum += len(j)

        dialougesAvergeChars = dialougesCounterCharSum / dialouge
        print('Averge chars in dialoge: ', dialougesAvergeChars)

        longDialougeCount = 0
        shortDialougeCount = 0
        # Long dialouges amount and percent for words
        for i in range(dialoges.__len__()):
            wordsDialog = dialoges[i].split(' ')
            if len(wordsDialog) > dialougesAvergeWords:
                longDialougeCount += 1
            else:
                shortDialougeCount += 1

        percentShortDialogue = (shortDialougeCount * 100) / dialoges.__len__()
        percentLongDialogue = (longDialougeCount * 100) / dialoges.__len__()
        print('All dialogue: ', dialoges.__len__())
        print('Short dialogue:', shortDialougeCount, percentShortDialogue, '%')
        print('Long dialogue:', longDialougeCount, percentLongDialogue, '%')

        return dialouge
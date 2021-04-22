import pandas as pd

class DialogueTool():
    def __init__(self):
        pass

    def getAmountOfDialogues(self, content, type):
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
        return dialoges

    def dialougeAvergeWords(self, dialoges, dialouge):
        # Amount of words in dialoges (averge)
        dialougesCounterSum = 0
        for i in range(dialoges.__len__()):
            wordsDialog = dialoges[i].split(' ')
            dialougesCounterSum += len(wordsDialog)
        dialougesAvergeWords = 0
        try:
            dialougesAvergeWords = dialougesCounterSum / dialouge
        except:
            dialougesAvergeWords = 0
        return dialougesAvergeWords

    def dialougeAvergeChars(self, dialoges, dialouge):
        dialougesCounterCharSum = 0
        for i in range(dialoges.__len__()):
            wordsDialog = dialoges[i].split(' ')
            for j in wordsDialog:
                dialougesCounterCharSum += len(j)

        dialougesAvergeChars = 0
        try:
            dialougesAvergeChars = dialougesCounterCharSum / dialouge
        except:
            dialougesAvergeChars = 0

        return dialougesAvergeChars

    def dialogueLongShort(self, dialoges, dialougesAvergeWords):
        longDialougeCount = 0
        shortDialougeCount = 0
        # Long dialouges amount and percent for words
        for i in range(dialoges.__len__()):
            wordsDialog = dialoges[i].split(' ')
            if len(wordsDialog) > dialougesAvergeWords:
                longDialougeCount += 1
            else:
                shortDialougeCount += 1

        return longDialougeCount, shortDialougeCount

    def dialougeLongShortPercent(self, longDialougeCount, shortDialougeCount, dialoges):
        percentShortDialogue = 0
        percentLongDialogue = 0
        try:
            percentShortDialogue = (shortDialougeCount * 100) / dialoges.__len__()
            percentLongDialogue = (longDialougeCount * 100) / dialoges.__len__()
        except:
            percentShortDialogue = 0
            percentLongDialogue = 0

        return percentLongDialogue, percentShortDialogue


    # def rest(self):
    #     dialoges = []
    #     dialouge = 0
    #     dialougesAvergeWords = 0

        # # print('All dialogue: ', dialoges.__len__())
        # # print('Short dialogue:', shortDialougeCount, percentShortDialogue, '%')
        # # print('Long dialogue:', longDialougeCount, percentLongDialogue, '%')
        #
        # if type == 'LOCAL':
        #     # df = pd.DataFrame(columns=['Len', 'WA', 'CA', 'SDC', 'LDC', 'SDP', 'LDP'])
        #     d = {'Len': dialoges.__len__(), 'WA': "{:.0f}".format(dialougesAvergeWords), 'CA': "{:.0f}".format(dialougesAvergeChars),
        #                'SDC': "{:.0f}".format(shortDialougeCount), 'LDC': "{:.0f}".format(longDialougeCount), 'SDP': "{:.0f}".format(percentShortDialogue),
        #                'LDP': "{:.0f}".format(percentLongDialogue)}
        #     # df = pd.DataFrame(data=d)
        #     # print(df)
        #     return d
        #
        # else:
        #     print(dialoges.__len__(), "{:.0f}".format(dialougesAvergeWords), "{:.0f}".format(dialougesAvergeChars), "{:.0f}".format(shortDialougeCount), "{:.0f}".format(percentShortDialogue), '%', "{:.0f}".format(longDialougeCount), "{:.0f}".format(percentLongDialogue), '%')
        #
        # # return dialouge
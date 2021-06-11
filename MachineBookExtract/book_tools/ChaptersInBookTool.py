import collections
import re
import pandas as pd
# TO DO:
# podzial na watki
# podzielic na rozdzialy ksiazke string
from book_tools.BasicStatisticsTool import BasicStatisticsTool
from book_tools.DialogueTool import DialogueTool
from book_tools.TimeStatistics import TimeStatistics


class ChaptersInBookTool():

    def __init__(self, doc):
        self.doc = doc

    def getAmountOfChaptersByTableOfContent(self, content):
        # Check content first
        lines = content.split('\n')
        threeCount = 0

        chapters = 0
        liWords = []
        start = False
        for i in range(lines.__len__()):
            # print(lines[i])
            if 'CONTENTS' in lines[i] or 'Contents' in lines[i] or 'contents' in lines[i]:
                start = True
            if start:
                liWords.append(lines[i])
            if start and lines[i] == '':
                if lines[i + 1] == '':
                    break
        for i in liWords:
            i = i.lower()
            # print(i)
            if 'chapter' in i:
                chapters += 1

        print('Amount of chapter (Table of Content) ' + str(chapters))
        # Check in all text with space

        return chapters

    def getAmountOfChaptersByInsideOfContent(self, content):

        lines = content.split('\n')
        liChapters = []
        liChaptersCharPositions = []
        thisdictRomanAndDot = {}
        thisdictRoman = {}
        thisdictChapterNumberDot = {}
        thisdictChapterRomanDot = {}
        # counter = 0
        for i in range(lines.__len__()):
            # print("=====================")
            # print('L', lines[i])
            if i - 1 > 0:
                if lines[i - 1] == '':
                    if lines[i] == '':
                        continue
                    if 'THE END.' in lines[i]:
                        continue
                    # Remove table of contents
                    # print('B', lines[i])
                    if i + 1 < lines.__len__() and i + 2 < lines.__len__():
                        wordsNext = lines[i + 1].lstrip().split(' ')
                        wordsNextNext = lines[i + 2].lstrip().split(' ')
                        if 'chapter' in wordsNext[0].lower() or 'chapter' in wordsNextNext[0].lower():
                            continue
                    words = lines[i].lstrip().split(' ')
                    # print('F', lines[i])

                    # Check first word
                    # CHAPTER and NUMBER and .
                    firstword = words[0]
                    # if 'CHAPTER 30.' in lines[i]:
                    #     break
                    s = ''
                    # print(lines[i],'|',firstword)
                    if firstword.lower() == 'chapter':
                        # print(lines[i], '|', words[0], words[1])
                        s = re.sub(r'[^a-zA-Z0-9]', '', words[1])
                        if not self.checkIfRomanNumeral(s):
                            thisdictChapterNumberDot[int(s)] = i

                    # Check first word
                    # ROMAN NUMBER and .
                    s = ''
                    try:
                        s = re.sub(r'[^a-zA-Z0-9]', '', firstword)
                    except:
                        s = ''
                    lastwordot = ''
                    try:
                        lastwordot = s[-1]
                        # print(s)
                    except:
                        lastwordot = ''
                    if self.checkIfRomanNumeral(s):
                        # print(lines[i], '|', s)
                        if thisdictChapterRomanDot.get(self.romanToDecimal(s)) == None:
                            thisdictChapterRomanDot[int(self.romanToDecimal(s))] = i

                    # Check last word
                    # ROMAN NUMBER and .
                    lastwordot = ''
                    try:
                        lastwordot = words[words.__len__() - 1]
                    except:
                        lastwordot = ''
                    if lastwordot != '' and lastwordot[-1] == '.':
                        lastword = lastwordot[0:lastwordot.__len__() - 1]
                        if self.checkIfRomanNumeral(lastword):
                            if thisdictRomanAndDot.get(self.romanToDecimal(lastword)) == None:
                                # print(lines[i], '|', lastwordot)
                                thisdictRomanAndDot[self.romanToDecimal(lastword)] = i

                    # Check last word
                    # ROMAN NUMBER
                    lastwordot = ''
                    try:
                        lastwordot = words[words.__len__() - 1]
                    except:
                        lastwordot = ''
                    if lastwordot != '':

                        lastword = lastwordot
                        if self.checkIfRomanNumeral(lastword):
                            if thisdictRoman.get(self.romanToDecimal(lastword)) == None:
                                # print(lines[i], '|', lastwordot)
                                thisdictRoman[self.romanToDecimal(lastword)] = i



        # Create List of chapters and positions
        # Roman and .
        chaptersCountRomanAndDot = 0
        od = sorted(thisdictRomanAndDot.items())
        # print(od)
        count = 1
        liChaptersCharPositionsApprovedRomanAndDot = []
        for key in od:
            if key[0] == count:
                chaptersCountRomanAndDot += 1
                liChaptersCharPositionsApprovedRomanAndDot.append(key[1])
                count += 1
            else:
                break

        # Roman
        chaptersCountRoman = 0
        od = sorted(thisdictRoman.items())
        # print(od)
        count = 1
        liChaptersCharPositionsApprovedRoman = []
        for key in od:
            if key[0] == count:
                chaptersCountRoman += 1
                liChaptersCharPositionsApprovedRoman.append(key[1])
                count += 1
            else:
                break

        # Chapter Number Dot
        chaptersCountChapterNumberDot = 0
        od = sorted(thisdictChapterNumberDot.items())
        count = 1
        liChaptersCharPositionsApprovedChapterNumberDot = []
        for key in od:
            if key[0] == count:
                chaptersCountChapterNumberDot += 1
                liChaptersCharPositionsApprovedChapterNumberDot.append(key[1])
                count += 1
            else:
                break

        # Chapter Roman Dot
        chaptersCountChapterRomanDot = 0
        od = sorted(thisdictChapterRomanDot.items())
        count = 1
        liChaptersCharPositionsApprovedChapterRomanDot = []
        for key in od:
            if key[0] == count:
                chaptersCountChapterRomanDot += 1
                liChaptersCharPositionsApprovedChapterRomanDot.append(key[1])
                count += 1
            else:
                break

        # Check most apropriate
        liMax = []
        liMax.append(chaptersCountRomanAndDot)
        liMax.append(chaptersCountRoman)
        liMax.append(chaptersCountChapterNumberDot)
        liMax.append(chaptersCountChapterRomanDot)

        # print(liMax)
        liMax.sort()
        if liMax[-1] == chaptersCountRomanAndDot:
            chaptersCount = chaptersCountRomanAndDot
            liChaptersCharPositionsApproved = liChaptersCharPositionsApprovedRomanAndDot
        elif liMax[-1] == chaptersCountRoman:
            chaptersCount = chaptersCountRoman
            liChaptersCharPositionsApproved = liChaptersCharPositionsApprovedRoman
        elif liMax[-1] == chaptersCountChapterNumberDot:
            chaptersCount = chaptersCountChapterNumberDot
            liChaptersCharPositionsApproved = liChaptersCharPositionsApprovedChapterNumberDot
        elif liMax[-1] == chaptersCountChapterRomanDot:
            chaptersCount = chaptersCountChapterRomanDot
            liChaptersCharPositionsApproved = liChaptersCharPositionsApprovedChapterRomanDot

        self.lines = lines
        self.liChaptersCharPositionsApproved = liChaptersCharPositionsApproved
        return chaptersCount

        # print('Amount of chapters inside ' + str(chaptersCount))
        # print(liChaptersCharPositionsApproved.__len__())
        # print(liChaptersCharPositionsApproved)
        #
        # self.getFragmentsOfBook(lines, liChaptersCharPositionsApproved)

    def getFragmentsOfBook(self):
        p = self.liChaptersCharPositionsApproved
        lines = self.lines
        fragments = []
        j = 0
        chapter = ''
        for i in range(lines.__len__()):
            if i < p[j]:
                continue
            if i >= p[j]:
                if j + 1 < p.__len__() and i == p[j + 1]:
                    j += 1
                    fragments.append(chapter)
                    chapter = ''
                else:
                    chapter += lines[i]
                if i + 1 >= lines.__len__():
                    fragments.append(chapter)

        print('FRAGMENTS')
        for i in range(fragments.__len__()):
            print('CHAPTER ', i + 1)
            print(fragments[i])

        return fragments

        # df = self.getStatisticsDialogByChapter(fragments)
        # df = self.getStatisticsAdjectiveByChapter(fragments, self.doc, df)
        # df = self.getStatisticsTimeLineByChapter(fragments, self.doc, df)
        # self.getStatisticsLocationByChapter(fragments, self.doc, df)

    def getStatisticsDialogByChapter(self, fragments):
        d = DialogueTool()
        df = pd.DataFrame()
        dialogesLenLi = []
        dialogesAvergeWordsLi = []
        dialogesAvergeCharsLi = []
        longDialogueAmountLi = []
        shortDialogueAmountLi = []
        longDialoguePercentLi = []
        shortDialoguePercentLi = []

        for i in range(fragments.__len__()):
            dialoges = d.getAmountOfDialogues(fragments[i], 'LOCAL')
            dialogesAvergeWords = d.dialougeAvergeWords(dialoges, len(dialoges))
            dialogesAvergeChars = d.dialougeAvergeChars(dialoges, len(dialoges))
            longDialogueAmount, shortDialogueAmount = d.dialogueLongShort(dialoges, dialogesAvergeWords)
            longDialoguePercent, shortDialoguePercent = d.dialougeLongShortPercent(longDialogueAmount,
                                                                                                shortDialogueAmount,
                                                                                                dialoges)
            dialogesLenLi.append(len(dialoges))
            dialogesAvergeWordsLi.append(dialogesAvergeWords)
            dialogesAvergeCharsLi.append(dialogesAvergeChars)
            longDialogueAmountLi.append(longDialogueAmount)
            shortDialogueAmountLi.append(shortDialogueAmount)
            longDialoguePercentLi.append(longDialoguePercent)
            shortDialoguePercentLi.append(shortDialoguePercent)

        df['DialogesTotal'] = dialogesLenLi
        df['DialogesAvergeWords'] = dialogesAvergeWordsLi
        df['DialogesAvergeChars'] = dialogesAvergeCharsLi
        df['LongDialogueAmount'] = longDialogueAmountLi
        df['ShortDialogueAmount'] = shortDialogueAmountLi
        df['LongDialoguePercent'] = longDialoguePercentLi
        df['ShortDialoguePercent'] = shortDialoguePercentLi

        return df


    def getLengthWordCharsByChapter(self, fragments):
        df = pd.DataFrame()
        sentencesLenLi = []
        sentencesCharLenLi = []
        sentencesWordsLenLi = []
        fragmentsLengthCharLi = []
        fragmentsLengthWordLi = []

        for i in range(fragments.__len__()):
            b = BasicStatisticsTool(fragments[i])
            sentencesLenLi.append(len(b.getSentences()))
            sentencesCharLenLi.append(b.getAvergeLengthOfSentenceInBook(fragments[i]))
            sentencesWordsLenLi.append(b.getAvergeWordInSentenceInBook())
            fragmentsLengthCharLi.append(b.getBookLength(fragments[i]))
            fragmentsLengthWordLi.append(b.getAmountOfWords(fragments[i]))

        df['WordsTotal'] = fragmentsLengthWordLi
        df['CharTotal'] = fragmentsLengthCharLi
        df['SentencesWord'] = sentencesWordsLenLi
        df['SentencesChar'] = sentencesCharLenLi
        df['SentencesTotal'] = sentencesLenLi
        return df

    def getStatisticsAdjectiveByChapter(self, fragments, doc):
        df = pd.DataFrame()
        liWordsAmount = []
        liAdjAmount = []
        liAdjPercent = []
        adj = [token.lemma_ for token in doc if token.pos_ == "ADJ"]

        for i in range(fragments.__len__()):
            words = fragments[i].split(' ')
            wordsAmount = words.__len__()
            adjAmount = 0

            for w in words:
                if w in adj:
                    adjAmount += 1

            liWordsAmount.append(wordsAmount)
            liAdjAmount.append(adjAmount)
            liAdjPercent.append((adjAmount*100)/wordsAmount)
            # print(i, wordsAmount, adjAmount, (adjAmount*100)/wordsAmount)

        # df['WordsTotal'] = liWordsAmount
        df['AdjAmount'] = liAdjAmount
        df['AdjPercent'] = liAdjPercent

        return df

    def getTimeStatisticsByChapter(self, fragments, doc, li1, li2):
        df = pd.DataFrame()
        pastAmountLi = []
        presentAmountLi = []
        totalAmountLi = []
        pastPercentAmountLi = []
        presentPercentAmountLi = []

        t = TimeStatistics()

        for i in range(fragments.__len__()):
            words = fragments[i].split(' ')
            present = 0
            past = 0

            for w in words:
                if w in li1:
                    present += 1
                if w in li2:
                    past += 1

            pastAmountLi.append(past)
            presentAmountLi.append(present)
            totalAmountLi.append(past + present)
            if past and present != 0:
                pastPercentAmountLi.append((present * 100 / (past + present)))
                presentPercentAmountLi.append((past * 100 / (past + present)))

        df['PastTotal'] = pastAmountLi
        df['PresentTotal'] = presentAmountLi
        df['VerbsTotal'] = totalAmountLi
        df['PastPercent'] = pastPercentAmountLi
        df['PresentPercent'] = presentPercentAmountLi
        return df

    def getCharactersInChapters(self, fragments, characters):
        df = pd.DataFrame()
        liChaptersLevel = []
        for i in range(len(fragments)):
            liCharactersInside = []
            words = fragments[i].split(' ')
            for c in characters:
                if c in words:
                    if c in words:
                        s = 0
                        for w in words:
                            if c in w:
                                s += 1

                        st = (s * 100) / len(words)
                        liCharactersInside.append((c, st))
            liChaptersLevel.append(liCharactersInside)

        df['Heroes'] = liChaptersLevel
        return df



    # EXPERIMENT - AND VALUES
    def getStatisticsTimeLineByChapter(self, fragments, doc, df):

        # for ent in doc.ents:
        #     print("{} -> {}".format(ent.text, ent.label_))

        liDates = []
        for ent in filter(lambda e: e.label_ == 'DATE', doc.ents):
            liDates.append(ent.text)

        myDateList = list(dict.fromkeys(liDates))
        listTimes = []

        for i in range(fragments.__len__()):
            words = fragments[i].split(' ')
            fragmentTime = []
            for d in myDateList:
                if d in words:
                    fragmentTime.append(d)

            listTimes.append(fragmentTime)
            # print(fragmentTime)

        df['Times'] = listTimes
        return  df

    def getStatisticsLocationByChapter(self, fragments, doc, df):
        liLoc = []
        for ent in filter(lambda e: e.label_ == 'LOC' or e.label_ == 'NORP', doc.ents):
            liLoc.append(ent.text)

        myLocList = list(dict.fromkeys(liLoc))
        listLoc = []

        for i in range(fragments.__len__()):
            words = fragments[i].split(' ')
            fragmentLoc = []
            for d in myLocList:
                if d in words:
                    fragmentLoc.append(d)

            listLoc.append(fragmentLoc)
            # print(fragmentTime)

        df['Locations'] = listLoc
        df.to_excel("output.xlsx")



    def checkIfRomanNumeral(self, numeral):
            # numeral = numeral.upper()
            if numeral.isupper() == False:
                    valid = False
                    return valid
            validRomanNumerals = ["M", "D", "C", "L", "X", "V", "I", "(", ")"]
            valid = True
            for letters in numeral:
                    if letters not in validRomanNumerals:
                            # print("Sorry that is not a valid roman numeral")
                            valid = False
                            break
            return valid

    def value(self, r):
            if (r == 'I'):
                    return 1
            if (r == 'V'):
                    return 5
            if (r == 'X'):
                    return 10
            if (r == 'L'):
                    return 50
            if (r == 'C'):
                    return 100
            if (r == 'D'):
                    return 500
            if (r == 'M'):
                    return 1000
            return -1

    def romanToDecimal(self, str):
            res = 0
            i = 0

            while (i < len(str)):

                    # Getting value of symbol s[i]
                    s1 = self.value(str[i])

                    if (i + 1 < len(str)):
                            # Getting value of symbol s[i + 1]
                            s2 = self.value(str[i + 1])

                            # Comparing both values
                            if (s1 >= s2):
                                    # Value of current symbol is greater
                                    # or equal to the next symbol
                                    res = res + s1
                                    i = i + 1
                            else:
                                    # Value of current symbol is greater
                                    # or equal to the next symbol
                                    res = res + s2 - s1
                                    i = i + 2
                    else:
                            res = res + s1
                            i = i + 1
            return res

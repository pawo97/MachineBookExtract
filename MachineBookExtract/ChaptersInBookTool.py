import re

# TO DO:
# podzial na watki
# podzielic na rozdzialy ksiazke string

class ChaptersInBookTool():
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
        # linie i zaczyna sie tekst, konczy sie liczba rzymska albo cyfra obojetnie
        lines = content.split('\n')
        find = False
        CHAPTERS_COUNT = 3
        # check if last word has ROMAN NUMBER and .
        # on the end and then check if its roman number, order it and check if it is one for one
        liChapters = []
        for l in lines:
            if l == '':
                continue
            if 'THE END.' in l:
                continue
            words = l.split(' ')
            lastword = words[words.__len__() - 1]
            # lastword = lastword[0:lastword.__len__() - 1]

            try:
                lastwordot = lastword[-1]
            except:
                lastwordot = ''

            if lastwordot == '.':
                lastword = lastword[0:lastword.__len__() - 1]
                # print(l, lastwordot, words[words.__len__() - 1], lastword, self.checkIfRomanNumeral(lastword))
                if self.checkIfRomanNumeral(lastword):
                    liChapters.append(self.romanToDecimal(lastword))

        # print(liChapters)
        liChapters = sorted(liChapters)
        liChapters = list(dict.fromkeys(liChapters))
        second = False

        # print(liChapters)
        chaptersCount = 0
        for i in range(liChapters.__len__()):
            if i + 1 == liChapters[i]:
                chaptersCount += 1
            else:
                break

        if chaptersCount > CHAPTERS_COUNT:
            find = True

        if find == False:
            # check if last word has ROMAN NUMBER and .
            # on the end and then check if its roman number, order it and check if it is one for one
            liChapters = []
            for i in range(lines.__len__()):
                if i - 1 > 0 and i + 1 < lines.__len__():
                    if lines[i - 1] == '' and lines[i + 1] == '':
                        if lines[i] == '':
                            continue
                        if 'THE END.' in lines[i]:
                            continue
                        words = lines[i].split(' ')
                        lastword = words[words.__len__() - 1]
                        # lastword = lastword[0:lastword.__len__() - 1]

                        try:
                            lastwordot = lastword[-1]
                        except:
                            lastwordot = ''

                        # lastword = lastword[0:lastword.__len__() - 1]
                        # print(lastword)
                        if self.checkIfRomanNumeral(lastword):
                            liChapters.append(self.romanToDecimal(lastword))

            chaptersCount = 0
            for i in range(liChapters.__len__()):
                if i + 1 == liChapters[i]:
                    chaptersCount += 1
                else:
                    break

            if chaptersCount > CHAPTERS_COUNT:
                find = True

        if find == False:
            # check if start word has CHAPTER and NUMBER and .
            # on the end and then check if its roman number, order it and check if it is one for one
            liChapters = []
            for i in range(lines.__len__()):
                if i - 1 > 0:
                    if lines[i - 1] == '':
                        if lines[i] == '':
                            continue
                        if 'THE END.' in lines[i]:
                            continue
                        words = lines[i].split(' ')
                        firstword = words[0]

                        s = ''
                        if firstword.lower() == 'chapter':
                            s = re.sub(r'[^a-zA-Z0-9]', '', words[1])
                            # print(s)
                            liChapters.append(s)

                        # if self.checkIfRomanNumeral(lastword):
                        #         liChapters.append(self.romanToDecimal(lastword))

            chaptersCount = 0
            # print(liChapters)
            for i in range(liChapters.__len__()):
                if i + 1 == int(liChapters[i]):
                    chaptersCount += 1
                else:
                    break

            if chaptersCount > CHAPTERS_COUNT:
                find = True

        if find == False:
            # check if start word has ROMAN NUMBER and .
            # on the end and then check if its roman number, order it and check if it is one for one
            liChapters = []
            for i in range(lines.__len__()):
                if i - 1 > 0:
                    if lines[i - 1] == '':
                        if lines[i] == '':
                            continue
                        if 'THE END.' in lines[i]:
                            continue
                        words = lines[i].split(' ')
                        firstword = words[0]

                        s = ''
                        try:
                            s = re.sub(r'[^a-zA-Z0-9]', '', firstword)
                        except:
                            s = ''

                        # check dots
                        lastwordot = ''
                        try:
                            lastwordot = s[-1]
                            # print(s)
                        except:
                            lastwordot = ''

                        if self.checkIfRomanNumeral(s):
                            # print(s)
                            liChapters.append(self.romanToDecimal(s))

            chaptersCount = 0
            liChapters = sorted(liChapters)
            liChapters = list(dict.fromkeys(liChapters))
            # print(liChapters)
            for i in range(liChapters.__len__()):
                if i + 1 == int(liChapters[i]):
                    chaptersCount += 1
                else:
                    break

            if chaptersCount > CHAPTERS_COUNT:
                find = True

        print('Amount of chapters inside ' + str(chaptersCount))

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

from MachineBookExtract.book_tools.PersonRate import PersonRate


class TestBook:
    def __init__(self):
        pass

    def mainCharactersCheck(self, aliceInWonderlandCharacterList, b, nameOfTest):
        # aliceInWonderlandCharacterList = ["rabbit", "queen", "king", "cat", "duchess", "hatter", "hare", "dormouse",
        #                                   "gryphon"]
        aliceOfficialCharacters = []
        for person in aliceInWonderlandCharacterList:
            p = PersonRate()
            p.word = person
            aliceOfficialCharacters.append(p)

        totalCharacters = len(aliceInWonderlandCharacterList)
        totalFit = 0
        aliceCheckCharacters = b.getCharactersInBook()
        totalFitCharacters = len(aliceCheckCharacters)
        for i in aliceInWonderlandCharacterList:
            for j in aliceCheckCharacters:
                if i == j.word:
                    totalFit += 1

        print(nameOfTest)
        print("Total Main: " + str(totalCharacters))
        print("Total Fit: " + str(totalFitCharacters))
        print("Fit " + str(totalFit))
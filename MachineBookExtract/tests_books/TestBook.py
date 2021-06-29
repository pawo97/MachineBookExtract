from MachineBookExtract.book_tools.person_rate import person_rate
from book_tools_main.book_analyser_global import book_analyser_global
from book_tools_main.book_analyser_output import book_analyser_output


class characters_tool_test:
    def __init__(self):
        pass

    def mainCharactersCheck(self, aliceInWonderlandCharacterList, b, nameOfTest):
        # aliceInWonderlandCharacterList = ["rabbit", "queen", "king", "cat", "duchess", "hatter", "hare", "dormouse",
        #                                   "gryphon"]
        aliceOfficialCharacters = []
        for person in aliceInWonderlandCharacterList:
            p = person_rate()
            p.word = person
            aliceOfficialCharacters.append(p)

        totalCharacters = len(aliceInWonderlandCharacterList)
        totalFit = 0
        aliceCheckCharacters = b.get_characters()
        totalFitCharacters = len(aliceCheckCharacters)
        for i in aliceInWonderlandCharacterList:
            for j in aliceCheckCharacters:
                if i == j.word:
                    totalFit += 1

        print(nameOfTest)
        print("Total Main: " + str(totalCharacters))
        print("Total Fit: " + str(totalFitCharacters))
        print("Fit " + str(totalFit))

if __name__ == "__main__":

    # Method test Christmas Carol
    content = open(r'MachineBookExtract/books/A Christmas Carol by Charles Dickens.txt', encoding="utf8").read()
    book = book_analyser_global(content)
    print(book.old_content)
    # book.start()

    # book_output = book_analyser_output(book)
    # book_output.get_statistics_print()




        # analyzer = BookAnalyzer()
        # analyzer.start()
        # # analyzer.getAvergeOfSentenceInBook()
        # analyzer.getCharactersInBook()
        # analyzer.mainCharactersCheck()
        # # analyzer.printExecutionTime()

        #=======================================================================================

        # # Method test Alice
        # b = BookAnalyzer(r'books/Alices Adventures in Wonderland by Lewis Carroll')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["rabbit", "queen", "king", "cat", "duchess", "hatter", "hare", "dormouse", "gryphon"], b, 'Alice Test')

        # # Method test Christmas Carol
        # b = BookAnalyzer(r'books/A Christmas Carol by Charles Dickens.txt')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["scrooge", "marley", "cratchit", "ghost", "tim", "fred", "fezziwig", "marta"], b, 'Christmas Test')
        #
        # # Method test Drakula
        # b = BookAnalyzer(r'books/Dracula by Bram Stoker')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["lucy", "dracula", "harker", "lucy", "helsing", "renfield", "seward", "morris"], b,
        #                       'Dracula Test')
        #
        # Method test Moby
        # b = BookAnalyzer(r'books/Moby Dick; Or, The Whale_Herman Melville')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["ahab", "dick", "ishmael", "queequeg", "mapple", "sam", "boomer", "sturbuck", "stubb", "elijah"], b,
        #                       'Moby Test')

        #=========================================================================================

        #Method test Peter
        # b = BookAnalyzer(r'books/Peter Pan by J. M. Barrie')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["peter", "wendy", "hak", "darling", "lilia", "smee", "nibs", "rabbit", "bell"], b,
        #                       'Peter Test')
        #
        # Method test Sherlock
        # b = BookAnalyzer(r'books/The Adventures of Sherlock Holmes by Arthur Conan Doyle')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["holmes", "watson", "lestrade", "bohemia", "adler", "wilson", "sutherland", "mccarthy"], b,
        #                       'Sherlock Test')
        #
        # Method test Castle
        # b = BookAnalyzer(r'books/The Castle of Otranto by Horace Walpole')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["manfred", r"hippolita", "conrad", "matilda", r"isabella", "theodore", "jerome", "diego"], b,
        #                       'Castle Test')
        #
        # Method test Moonstone
        # b = BookAnalyzer(r'books/Metamorphosis by Franz Kafka')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["verinder", "blake", "ablewhite", "betteredge", "jennings", "cuff", "clack", "bruff", "candy"], b,
        #                       'Moonstone Test')
        #
        # # Method test Odyssey
        # b = BookAnalyzer(r'books/Pride and Prejudice by Jane Austen')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck([r"odysseus", r"apollo", r"penelope", r"agamemnon", r"queen", "zeus", r"neptune", "eurymachus", r"amphinomus"], b,
        #                       'Odyssey Test')
        #
        # # Method test Wuthering
        # b = book_analyser_global(r'MachineBookExtract/books/Wuthering Heights by Emily Bronte')
        # b.start()
        # b.getStatistics()
        # # t = TestBook()
        # # t.mainCharactersCheck(["heathcliff", "catherine", "linton", "dean", "lockwood", "earnshaw", "linton", "joseph"], b,
        # #                       'Wuthering Test')

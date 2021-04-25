from MachineBookExtract.Main import BookAnalyzer

if __name__ == "__main__":
        # analyzer = BookAnalyzer()
        # analyzer.start()
        # # analyzer.getAvergeOfSentenceInBook()
        # analyzer.getCharactersInBook()
        # analyzer.mainCharactersCheck()
        # # analyzer.printExecutionTime()

        #=======================================================================================

        # # Method test Alice
        # b = BookAnalyzer(r'Books/Alices Adventures in Wonderland by Lewis Carroll')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["rabbit", "queen", "king", "cat", "duchess", "hatter", "hare", "dormouse", "gryphon"], b, 'Alice Test')

        # # Method test Christmas Carol
        # b = BookAnalyzer(r'Books/A Christmas Carol by Charles Dickens')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["scrooge", "marley", "cratchit", "ghost", "tim", "fred", "fezziwig", "marta"], b, 'Christmas Test')
        #
        # # Method test Drakula
        # b = BookAnalyzer(r'Books/Dracula by Bram Stoker')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["lucy", "dracula", "harker", "lucy", "helsing", "renfield", "seward", "morris"], b,
        #                       'Dracula Test')
        #
        # Method test Moby
        # b = BookAnalyzer(r'Books/Moby Dick; Or, The Whale_Herman Melville')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["ahab", "dick", "ishmael", "queequeg", "mapple", "sam", "boomer", "sturbuck", "stubb", "elijah"], b,
        #                       'Moby Test')

        #=========================================================================================

        #Method test Peter
        # b = BookAnalyzer(r'Books/Peter Pan by J. M. Barrie')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["peter", "wendy", "hak", "darling", "lilia", "smee", "nibs", "rabbit", "bell"], b,
        #                       'Peter Test')
        #
        # Method test Sherlock
        # b = BookAnalyzer(r'Books/The Adventures of Sherlock Holmes by Arthur Conan Doyle')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["holmes", "watson", "lestrade", "bohemia", "adler", "wilson", "sutherland", "mccarthy"], b,
        #                       'Sherlock Test')
        #
        # Method test Castle
        # b = BookAnalyzer(r'Books/The Castle of Otranto by Horace Walpole')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["manfred", r"hippolita", "conrad", "matilda", r"isabella", "theodore", "jerome", "diego"], b,
        #                       'Castle Test')
        #
        # Method test Moonstone
        # b = BookAnalyzer(r'Books/Metamorphosis by Franz Kafka')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["verinder", "blake", "ablewhite", "betteredge", "jennings", "cuff", "clack", "bruff", "candy"], b,
        #                       'Moonstone Test')
        #
        # # Method test Odyssey
        # b = BookAnalyzer(r'Books/Pride and Prejudice by Jane Austen')
        # b.start()
        # b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck([r"odysseus", r"apollo", r"penelope", r"agamemnon", r"queen", "zeus", r"neptune", "eurymachus", r"amphinomus"], b,
        #                       'Odyssey Test')
        #
        # # Method test Wuthering
        b = BookAnalyzer(r'MachineBookExtract/Books/Wuthering Heights by Emily Bronte')
        b.start()
        b.getStatistics()
        # t = TestBook()
        # t.mainCharactersCheck(["heathcliff", "catherine", "linton", "dean", "lockwood", "earnshaw", "linton", "joseph"], b,
        #                       'Wuthering Test')



import traceback

from book_tools_main.book_analyser_global import book_analyser_global
from book_tools_main.book_analyser_output import book_analyser_output


class test_books_statistics:
    def __init__(self):
        pass

    def get_statistics(self, books):
        for i in range(len(books)):
            file = open(r'books/' + str(books[i]), encoding="utf8")
            content = file.read()
            file.close()
            book = book_analyser_global(content)
            book.start()

            try:
                book.start()
                b_o = book_analyser_output(book)
                print(books[i])
                b_o.get_statistics_print()
            except Exception as e:
                print('ERROR - ', str(books[i]))
                print(traceback.format_exc())


if __name__ == "__main__":
    print('LOCAL DEBUG')
    books = [
        'A Christmas Carol by Charles Dickens.txt',
        'Alices Adventures in Wonderland by Lewis Carroll.txt',
        'Dracula by Bram Stoker.txt',
        'Metamorphosis by Franz Kafka.txt',
        'Moby Dick; Or, The Whale_Herman Melville.txt',
        'Peter Pan by J. M. Barrie.txt',
        'Pride and Prejudice by Jane Austen.txt',
        'Romeo i Julia.txt',
        'shakespeare.txt',
        'test.txt',
        'The Adventures of Sherlock Holmes by Arthur Conan Doyle.txt',
        'The Castle of Otranto by Horace Walpole.txt',
        'Wuthering Heights by Emily Bronte.txt'
    ]

    books_single = ['test.txt']

    t_b_s = test_books_statistics()
    t_b_s.get_statistics(books)


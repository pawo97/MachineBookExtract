
from PyQt5.QtCore import QThread, pyqtSignal
from book_tools.BookAnalyzer import BookAnalyzer


class MyThread(QThread):
    changeValue = pyqtSignal(object)

    def __init__(self, content, parent=None):
        QThread.__init__(self, parent)
        self.content = content

    def run(self):
        try:
            b = BookAnalyzer(self.content)
            b.start()
            b.getStatisticsPrint()
            self.changeValue.emit(b)
        except Exception as e:
            print('Exception ' + str(e))
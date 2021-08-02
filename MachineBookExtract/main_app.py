import sys
import traceback

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox
# from PyQt5.QtChart import *
from book_tools_main.book_analyser_output import book_analyser_output
from gui.MyThread import MyThread
from gui.MyThreadProgress import MyThreadProgress
from gui.WindowChart import WindowChart


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.content = ''
        self.initUI()
        self.openedFile = False
        self.analyzedFile = False
        self.getChapterFile = False

        self.book = None
        self.book_output = None

    def initUI(self):
        # load UI
        uic.loadUi('gui/TestUI.ui', self)
        self.progressBar.setValue(0)

        # connect buttons
        self.pushButton.clicked.connect(self.openFileNameDialog)
        self.pushButton_2.clicked.connect(self.startAnalisye)
        self.pushButton_3.clicked.connect(self.getChaptersView)
        self.pushButton_8.clicked.connect(self.getPrev)
        self.pushButton_7.clicked.connect(self.getNext)
        self.pushButton_5.clicked.connect(self.showChartsTime)
        self.pushButton_9.clicked.connect(self.showChartsDialogue)
        self.pushButton_4.clicked.connect(self.saveOutput)
        self.pushButton_6.clicked.connect(self.exitProgram)

        # enable buttons
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_8.setEnabled(False)
        self.pushButton_7.setEnabled(False)

        self.show()

    # =====================================================================================================
    # CONTROL BUTTONS
    def startAnalisye(self):
        self.runTasks()

    def getChaptersView(self):
        self.currentVal = 0
        try:
            # get fragments
            if self.book.chap_inside:
                self.fragments = self.book.fragments
                self.amountChapters = self.book.chap_value
                self.df1 = self.book.fragments_s

                self.textEdit.setPlainText(self.fragments[self.currentVal])
                self.updateLabelsForLocalChapters()
                self.pushButton_8.setEnabled(True)
                self.pushButton_7.setEnabled(True)
            else:
                self.show_error('Chapters not founded')

        except Exception as e:
            print(traceback.format_exc())

    def getNext(self):
        if self.currentVal + 1 < len(self.fragments):
            self.currentVal += 1
            self.updateLabelsForLocalChapters()

    def getPrev(self):
        if self.currentVal - 1 >= 0:
            self.currentVal -= 1
            self.updateLabelsForLocalChapters()

    def updateLabelsForLocalChapters(self):
        # BASIC LOCAL STATISTICS
        self.textEdit.setPlainText(self.fragments[self.currentVal])
        self.label_39.setText('Chapter: ' + str(self.currentVal + 1))
        self.label_63.setText(str(self.df1.iat[self.currentVal, 0]))
        self.label_62.setText(str(self.df1.iat[self.currentVal, 1]))
        self.label_61.setText(str(self.df1.iat[self.currentVal, 2]))
        self.label_60.setText(str(self.df1.iat[self.currentVal, 3]))
        self.label_59.setText(str(self.df1.iat[self.currentVal, 4]))
        self.label_57.setText(str(self.df1.iat[self.currentVal, 5]))
        self.label_64.setText(str(self.df1.iat[self.currentVal, 6]))
        self.label_58.setText(str(self.df1.iat[self.currentVal, 7]))
        self.label_41.setText(str(self.df1.iat[self.currentVal, 8]))
        self.label_42.setText(str(self.df1.iat[self.currentVal, 9]))
        self.label_43.setText(str(self.df1.iat[self.currentVal, 10]))
        self.label_44.setText(str(self.df1.iat[self.currentVal, 11]))

        # Heroes
        self.listWidget_2.clear()
        li = self.df1.iat[self.currentVal, 12]
        liHeroes = []
        for i in self.df1.iat[self.currentVal, 12]:
            liHeroes.append(i)

        self.listWidget_2.addItems(liHeroes)

    def openFileNameDialog(self):
        status_ok = True
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Text files (*.txt)", options=options)


        if fileName:
            fileNameSplit = fileName.split('/')
            if len(fileNameSplit) >= 1:
                self.file_name = fileNameSplit[len(fileNameSplit) - 1]
                self.label_20.setText(self.file_name)

                try:
                    file = open(fileName, encoding="utf8")
                    self.content = file.read()
                    file.close()
                    if len(self.content) == 0:
                        raise Exception
                except Exception as e:
                    print(traceback.format_exc())
                    status_ok = False
                    self.show_error('File is empty')

        if status_ok:
            self.pushButton_2.setEnabled(True)

            # New file
            self.pushButton_3.setEnabled(False)
            self.pushButton_8.setEnabled(False)
            self.pushButton_7.setEnabled(False)

    def showChartsTime(self):
        # print('Charts')
        self.w = WindowChart(self.book.present_vb_p, self.book.past_vb_p, 'Tense Statistics', 'Present', 'Past')
        self.w.show()

    def showChartsDialogue(self):
        # print('Charts')
        self.w = WindowChart(self.book.dialogues_long_p, self.book.dialogues_short_p, 'Dialogue Statistics', 'Long', 'Short')
        self.w.show()

    def saveOutput(self):
        self.book_output.save_statistics_basic(self.file_name)
        self.book_output.save_statistics_local(self.file_name, self.df1)

    def exitProgram(self):
        sys.exit()
    # =================================================================================
    # Help functions
    # =================================================================================
    def runTasks(self):
        self.thread = MyThread(self.content)
        # print('Start analyze')
        self.progressBar.setValue(0)
        try:
            self.thread.changeValue.connect(self.updateLabels)
            self.thread.start()
        except Exception as e:
            print(traceback.format_exc())

        self.stopThread = False
        self.thread2 = MyThreadProgress(self.progressBar, self.stopThread)
        # print('Start counter')
        try:
            self.thread2.start()
        except Exception as e:
            print(traceback.format_exc())

    def updateLabels(self, label):
        self.book = label
        self.book_output = book_analyser_output(self.book)

        self.label_11.setText(str(self.book.book_words_amount))
        self.label_10.setText(str(self.book.book_chars_amount))
        self.label_8.setText(str(self.book.book_sentences_amount))
        self.label_9.setText(str(self.book.book_sentences_average_chars))
        self.label_22.setText(str(self.book.book_sentences_average_words))

        self.label_27.setText(str(self.book.fre))
        self.label_28.setText(str(self.book.smog))
        self.label_29.setText(str(self.book.fog))

        self.label_19.setText(str(self.book.total_vb))
        self.label_18.setText(str(self.book.present_vb))
        self.label_16.setText(str(self.book.past_vb))

        self.label_17.setText(str(self.book.dialogues_amount))
        self.label_33.setText(str(self.book.dialogues_average_words))
        self.label_34.setText(str(self.book.dialogues_average_chars))
        self.label_35.setText(str(self.book.dialogues_long_a))
        self.label_36.setText(str(self.book.dialogues_short_a))

        # Set adjectives
        self.label_37.setText("Amount of adjectives: " + str(self.book.total_adj))

        # Characters
        entries = self.book.characters
        self.listWidget.clear()
        self.listWidget.addItems(entries)

        # Stop progress bar
        self.progressBar.setValue(100)
        try:
            self.thread2.join()
        except Exception as e:
            # print(traceback.format_exc())
            pass
        self.pushButton_3.setEnabled(True)

    def show_error(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(text)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
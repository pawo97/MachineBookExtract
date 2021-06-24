import sys
import threading
import time
import traceback

from PyQt5 import uic
from PyQt5.QtChart import QPieSeries, QChartView, QChart
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QFileDialog, QMainWindow, QMessageBox
# from PyQt5.QtChart import *
from book_tools.BookAnalyzer import BookAnalyzer
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

    def initUI(self):
        # load UI
        uic.loadUi('TestUI.ui', self)
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
        # get fragments
        self.currentVal = 0
        self.amountChapters, self.fragments, self.df1 = self.b.getFragmentsAndChapters()
        # print(self.df1)
        try:
            self.textEdit.setPlainText(self.fragments[self.currentVal])
            self.updateLabelsForLocalChapters()
        except Exception as e:
            print(traceback.format_exc())

        self.pushButton_8.setEnabled(True)
        self.pushButton_7.setEnabled(True)

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
        self.label_61.setText(str(self.df1.iat[self.currentVal, 4]))
        self.label_60.setText(str(self.df1.iat[self.currentVal, 3]))
        self.label_59.setText(str(self.df1.iat[self.currentVal, 2]))
        self.label_57.setText(str(self.df1.iat[self.currentVal, 5]))
        self.label_64.setText(str(self.df1.iat[self.currentVal, 8]))
        self.label_58.setText(str(self.df1.iat[self.currentVal, 9]))
        self.label_41.setText(str(self.df1.iat[self.currentVal, 16]))
        self.label_42.setText(str(self.df1.iat[self.currentVal, 15]))
        self.label_43.setText(str(self.df1.iat[self.currentVal, 14]))
        self.label_44.setText(str(self.df1.iat[self.currentVal, 12]))

        # Heroes
        self.listWidget_2.clear()
        li = self.df1.iat[self.currentVal, 19]
        liHeroes = []
        for i in self.df1.iat[self.currentVal, 19]:
            liHeroes.append(i[0])

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
                    self.content = open(fileName, encoding="utf8").read()
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
        self.w = WindowChart(self.presentPercent, self.pastPercent, 'Time Statistics', 'Present', 'Past')
        self.w.show()

    def showChartsDialogue(self):
        # print('Charts')
        self.w = WindowChart(self.dlongPercent, self.dshortPercent, 'Dialogue Statistics', 'Long', 'Short')
        self.w.show()

    def saveOutput(self):
        self.b.getStatisticsOutput(self.file_name)

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
        self.b = label
        self.label_11.setText(str(self.b.book_chars_length))
        self.label_10.setText(str(self.b.book_words_length))
        self.label_8.setText(str(self.b.book_sentences_amount))
        self.label_9.setText(str(self.b.book_sentences_average_chars))
        self.label_22.setText(str(self.b.book_sentences_average_words))

        # fre, smog, fog = self.b.getFRESMOGFOGReadability()
        # self.label_27.setText(fre)
        # self.label_28.setText(smog)
        # self.label_29.setText(fog)
        #
        # # Set labels time and dialogues
        # total, present, past, self.presentPercent, self.pastPercent = self.b.getTotalVerbsStatisticsAmount()
        # self.label_19.setText(total)
        # self.label_18.setText(present)
        # self.label_16.setText(past)
        #
        # dialoges, dialogesAvergeWords, dialogesAvergeChars, longDialogueAmount, shortDialogueAmount, self.dlongPercent, self.dshortPercent = self.b.getDialogesAmounts()
        # self.label_17.setText(dialoges)
        # self.label_33.setText(dialogesAvergeWords)
        # self.label_34.setText(dialogesAvergeChars)
        # self.label_35.setText(longDialogueAmount)
        # self.label_36.setText(shortDialogueAmount)
        #
        # # Set adjectives
        # adj = self.b.getAdjectivesAmount()
        # self.label_37.setText("Amount of adjectives: " + adj)
        #
        # # Characters
        # entries = self.b.getCharactersList(self.b.content, self.b.doc, self.b.nlp)
        # self.listWidget.addItems(entries)
        #
        # # Stop progress bar
        # self.progressBar.setValue(100)
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
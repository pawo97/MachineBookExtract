
import asyncio
import sys
import threading
import time
from asyncio import coroutine

from PyQt5 import uic
from PyQt5.QtChart import QPieSeries, QPieSlice, QChartView, QChart
from PyQt5.QtCore import QRunnable, pyqtSlot, Qt, QThread, QObject, pyqtSignal, QThreadPool
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QPlainTextEdit, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QWidget, QLabel, \
    QLineEdit, QFileDialog, QListView, QListWidget, QGridLayout, QTableWidget, QTableWidgetItem, QMainWindow
from matplotlib.backends.backend_template import FigureCanvas
from qtpy import QtWidgets, QtCore
# from PyQt5.QtChart import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("Machine Book Extract")
#         self.resize(800,800)
#
#         okButton = QPushButton('OK')
#         cancelButton = QPushButton('Cancel')
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#         self.setLayout(vbox)
#         self.setGeometry(300, 300, 350, 150)
#         self.setWindowTitle('Box layout example, QHBoxLayout, QVBoxLayout')
#         self.show()
#
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     sys.exit(app.exec_())
from Main import BookAnalyzer
import matplotlib.pyplot as plt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.content = ''
        self.initUI()

    def initUI(self):
        print('hello')
        uic.loadUi('TestUI.ui', self)
        # set progress to zero
        self.progressBar.setValue(0)

        # connect buttons
        self.pushButton.clicked.connect(self.openFileNameDialog)
        self.pushButton_2.clicked.connect(self.startAnalisye)
        self.pushButton_3.clicked.connect(self.getCahptersView)
        self.pushButton_8.clicked.connect(self.getPrev)
        self.pushButton_7.clicked.connect(self.getNext)
        self.show()

        # self.initMyComponent()

    def initMyComponent(self):
        # create components
        analyze_button = QPushButton("Analyze")
        # charts_button = QPushButton("Charts")
        get_chapters_button = QPushButton("Get chapters")
        get_chapters_txt_button = QPushButton("Save txt")
        get_chapters_excel_button = QPushButton("Save excel")
        open_button = QPushButton("Open")
        exit_button = QPushButton("Exit")

        prev_button = QPushButton("Prev")
        next_button = QPushButton("Next")

        self.text_editor = QPlainTextEdit()
        self.text_editor.setReadOnly(True)
        self.text_editor.setPlainText('')
        self.text_editor.setFixedWidth(500)
        self.text_editor.setFixedHeight(500)

        label_1 = QLabel()
        label_1.setText('Menu: ')

        label_2 = QLabel()
        label_2.setText('Basic statistics: ')

        self.label_3 = QLabel()
        self.label_3.setText('Chapter: ')

        label_4 = QLabel()
        label_4.setText('Chapter statistics: ')

        label_5 = QLabel()
        label_5.setText('Opened Book: ')

        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setMaximumWidth(700)

        self.label_6 = QLabel()
        self.label_6_text = 'Amount of words: '
        self.label_6.setText(self.label_6_text)
        self.label_6_1 = QLabel()

        self.label_7 = QLabel()
        self.label_7_text = 'Amount of chars: '
        self.label_7.setText(self.label_7_text)
        self.label_7_1 = QLabel()

        self.label_8 = QLabel()
        self.label_8_text = 'Amount of sentences: '
        self.label_8.setText(self.label_8_text)
        self.label_8_1 = QLabel()

        self.label_9 = QLabel()
        self.label_9_text = 'Average amount of sentences (chars): '
        self.label_9.setText(self.label_9_text)
        self.label_9_1 = QLabel()

        self.label_10 = QLabel()
        self.label_10_text = 'Average amount of sentences (words): '
        self.label_10.setText(self.label_10_text)
        self.label_10_1 = QLabel()

        self.label_11 = QLabel()
        self.label_11_text = 'Analise book status: '
        self.label_11.setText(self.label_11_text)

        self.label_12 = QLabel()
        self.label_12_text = 'Amount of verbs: '
        self.label_12.setText(self.label_12_text)

        self.label_13 = QLabel()
        self.label_13_text = 'Amount of present verbs: '
        self.label_13.setText(self.label_13_text)

        self.label_14 = QLabel()
        self.label_14_text = 'Amount of past verbs: '
        self.label_14.setText(self.label_14_text)

        self.label_15 = QLabel()
        self.label_15_text = 'FRE value: '
        self.label_15.setText(self.label_15_text)

        self.label_16 = QLabel()
        self.label_16_text = 'SMOG value: '
        self.label_16.setText(self.label_16_text)

        self.label_17 = QLabel()
        self.label_17_text = 'FOG value: '
        self.label_17.setText(self.label_17_text)

        self.label_18 = QLabel()
        self.label_18_text = 'Amount of adjectives: '
        self.label_18.setText(self.label_18_text)

        self.label_19 = QLabel()
        self.label_19_text = 'Amount of dialogues: '
        self.label_19.setText(self.label_19_text)

        self.label_20 = QLabel()
        self.label_20_text = 'Average words in dialogues: '
        self.label_20.setText(self.label_20_text)

        self.label_21 = QLabel()
        self.label_21_text = 'Average chars in dialogues: '
        self.label_21.setText(self.label_21_text)

        self.label_22 = QLabel()
        self.label_22_text = 'Amount of long dialogues: '
        self.label_22.setText(self.label_22_text)

        self.label_23 = QLabel()
        self.label_23_text = 'Amount of short dialogues: '
        self.label_23.setText(self.label_23_text)

        self.open_text = QLineEdit()
        self.open_text.resize(1, 2)
        self.open_text.setReadOnly(True)

        self.listwidget = QListWidget()

        entries = []

        self.listwidget.addItems(entries)

        # Local labels
        self.label_1_local = QLabel()
        self.label_1_local.setText(self.label_6_text)
        self.label_1_local_value = QLabel()

        self.label_2_local = QLabel()
        self.label_2_local.setText(self.label_7_text)
        self.label_2_local_value = QLabel()

        self.label_3_local = QLabel()
        self.label_3_local.setText(self.label_8_text)
        self.label_3_local_value = QLabel()

        self.label_4_local = QLabel()
        self.label_4_local.setText(self.label_9_text)
        self.label_4_local_value = QLabel()

        self.label_5_local = QLabel()
        self.label_5_local.setText(self.label_10_text)
        self.label_5_local_value = QLabel()


        # add logic
        open_button.clicked.connect(self.openFileNameDialog)
        analyze_button.clicked.connect(self.start_analisye)
        get_chapters_button.clicked.connect(self.getCahptersView)
        prev_button.clicked.connect(self.getPrev)
        next_button.clicked.connect(self.getNext)

        # add layout
        vbox_1 = QVBoxLayout()
        # vbox1.addStretch(1)

        vbox_1.addWidget(self.label_11)
        vbox_1.addWidget(self.progressBar)
        vbox_1.addWidget(label_5)
        vbox_1.addWidget(self.open_text)

        vbox_1.addWidget(label_1)
        vbox_1.addWidget(open_button)

        vbox_1.addWidget(analyze_button)
        # vbox_1.addWidget(charts_button)
        vbox_1.addWidget(get_chapters_button)
        vbox_1.addWidget(get_chapters_txt_button)
        vbox_1.addWidget(get_chapters_excel_button)
        vbox_1.addWidget(exit_button)


        vbox_2 = QVBoxLayout()
        vbox_2.addWidget(label_2)

        vbox_2_1 = QVBoxLayout()
        vbox_2_1.addWidget(self.label_6)
        vbox_2_1.addWidget(self.label_7)
        vbox_2_1.addWidget(self.label_8)
        vbox_2_1.addWidget(self.label_9)
        vbox_2_1.addWidget(self.label_10)

        vbox_2_1_1 = QVBoxLayout()
        vbox_2_1_1.addWidget(self.label_6_1)
        vbox_2_1_1.addWidget(self.label_7_1)
        vbox_2_1_1.addWidget(self.label_8_1)
        vbox_2_1_1.addWidget(self.label_9_1)
        vbox_2_1_1.addWidget(self.label_10_1)

        vbox_2_1.addWidget(self.label_18)
        vbox_2_1.addWidget(self.label_18)
        vbox_2_1.addWidget(self.label_19)
        vbox_2_1.addWidget(self.label_20)
        vbox_2_1.addWidget(self.label_21)
        vbox_2_1.addWidget(self.label_22)

        vbox_2_2 = QVBoxLayout()
        vbox_2_2.addWidget(self.label_12)
        vbox_2_2.addWidget(self.label_13)
        vbox_2_2.addWidget(self.label_14)

        vbox_2_3 = QVBoxLayout()
        vbox_2_3.addWidget(self.label_12)
        vbox_2_3.addWidget(self.label_13)
        vbox_2_3.addWidget(self.label_14)

        vbox_2_3.addWidget(self.label_15)
        vbox_2_3.addWidget(self.label_16)
        vbox_2_3.addWidget(self.label_17)
        vbox_2_3.addWidget(self.listwidget)
        # vbox_2_2.addWidget(self.addChart())

        # hbox_2_3.addWidget(self.label_7)

        vbox_2_4 = QVBoxLayout()
        vbox_2_4.addWidget(self.getPieChart1())

        vbox_2_5 = QVBoxLayout()
        vbox_2_5.addWidget(self.getPieChart2())

        vbox_3 = QHBoxLayout()
        vbox_3.addLayout(vbox_2_1)
        vbox_3.addLayout(vbox_2_1_1)
        vbox_3.addLayout(vbox_2_2)
        vbox_3.addLayout(vbox_2_3)
        vbox_3.addLayout(vbox_2_4)
        vbox_3.addLayout(vbox_2_5)
        vbox_2.addLayout(vbox_3)

        # vbox_3 = QVBoxLayout()


        hbox_3_1 = QHBoxLayout()
        hbox_3_1.addWidget(prev_button)
        hbox_3_1.addWidget(next_button)

        vbox_3_2 = QVBoxLayout()
        vbox_3_2.addWidget(self.label_1_local)
        vbox_3_2.addWidget(self.label_2_local)
        vbox_3_2.addWidget(self.label_3_local)
        vbox_3_2.addWidget(self.label_4_local)
        vbox_3_2.addWidget(self.label_5_local)

        vbox_3_2_val = QVBoxLayout()
        vbox_3_2_val.addWidget(self.label_1_local_value)
        vbox_3_2_val.addWidget(self.label_2_local_value)
        vbox_3_2_val.addWidget(self.label_3_local_value)
        vbox_3_2_val.addWidget(self.label_4_local_value)
        vbox_3_2_val.addWidget(self.label_5_local_value)

        vbox_3_text = QVBoxLayout()
        vbox_3_text.addWidget(self.text_editor)

        hbox_text = QHBoxLayout()
        hbox_text.addLayout(vbox_3_text)
        hbox_text.addLayout(vbox_3_2)
        hbox_text.addLayout(vbox_3_2_val)

        vbox_2.addWidget(self.label_3)
        vbox_2.addLayout(hbox_3_1)
        vbox_2.addLayout(hbox_text)



        # vbox_4 = QVBoxLayout()
        # vbox_4.addWidget(label_4)

        # add layout
        hbox_1 = QHBoxLayout()
        # hbox_1.addStretch()
        # hbox_1.addStretch()
        hbox_1.setAlignment(Qt.AlignTop)
        hbox_1.addLayout(vbox_1)
        # hbox_1.addStretch()

        hbox_2 = QHBoxLayout()
        # hbox.addStretch(1)
        # hbox_2.addLayout(vbox_3)
        # hbox_2.addLayout(vbox_4)
        hbox_2.addLayout(vbox_2)

        vbox_main = QHBoxLayout()
        vbox_main.addLayout(hbox_1)
        vbox_main.addLayout(hbox_2)

        # hbox.addWidget(analyze_button)
        # hbox.addWidget(charts_button)
        # hbox.addWidget(text_editor)

        # vbox = QVBoxLayout()
        # vbox.addStretch(1)
        # vbox.addLayout(hbox)


        self.setLayout(vbox_main)

        self.setWindowTitle("Machine Book Extract")
        self.resize(800,800)
        self.show()

    # =====================================================================================================
    # CONTROL BUTTONS
    def startAnalisye(self):
        self.runTasks()

        # self.b = BookAnalyzer(self.content)
        # self.b.start()
        # self.b.getStatisticsOutput("Peter")

        # add ===========================================
        # self.progressBar.setValue(10)
        # b = thread.join()
        # try:
        #     thread = YouThread(num=14)
        #     thread.start()
        #     # b = BookAnalyzer(self.content)
        #     # b.start()
        #     # b.getStatisticsOutput("Peter")
        #     # self.progressBar.setValue(10)
        #     # b = thread.join()
        # except Exception as e:
        #     print(e)
        # add ===========================================

        # # Set labels basic amount with Readability
        # self.label_11.setText(self.b.getBookLengthWords())
        # self.label_10.setText(self.b.getBookLengthChars())
        # self.label_8.setText(self.b.getBookSentenceAmount())
        # self.label_9.setText(self.b.getBookSentenceAverageChars())
        # self.label_22.setText(self.b.getBookSentenceAverageWords())
        #
        # fre, smog, fog = self.b.getFRESMOGFOGReadability()
        # self.label_27.setText(fre)
        # self.label_28.setText(smog)
        # self.label_29.setText(fog)
        #
        # # Set labels time and dialogues
        # total, present, past, presentPercent, pastPercent = self.b.getTotalVerbsStatisticsAmount()
        # self.label_19.setText(total)
        # self.label_18.setText(present)
        # self.label_16.setText(past)
        #
        # dialoges, dialogesAvergeWords, dialogesAvergeChars, longDialogueAmount, shortDialogueAmount, plong, pshort = self.b.getDialogesAmounts()
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


        # add charts================================================
        # # Add to chart
        # series1 = QPieSeries()
        # series1.append("Past", pastPercent)
        # series1.append("Present", presentPercent)
        # self.chart.removeAllSeries()
        # self.chart.addSeries(series1)
        #

        #
        # adj = self.b.getAdjectivesAmount()
        # self.label_18.setText(self.label_18_text + adj)
        #
        # series2 = QPieSeries()
        # series2.append("Long", plong)
        # series2.append("Short", pshort)
        # self.chart2.removeAllSeries()
        # self.chart2.addSeries(series2)
        #
        # entries = self.b.getCharactersList(self.b.content, self.b.doc, self.b.nlp)
        # self.listwidget.addItems(entries)

    def getCahptersView(self):
        # get fragments
        self.currentVal = 0
        self.amountChapters, self.fragments, self.df1 = self.b.getFragmentsAndChapters()
        print(self.df1)
        self.textEdit.setPlainText(self.fragments[self.currentVal])
        self.label_39.setText('Chapter: ' + str(self.currentVal + 1))
        # self.label_1_local_value.setText(str(self.df1.iat[0, 0]))
        # self.label_2_local_value.setText(str(self.df1.iat[0, 1]))
        # self.label_3_local_value.setText(str(self.df1.iat[0, 2]))
        # self.label_4_local_value.setText(str(self.df1.iat[0, 3]))
        print('Ended')

    def getNext(self):
        if self.currentVal + 1 < len(self.fragments):
            self.currentVal += 1
            self.textEdit.setPlainText(self.fragments[self.currentVal])
            self.label_39.setText('Chapter: ' + str(self.currentVal + 1))
            # self.label_1_local_value.setText(str(self.df1.iat[self.currentVal, 0]))
            # self.label_2_local_value.setText(str(self.df1.iat[self.currentVal, 1]))
            # self.label_3_local_value.setText(str(self.df1.iat[self.currentVal, 2]))
            # self.label_4_local_value.setText(str(self.df1.iat[self.currentVal, 3]))


    def getPrev(self):
        if self.currentVal - 1 >= 0:
            self.currentVal -= 1
            self.textEdit.setPlainText(self.fragments[self.currentVal])
            self.label_39.setText('Chapter: ' + str(self.currentVal + 1))
            # self.label_1_local_value.setText(str(self.df1.iat[self.currentVal, 0]))
            # self.label_2_local_value.setText(str(self.df1.iat[self.currentVal, 1]))
            # self.label_3_local_value.setText(str(self.df1.iat[self.currentVal, 2]))
            # self.label_4_local_value.setText(str(self.df1.iat[self.currentVal, 3]))


    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.txt)", options=options)

        if fileName:
            fileNameSplit = fileName.split('/')
            if len(fileNameSplit) >= 1:
                self.label_20.setText(fileNameSplit[len(fileNameSplit) - 1])
                self.content = open(fileName, encoding="utf8").read()
                # print(self.content)


    def getPieChart1(self):
        self.series = QPieSeries()
        self.series.append("Python", 40)
        self.series.append("C++", 60)

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Pie Chart Example")

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(self.chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        return chartview

    def getPieChart2(self):
        self.series2 = QPieSeries()
        self.series2.append("Python", 40)
        self.series2.append("C++", 60)

        self.chart2 = QChart()
        self.chart2.legend().hide()
        self.chart2.addSeries(self.series2)
        self.chart2.createDefaultAxes()
        self.chart2.setAnimationOptions(QChart.SeriesAnimations)
        self.chart2.setTitle("Pie Chart Example")

        self.chart2.legend().setVisible(True)
        self.chart2.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(self.chart2)
        chartview.setRenderHint(QPainter.Antialiasing)
        return chartview

    def runTasks(self):
        self.thread = MyThread(self.content)
        # print('Start analyze')
        self.progressBar.setValue(0)
        try:
            self.thread.changeValue.connect(self.updateLabels)
            self.thread.start()
        except Exception as e:
            print(e)

        self.stopThread = False
        self.thread2 = MyThreadProgress(self.progressBar, self.stopThread)
        # print('Start counter')
        try:
            self.thread2.start()
        except Exception as e:
            print(e)

    def updateLabels(self, label):
        self.b = label
        self.label_11.setText(self.b.getBookLengthWords())
        self.label_10.setText(self.b.getBookLengthChars())
        self.label_8.setText(self.b.getBookSentenceAmount())
        self.label_9.setText(self.b.getBookSentenceAverageChars())
        self.label_22.setText(self.b.getBookSentenceAverageWords())

        fre, smog, fog = self.b.getFRESMOGFOGReadability()
        self.label_27.setText(fre)
        self.label_28.setText(smog)
        self.label_29.setText(fog)

        # Set labels time and dialogues
        total, present, past, presentPercent, pastPercent = self.b.getTotalVerbsStatisticsAmount()
        self.label_19.setText(total)
        self.label_18.setText(present)
        self.label_16.setText(past)

        dialoges, dialogesAvergeWords, dialogesAvergeChars, longDialogueAmount, shortDialogueAmount, plong, pshort = self.b.getDialogesAmounts()
        self.label_17.setText(dialoges)
        self.label_33.setText(dialogesAvergeWords)
        self.label_34.setText(dialogesAvergeChars)
        self.label_35.setText(longDialogueAmount)
        self.label_36.setText(shortDialogueAmount)

        # Set adjectives
        adj = self.b.getAdjectivesAmount()
        self.label_37.setText("Amount of adjectives: " + adj)

        # Characters
        entries = self.b.getCharactersList(self.b.content, self.b.doc, self.b.nlp)
        self.listWidget.addItems(entries)

        # zatrzymac stad progress bar
        self.progressBar.setValue(100)
        try:
            self.thread2.join()
        except Exception as e:
            print(e)

class MyThread(QThread):
    changeValue = pyqtSignal(object)

    def __init__(self, content, parent=None):
        QThread.__init__(self, parent)
        self.content = content
        # print(content)

    def run(self):
        # print('Dupa')
        try:
            print(len(self.content))
            b = BookAnalyzer(self.content)
            b.start()
            b.getStatisticsOutput("Peter")

            self.changeValue.emit(b)
            print(threading)
            # print('Ended')
        except Exception as e:
            print('Exception ' + str(e))


class MyThreadProgress(QThread):
    changeValue = pyqtSignal(str)

    def __init__(self, progressBar, stopThread, parent=None):
        QThread.__init__(self, parent)
        self.counter = 0
        self.progressBar = progressBar
        self.stopThread = stopThread
        self._stopevent = threading.Event()
        self._sleepperiod = 1.

    def run(self):
        # print('Dupa')
        try:
            while not self._stopevent.isSet():
                self.counter += 1
                self.progressBar.setValue(self.counter)
                time.sleep(1)
                if self.counter == 100:
                    break
                self._stopevent.wait(self._sleepperiod)

            # print('Ended')
        except Exception as e:
            print('Exception ' + str(e))

    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set()
        threading.Thread.join(self, timeout)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
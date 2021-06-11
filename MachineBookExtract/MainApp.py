
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

    # =====================================================================================================
    # CONTROL BUTTONS
    def startAnalisye(self):
        self.runTasks()

    def getCahptersView(self):
        # get fragments
        self.currentVal = 0
        self.amountChapters, self.fragments, self.df1 = self.b.getFragmentsAndChapters()
        print(self.df1)
        try:
            self.textEdit.setPlainText(self.fragments[self.currentVal])
            self.label_39.setText('Chapter: ' + str(self.currentVal + 1))
            self.label_63.setText(str(self.df1.iat[self.currentVal, 0]))
            self.label_62.setText(str(self.df1.iat[self.currentVal, 1]))
            self.label_61.setText(str(self.df1.iat[self.currentVal, 4]))
            self.label_60.setText(str(self.df1.iat[self.currentVal, 3]))
            self.label_59.setText(str(self.df1.iat[self.currentVal, 2]))
            # self.label_57.setText(str(self.df1.iat[self.currentVal, 5]))
            # self.label_64.setText(str(self.df1.iat[self.currentVal, 8]))
            # self.label_58.setText(str(self.df1.iat[self.currentVal, 9]))
            # self.label_41.setText(str(self.df1.iat[self.currentVal, 16]))
            # self.label_42.setText(str(self.df1.iat[self.currentVal, 15]))
            # self.label_43.setText(str(self.df1.iat[self.currentVal, 14]))
            # self.label_44.setText(str(self.df1.iat[self.currentVal, 12]))
        except Exception as e:
            print(e)

        print('Ended')

    def getNext(self):
        if self.currentVal + 1 < len(self.fragments):
            self.currentVal += 1
            self.textEdit.setPlainText(self.fragments[self.currentVal])
            self.label_39.setText('Chapter: ' + str(self.currentVal + 1))
            self.label_63.setText(str(self.df1.iat[self.currentVal, 0]))
            self.label_62.setText(str(self.df1.iat[self.currentVal, 1]))
            self.label_61.setText(str(self.df1.iat[self.currentVal, 4]))
            self.label_60.setText(str(self.df1.iat[self.currentVal, 3]))
            self.label_59.setText(str(self.df1.iat[self.currentVal, 2]))
            # self.label_57.setText(str(self.df1.iat[self.currentVal, 5]))
            # self.label_64.setText(str(self.df1.iat[self.currentVal, 8]))
            # self.label_58.setText(str(self.df1.iat[self.currentVal, 9]))
            # self.label_41.setText(str(self.df1.iat[self.currentVal, 16]))
            # self.label_42.setText(str(self.df1.iat[self.currentVal, 15]))
            # self.label_43.setText(str(self.df1.iat[self.currentVal, 14]))
            # self.label_44.setText(str(self.df1.iat[self.currentVal, 12]))


    def getPrev(self):
        if self.currentVal - 1 >= 0:
            self.currentVal -= 1
            self.textEdit.setPlainText(self.fragments[self.currentVal])
            self.label_39.setText('Chapter: ' + str(self.currentVal + 1))
            self.label_63.setText(str(self.df1.iat[self.currentVal, 0]))
            self.label_62.setText(str(self.df1.iat[self.currentVal, 1]))
            self.label_61.setText(str(self.df1.iat[self.currentVal, 4]))
            self.label_60.setText(str(self.df1.iat[self.currentVal, 3]))
            self.label_59.setText(str(self.df1.iat[self.currentVal, 2]))
            # self.label_57.setText(str(self.df1.iat[self.currentVal, 5]))
            # self.label_64.setText(str(self.df1.iat[self.currentVal, 8]))
            # self.label_58.setText(str(self.df1.iat[self.currentVal, 9]))
            # self.label_41.setText(str(self.df1.iat[self.currentVal, 16]))
            # self.label_42.setText(str(self.df1.iat[self.currentVal, 15]))
            # self.label_43.setText(str(self.df1.iat[self.currentVal, 14]))
            # self.label_44.setText(str(self.df1.iat[self.currentVal, 12]))


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


    # =================================================================================

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
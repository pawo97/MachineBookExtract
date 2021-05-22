
import asyncio
import sys
from asyncio import coroutine
from time import sleep, time

from PyQt5.QtChart import QPieSeries, QPieSlice, QChartView
from PyQt5.QtCore import QRunnable, pyqtSlot, Qt, QThread, QObject, pyqtSignal
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QPlainTextEdit, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QWidget, QLabel, \
    QLineEdit, QFileDialog, QListView, QListWidget, QGridLayout, QTableWidget, QTableWidgetItem
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

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.content = ''
        self.initUI()

    def initUI(self):

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

        self.label_7 = QLabel()
        self.label_7_text = 'Amount of chars: '
        self.label_7.setText(self.label_7_text)

        self.label_8 = QLabel()
        self.label_8_text = 'Amount of sentences: '
        self.label_8.setText(self.label_8_text)

        self.label_9 = QLabel()
        self.label_9_text = 'Average amount of sentences (chars): '
        self.label_9.setText(self.label_9_text)

        self.label_10 = QLabel()
        self.label_10_text = 'Average amount of sentences (words): '
        self.label_10.setText(self.label_10_text)

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

        vbox_2_2.addWidget(self.label_15)
        vbox_2_2.addWidget(self.label_16)
        vbox_2_2.addWidget(self.label_17)
        vbox_2_2.addWidget(self.listwidget)
        # vbox_2_2.addWidget(self.addChart())

        # hbox_2_3.addWidget(self.label_7)

        vbox_2_3 = QVBoxLayout()
        # self.createTable()
        # vbox_2_3.addWidget(self.tableWidget)

        vbox_3 = QHBoxLayout()
        vbox_3.addLayout(vbox_2_1)
        vbox_3.addLayout(vbox_2_2)
        vbox_3.addLayout(vbox_2_3)

        vbox_2.addLayout(vbox_3)

        # vbox_3 = QVBoxLayout()


        hbox_3_1 = QHBoxLayout()
        hbox_3_1.addWidget(prev_button)
        hbox_3_1.addWidget(next_button)

        vbox_2.addWidget(self.label_3)
        vbox_2.addLayout(hbox_3_1)
        vbox_2.addWidget(self.text_editor)

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

    def start_analisye(self):
        print("Start")
        self.get_values()


    def get_values(self):
        self.b = BookAnalyzer(self.content)
        self.b.start()
        self.b.getStatisticsOutput("Peter")
        self.progressBar.setValue(10)
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

        # Set labels
        self.label_6.setText(self.label_6_text + self.b.getBookLengthWords())
        self.label_7.setText(self.label_7_text + self.b.getBookLengthChars())
        self.label_8.setText(self.label_8_text + self.b.getBookSentenceAmount())
        self.label_9.setText(self.label_9_text + self.b.getBookSentenceAverageChars())
        self.label_10.setText(self.label_10_text + self.b.getBookSentenceAverageWords())

        total, present, past = self.b.getTotalVerbsStatisticsAmount()
        self.label_12.setText(self.label_12_text + total)
        self.label_13.setText(self.label_13_text + present)
        self.label_14.setText(self.label_14_text + past)

        fre, smog, fog = self.b.getFRESMOGFOGReadability()
        self.label_15.setText(self.label_15_text + fre)
        self.label_16.setText(self.label_16_text + smog)
        self.label_17.setText(self.label_17_text + fog)

        adj = self.b.getAdjectivesAmount()
        self.label_18.setText(self.label_18_text + adj)

        s1, s2, s3, s4, s5 = self.b.getDialogesAmounts()
        self.label_19.setText(self.label_19_text + s1)
        self.label_20.setText(self.label_20_text + s2)
        self.label_21.setText(self.label_21_text + s3)
        self.label_22.setText(self.label_22_text + s4)
        self.label_23.setText(self.label_23_text + s5)

        entries = self.b.getCharactersList(self.b.content, self.b.doc, self.b.nlp)
        self.listwidget.addItems(entries)

    def getCahptersView(self):
        # get fragments
        self.currentVal = 0
        self.amountChapters, self.fragments = self.b.getFragmentsAndChapters()
        # self.text_editor = self.fragments[0]
        self.text_editor.setPlainText(self.fragments[self.currentVal])
        self.label_3.setText('Chapter: ' + str(self.currentVal + 1))
        print('Ended')

    def getNext(self):
        if self.currentVal + 1 < len(self.fragments):
            self.currentVal += 1
            self.text_editor.setPlainText(self.fragments[self.currentVal])
            self.label_3.setText('Chapter: ' + str(self.currentVal + 1))


    def getPrev(self):
        if self.currentVal - 1 >= 0:
            self.currentVal -= 1
            self.text_editor.setPlainText(self.fragments[self.currentVal])
            self.label_3.setText('Chapter: ' + str(self.currentVal + 1))

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.txt)", options=options)

        if fileName:
            fileNameSplit = fileName.split('/')
            if len(fileNameSplit) >= 1:
                self.open_text.setText(fileNameSplit[len(fileNameSplit) - 1])
                self.content = open(fileName, encoding="utf8").read()
                # print(self.content)


    def getPieChart(self):
        self.chartView = QChartView()
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chartView.chart()
        self.m_donuts = []
        # self.chart.legend().setVisible(False)
        # self.chart.setTitle("Nested donuts demo")
        # self.chart.setAnimationOptions(QChart.AllAnimations)

        minSize = 0.1
        maxSize = 0.9
        donutCount = 5

        donut = QPieSeries()
        sliceCount = 2
        for j in range(sliceCount):
            # Amount size
            value = 60
            slice_ = QPieSlice(str(value), value)
            slice_.setLabelVisible(True)
            slice_.setLabelColor(Qt.white)
            slice_.setLabelPosition(QPieSlice.LabelInsideTangential)
            # slice_.hovered[bool].connect(functools.partial(self.explodeSlice, slice_=slice_))
            donut.append(slice_)
            donut.setHoleSize(minSize + 1 * (maxSize - minSize) / donutCount)
            donut.setPieSize(minSize + (1 + 1) * (maxSize - minSize) / donutCount)


        self.m_donuts.append(donut)
        # self.chartView.chart().addSeries(donut)

        return self.chartView
        # create main layout
        # self.mainLayout = QGridLayout(self)
        # self.mainLayout.addWidget(self.chartView, 1, 1)
        # self.chartView.show()
        # self.setLayout(self.mainLayout)


# class MyThread(QThread):
#
#     def __init__(self, content):
#         QThread.__init__(self)
#         self.content = content
#
#     def run(self):
#         try:
#             # b = BookAnalyzer(self.content)
#             # b.start()
#             # b.getStatisticsOutput("Peter")
#             print('Finished')
#             # return b
#         except Exception as e:
#             print(e)

class YouThread(QtCore.QThread):

    def __init__(self, parent=None, num=None):
        QtCore.QThread.__init__(self, parent)
        self.num = num

    def run(self):
        print(self.num)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
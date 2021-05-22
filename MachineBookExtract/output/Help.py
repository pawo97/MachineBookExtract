#
# # extract epub to text:
# # https://github.com/kevinxiong/epub2txt
#
# # import nltk
# # from nameparser.parser import HumanName
# #
# # def get_human_names(text):
# #     tokens = nltk.tokenize.word_tokenize(text)
# #     pos = nltk.pos_tag(tokens)
# #     sentt = nltk.ne_chunk(pos, binary = False)
# #     person_list = []
# #     person = []
# #     name = ""
# #     for subtree in sentt.subtrees(filter=lambda t: t.node == 'PERSON'):
# #         for leaf in subtree.leaves():
# #             person.append(leaf[0])
# #         if len(person) > 1: #avoid grabbing lone surnames
# #             for part in person:
# #                 name += part + ' '
# #             if name[:-1] not in person_list:
# #                 person_list.append(name[:-1])
# #             name = ''
# #         person = []
# #
# #     return (person_list)
# #
# # text = """
# # Some economists have responded positively to Bitcoin, including
# # Francois R. Velde, senior economist of the Federal Reserve in Chicago
# # who described it as "an elegant solution to the problem of creating a
# # digital currency." In November 2013 Richard Branson announced that
# # Virgin Galactic would accept Bitcoin as payment, saying that he had invested
# # in Bitcoin and found it "fascinating how a whole new global currency
# # has been created", encouraging others to also invest in Bitcoin.
# # Other economists commenting on Bitcoin have been critical.
# # Economist Paul Krugman has suggested that the structure of the currency
# # incentivizes hoarding and that its value derives from the expectation that
# # others will accept it as payment. Economist Larry Summers has expressed
# # a "wait and see" attitude when it comes to Bitcoin. Nick Colas, a market
# # strategist for ConvergEx Group, has remarked on the effect of increasing
# # use of Bitcoin and its restricted supply, noting, "When incremental
# # adoption meets relatively fixed supply, it should be no surprise that
# # prices go up. And that’s exactly what is happening to BTC prices."
# # """
# #
# # names = get_human_names(text)
# # print("LAST, FIRST")
# # for name in names:
# #         last_first = HumanName(name).last + ', ' + HumanName(name).first
# #         print(last_first)
#
# #
# # text = "Bed and chair are types of furniture"
# #
# # print(text)
# # #
# # # DT is the determinant
# # #
# # # VBP is the verb
# # #
# # # JJ is the adjective
# # #
# # # IN is the preposition
# # #
# # # NN is the noun
# #
# # import nltk
# # sentence = [("a", "DT"),("clever","JJ"),("fox","NN"),("was","VBP"),
# #    ("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]
# #
# # grammar = "NP:{<DT>?<JJ>*<NN>}"
# #
# # parser_chunking = nltk.RegexpParser(grammar)
# #
# # parser_chunking.parse(sentence)
# #
# # output = parser_chunking.parse(sentence)
# #
# # output.draw()
#
#
# ##SPACY
# # from collections import Counter
# import re
#
# import spacy
# import ebooklib
# from ebooklib import epub
#
# # Spicy version, python version, en_core_web_sm version
# # # Load English tokenizer, tagger, parser and NER
# from MachineBookExtract.venv.epub2txt import main_method
#
# nlp = spacy.load("en_core_web_sm")
# print("Test1")
# # Process whole documents
# text = ("When Sebastian Thrun started working on self-driving cars at "
#         "Google in 2007, few people outside of the company took him "
#         "seriously. “I can tell you very senior CEOs of major American "
#         "car companies would shake my hand and turn away because I wasn’t "
#         "worth talking to,” said Thrun, in an interview with Recode earlier "
#         "this week.")
# doc = nlp(text)
#
# # Analyze syntax
# # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
# #
# # # Find named entities, phrases and concepts
# # for entity in doc.ents:
# #     print(entity.text, entity.label_)
#
# #book = epub.read_epub(r'C:\Users\pa-wo\Desktop\Studia\Magisterka\MachineBookExtract\MobyDick.epub')
# # str = []
#
# #main_method(r'C:\Users\pa-wo\Desktop\Studia\Magisterka\MachineBookExtract\MobyDick.epub')
#
# # str = open('test111.txt',  encoding="utf8").read()
# #
# # #print(str)
# #
# # # text = ("When Sebastian Thrun started working on self-driving cars at "
# # #         "Google in 2007, few people outside of the company took him "
# # #         "seriously. “I can tell you very senior CEOs of major American "
# # #         "car companies would shake my hand and turn away because I wasn’t "
# # #         "worth talking to,” said Thrun, in an interview with Recode earlier "
# # #         "this week.")
# #
# # info = (str[:999990] + '..') if len(str) > 999990 else str
# # # info = info.replace('\n', '')
# # # info = info.replace('        ## CHAPTER', '')
# # # info = info.replace('�', '')
# #
# # doc = nlp(info)
# #
# # # Analyze syntax
# # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
# #
# # # Find named entities, phrases and concepts
# #
# #
# # for entity in doc.ents:
# #         #if entity.label_ == 'PERSON':
# #         #print(entity.text)
# #         print(entity.text, entity.label_)
#================================================================
# import sys, datetime, time, random
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import Qt, QThread, pyqtSignal
#
#
# class MyThread(QThread):
#
#     change_value = pyqtSignal(int,int,int)
#     speed = 0
#     userID = None
#     def __init__(self, barNumber, parent=None):
#         QThread.__init__(self, parent)
#         self.barNumber = barNumber
#
#     def run(self):
#         cnt = 0
#         while cnt < 100:
#             cnt+=1
#             time.sleep(self.speed)
#             self.change_value.emit(self.userID,self.barNumber,cnt)
#
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("DropBox")
#         self.resize(1000,400)
#
#         self.listQueue = []
#         self.usersInQueue = []
#
#
#         self.btnAddRequest = QtWidgets.QPushButton('Add Request')
#         self.btnAddRequest.clicked.connect(self.addRequest)
#
#         self.labelUser = QtWidgets.QLabel("User ID")
#         self.spinBoxUser = QtWidgets.QSpinBox()
#
#         self.labelFiles = QtWidgets.QLabel("Number of files")
#         self.spinBoxFiles = QtWidgets.QSpinBox()
#         self.spinBoxFiles.setMaximum(1000)
#
#         self.labelSize = QtWidgets.QLabel("File size [MB]")
#         self.lineSize = QtWidgets.QLineEdit()
#         self.lineSize.setText("0")
#         self.lineSize.setMaximumWidth(200)
#
#         self.tableQueue = QtWidgets.QTableWidget()
#         self.tableQueue.setColumnCount(5)
#         self.tableQueue.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
#         self.tableQueue.setHorizontalHeaderLabels(["User ID", "Number of files", "File size [MB]", "Date", "Priority"])
#         self.tableQueue.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         header = self.tableQueue.horizontalHeader()
#         header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
#
#         vboxThreads = QtWidgets.QVBoxLayout()
#
#         numberOfThreads = 5
#
#         self.threads = []
#         for i in range(0,numberOfThreads):
#             thread = MyThread(i)
#             thread.change_value.connect(self.setProgressVal)
#             thread.finished.connect(self.startThread)
#             thread.started.connect(self.startThread)
#             self.threads.append(thread)
#
#         self.progressLabels = {}
#         self.progressBars = {}
#         for i in range(0,numberOfThreads):
#             label = QtWidgets.QLabel()
#             progressBar = QtWidgets.QProgressBar()
#             progressBar.setMaximumWidth(200)
#             self.progressLabels[i] = label
#             self.progressBars[i] = progressBar
#             vboxThreads.addWidget(label)
#             vboxThreads.addWidget(progressBar)
#
#         vbox = QtWidgets.QVBoxLayout()
#         vbox.addWidget(self.btnAddRequest)
#         vbox.addWidget(self.labelUser)
#         vbox.addWidget(self.spinBoxUser)
#         vbox.addWidget(self.labelFiles)
#         vbox.addWidget(self.spinBoxFiles)
#         vbox.addWidget(self.labelSize)
#         vbox.addWidget(self.lineSize)
#
#         grid = QtWidgets.QGridLayout()
#         grid.addLayout(vbox,0,0, alignment=Qt.AlignTop)
#         grid.addWidget(self.tableQueue,0,1)
#         grid.addLayout(vboxThreads,0,2)
#
#         mainView = QtWidgets.QWidget()
#         mainView.setLayout(grid)
#
#         self.setCentralWidget(mainView)
#
#     def addRequest(self):
#         id = self.spinBoxUser.value()
#         if id not in self.usersInQueue:
#             values = {"id": id , "files" : self.spinBoxFiles.value(),"size" : self.lineSize.text(), "date" : datetime.datetime.now()}
#             if values['files'] > 0:
#                 self.usersInQueue.append(id)
#                 self.spinBoxUser.setValue(random.randint(0, 99))
#                 self.listQueue.append(values)
#                 self.setPriority()
#                 self.addToQueueTable()
#                 self.startThread()
#
#     def addToQueueTable(self):
#         self.tableQueue.setRowCount(0)
#         for row, list in enumerate(self.listQueue):
#             self.tableQueue.insertRow(row)
#             for col, value in enumerate(list.values()):
#                 self.tableQueue.setItem(row, col, QtWidgets.QTableWidgetItem(str(value)))
#
#     def setPriority(self):
#         for value in self.listQueue:
#             weight = ((value['files']) * float(value['size'])/(1+datetime.datetime.now().timestamp()-value['date'].timestamp()))*100
#             value['priority'] = weight
#         self.listQueue = sorted(self.listQueue, key=lambda k: k['priority'])
#
#     def startThread(self):
#         if len(self.listQueue) > 0:
#             for thread in self.threads:
#                 if thread.isRunning() == False:
#                     self.setPriority()
#                     file = self.getOneFile()
#                     thread.speed = float(file['size'])/1000;
#                     thread.userID = file['id']
#                     thread.start()
#                     self.addToQueueTable()
#                     break
#
#     def getOneFile(self):
#         file = self.listQueue[0]
#         if file['files'] == 1:
#             self.usersInQueue.remove(file['id'])
#             fileToSend = self.listQueue.pop(0)
#         else:
#             file['files'] = file['files'] - 1
#             fileToSend = file.copy()
#             fileToSend['files'] = 1
#         return fileToSend
#
#     def setProgressVal(self, userID, barNumber, val):
#         self.progressLabels[barNumber].setText(f"UserID: {userID}")
#         self.progressBars[barNumber].setValue(val)
#         if self.progressBars[barNumber].value() == 100:
#             self.progressBars[barNumber].setValue(0)
#             self.progressLabels[barNumber].clear()
#
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     app.setStyle('Fusion')
#     window = MainWindow()
#     window.show()
#     app.exec_()
# =================================================================
# Pie chart
import functools
import random

from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 200)

        self.m_donuts = []

        self.chartView = QChartView()
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chartView.chart()
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
        self.chartView.chart().addSeries(donut)


        # create main layout
        self.mainLayout = QGridLayout(self)
        self.mainLayout.addWidget(self.chartView, 1, 1)
        self.chartView.show()
        self.setLayout(self.mainLayout)

        # self.updateTimer = QTimer(self)
        # self.updateTimer.timeout.connect(self.updateRotation)
        # self.updateTimer.start(1250)


    def updateRotation(self):
        for donut in self.m_donuts:
            phaseShift =  random.randrange(-50, 100)
            donut.setPieStartAngle(donut.pieStartAngle() + phaseShift)
            donut.setPieEndAngle(donut.pieEndAngle() + phaseShift)


    def explodeSlice(self, exploded, slice_):
        if exploded:
            self.updateTimer.stop()
            sliceStartAngle = slice_.startAngle()
            sliceEndAngle = slice_.startAngle() + slice_.angleSpan()

            donut = slice_.series()
            seriesIndex = self.m_donuts.index(donut)
            for i in range(seriesIndex + 1, len(self.m_donuts)):
                self.m_donuts[i].setPieStartAngle(sliceEndAngle)
                self.m_donuts[i].setPieEndAngle(360 + sliceStartAngle)
        else:
            for donut in self.m_donuts:
                donut.setPieStartAngle(0)
                donut.setPieEndAngle(360)
            self.updateTimer.start()
        slice_.setExploded(exploded)


a = QApplication([])
w = Widget()
w.show()
a.exec_()
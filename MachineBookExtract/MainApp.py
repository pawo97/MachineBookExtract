# import sys
#
# from PyQt5.QtWidgets import QPlainTextEdit, QHBoxLayout, QVBoxLayout, QPushButton
# from qtpy import QtWidgets
#
#
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("Machine Book Extract")
#         self.resize(800,800)
#
#         self.listQueue = []
#         self.usersInQueue = []
#
#         self.text_editor = QPlainTextEdit(self)
#         self.text_editor.setReadOnly(True)
#         self.text_editor.resize(400, 200)
#
#         hbox = QHBoxLayout()
#         self.analyze_button = QPushButton('Analyze')
#         hbox.addWidget(self.analyze_button)
#
#         vbox = QVBoxLayout()
#         vbox.addLayout(hbox)
#         vbox.addWidget(self.text_editor)
#
#         self.setLayout(vbox)
#         self.show()
#
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     sys.exit(app.exec_())
import sys
from time import sleep, time

from PyQt5.QtCore import QRunnable, pyqtSlot, Qt
from PyQt5.QtWidgets import QPlainTextEdit, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QWidget, QLabel, \
    QLineEdit, QFileDialog
from matplotlib.backends.backend_template import FigureCanvas
from qtpy import QtWidgets
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

        text_editor = QPlainTextEdit()
        text_editor.setReadOnly(True)
        text_editor.setPlainText('TEST')
        text_editor.setFixedWidth(500)
        text_editor.setFixedHeight(500)

        label_1 = QLabel()
        label_1.setText('Menu: ')

        label_2 = QLabel()
        label_2.setText('Basic statistics: ')

        label_3 = QLabel()
        label_3.setText('Chapter: ')

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

        self.open_text = QLineEdit()
        self.open_text.resize(1, 2)
        self.open_text.setReadOnly(True)

        # add logic
        open_button.clicked.connect(self.openFileNameDialog)
        analyze_button.clicked.connect(self.start_analisye)


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

        vbox_2_2 = QVBoxLayout()
        vbox_2_2.addWidget(self.label_12)
        vbox_2_2.addWidget(self.label_13)
        vbox_2_2.addWidget(self.label_14)
        # vbox_2_2.addWidget(self.addChart())

        # hbox_2_3.addWidget(self.label_7)

        vbox_3 = QHBoxLayout()
        vbox_3.addLayout(vbox_2_1)
        vbox_3.addLayout(vbox_2_2)

        vbox_2.addLayout(vbox_3)

        # vbox_3 = QVBoxLayout()


        hbox_3_1 = QHBoxLayout()
        hbox_3_1.addWidget(prev_button)
        hbox_3_1.addWidget(next_button)

        vbox_2.addWidget(label_3)
        vbox_2.addLayout(hbox_3_1)
        vbox_2.addWidget(text_editor)

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
        self.progressBar.setValue(10)
        b = BookAnalyzer(self.content)
        b.start(self.progressBar)
        b.getStatisticsOutput("Peter")
        self.progressBar.setValue(0)

        self.label_6.setText(self.label_6_text + b.getBookLengthWords())
        self.label_7.setText(self.label_7_text + b.getBookLengthChars())
        self.label_8.setText(self.label_8_text + b.getBookSentenceAmount())
        self.label_9.setText(self.label_9_text + b.getBookSentenceAverageChars())
        self.label_10.setText(self.label_10_text + b.getBookSentenceAverageWords())

        total, present, past = b.getTotalVerbsStatisticsAmount()
        self.label_12.setText(self.label_12_text + total)
        self.label_13.setText(self.label_13_text + present)
        self.label_14.setText(self.label_14_text + past)




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

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
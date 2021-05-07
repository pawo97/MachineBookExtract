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

from PyQt5.QtCore import QRunnable, pyqtSlot
from PyQt5.QtWidgets import QPlainTextEdit, QHBoxLayout, QVBoxLayout, QPushButton, QApplication, QWidget, QLabel, \
    QLineEdit, QFileDialog
from qtpy import QtWidgets


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


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.content = ''
        self.initUI()

    def initUI(self):

        # create components
        analyze_button = QPushButton("Analyze")
        charts_button = QPushButton("Charts")
        get_chapters_button = QPushButton("Get chapters")
        get_chapters_txt_button = QPushButton("Save txt")
        get_chapters_excel_button = QPushButton("Save excel")
        open_button = QPushButton("Open")
        exit_button = QPushButton("Exit")

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

        self.label_6 = QLabel()
        self.label_6.setText('Amount of words: ')

        self.label_7 = QLabel()
        self.label_7.setText('Amount of chars: ')

        self.label_8 = QLabel()
        self.label_8.setText('Amount of sentences: ')

        self.label_9 = QLabel()
        self.label_9.setText('Average amount of sentences (chars): ')

        self.label_10 = QLabel()
        self.label_10.setText('Average amount of sentences (words): ')


        self.open_text = QLineEdit()
        self.open_text.resize(1, 2)
        self.open_text.setReadOnly(True)

        # add logic
        open_button.clicked.connect(self.openFileNameDialog)
        analyze_button.clicked.connect(self.start_analisye)


        # add layout
        vbox_1 = QVBoxLayout()
        # vbox1.addStretch(1)
        vbox_1.addWidget(label_1)
        vbox_1.addWidget(open_button)

        vbox_1.addWidget(analyze_button)
        vbox_1.addWidget(charts_button)
        vbox_1.addWidget(get_chapters_button)
        vbox_1.addWidget(get_chapters_txt_button)
        vbox_1.addWidget(get_chapters_excel_button)
        vbox_1.addWidget(exit_button)

        vbox_2 = QVBoxLayout()
        vbox_2.addWidget(label_5)
        vbox_2.addWidget(self.open_text)
        vbox_2.addWidget(label_2)

        hbox_2_1 = QHBoxLayout()
        hbox_2_1.addWidget(self.label_6)
        hbox_2_1.addWidget(self.label_7)

        hbox_2_2 = QHBoxLayout()
        hbox_2_2.addWidget(self.label_8)
        hbox_2_2.addWidget(self.label_9)

        hbox_2_3 = QHBoxLayout()
        hbox_2_3.addWidget(self.label_10)
        # hbox_2_3.addWidget(self.label_7)

        vbox_2.addLayout(hbox_2_1)
        vbox_2.addLayout(hbox_2_2)
        vbox_2.addLayout(hbox_2_3)

        vbox_3 = QVBoxLayout()
        vbox_3.addWidget(label_3)
        vbox_3.addWidget(text_editor)

        vbox_4 = QVBoxLayout()
        vbox_4.addWidget(label_4)

        # add layout
        hbox_1 = QHBoxLayout()
        # hbox.addStretch(1)
        hbox_1.addLayout(vbox_1)
        hbox_1.addLayout(vbox_2)

        hbox_2 = QHBoxLayout()
        # hbox.addStretch(1)
        hbox_2.addLayout(vbox_3)
        hbox_2.addLayout(vbox_4)

        vbox_main = QVBoxLayout()
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
        b = BookAnalyzer(self.content)
        b.start()
        b.getStatisticsOutput("Peter")

        self.label_7.setText('Number of characters: ' + b.getBookLengthChars())
        self.label_6.setText('Number of words: ' + b.getBookLengthWords())


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



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
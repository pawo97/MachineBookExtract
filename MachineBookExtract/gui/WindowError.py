from PyQt5.QtChart import QPieSeries, QChart, QChartView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QMessageBox
from qtpy import QtWidgets


def show_error(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText('More information')
    msg.setWindowTitle("Error")
    msg.exec_()


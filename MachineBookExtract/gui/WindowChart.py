from PyQt5.QtChart import QPieSeries, QChart, QChartView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout


class WindowChart(QMainWindow):
    def __init__(self, one, two, title, oneLabel, twoLabel):
        super().__init__()
        self.one = one
        self.two = two
        self.title = title
        self.oneLabel = oneLabel
        self.twoLabel = twoLabel

        self.setWindowTitle('Charts')
        self.setFixedSize(640, 480)
        self.hboxLayout = QHBoxLayout()

        self.setCentralWidget(self.getPieChart1())
        # self.setLayout(self.hboxLayout)

    def getPieChart1(self):
        self.series = QPieSeries()
        self.series.append(self.oneLabel, self.one)
        self.series.append(self.twoLabel, self.two)

        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle(self.title)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(self.chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        return chartview
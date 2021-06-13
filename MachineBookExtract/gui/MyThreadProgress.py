import threading
import time

from PyQt5.QtCore import QThread, pyqtSignal


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
from GuI import Ui_MainWindow
import sys
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QGridLayout,
    QPushButton,
    QSlider,
)

from time import sleep
from threading import Thread

class UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.changeValue()

        #print(self.Top3_V2Label.text())
    def changeValue(self):
        self.checkBox.toggled.connect(self.do)
        self.Top1_V1Spin.textChanged.connect(self.setV1)
        self.Top1_VUVSpin.textChanged.connect(self.setV1)
        self.Top1_I1PSpin.textChanged.connect(self.setV1)
        
    def setV1(self):
        # self.Top1_V1Spin.setMinimum(14)
        V1 = self.Top1_V1Spin.value()
        UV1 = self.Top1_VUVSpin.value()
        IP = self.Top1_I1PSpin.value()
        
    def do(self):
        # print(self.checkBox.isChecked())
        if self.checkBox.isChecked() == True:
            self.Mode_Label.setText("MODE: BOOST CONVERTER")
        else:
            self.Mode_Label.setText("MODE: BUCK CONVERTER")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI()
    win.show()
    app.exec()
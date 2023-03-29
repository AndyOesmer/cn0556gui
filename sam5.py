from CN0556_GUI_Design5 import Ui_MainWindow
import sys
from PyQt5.QtCore import Qt, QThread
from PyQt5.QtWidgets import (
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
from PyQt5 import uic
from time import sleep
from threading import Thread

'''
class for reading/writing ADC/DAC

'''
class CN0556:
    def __init__(self,device):
        
        # Buck In / Boost Out Initialization
        self.V1_Input = 0
        self.UV1_Input = 0
        self.IP1_Input = 0
        self.IN1_Input = 0
        self.P1_Input = 0

        # Boost In / Buck Out Initialization
        self.V2_Input = 0
        self.UV2_Input = 0
        self.IP2_Input = 0
        self.IN2_Input = 0
        self.P2_Input = 0

        # MODE Initialization
        self.mode = 0 # Default Boost Mode

    def Start_():
        ...


class UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("CN0556_GUI_Design5.ui", self)
        self.setupUi(self)
        self.changeValue()

    def changeValue(self):
        
        self.checkBox.toggled.connect(self.do)

        ##### For V1 Write Values:
        self.V1_SpinBox.textChanged.connect(self.setV1)
        self.V1uv_SpinBox.textChanged.connect(self.setV1)
        self.I1P_SpinBox.textChanged.connect(self.setV1)
        self.I1N_SpinBox.textChanged.connect(self.setV1)
        self.Power1_SpinBox.textChanged.connect(self.setV1)

        ##### For V2 Write Values:
        self.V2_SpinBox.textChanged.connect(self.setV2)
        self.V2uv_SpinBox.textChanged.connect(self.setV2)
        self.I2P_SpinBox.textChanged.connect(self.setV2)
        self.I2N_SpinBox.textChanged.connect(self.setV2)
        self.Power2_SpinBox.textChanged.connect(self.setV2)

    def setV1(self):
        # self.Top1_V1Spin.setMinimum(14)
        V1 = self.V1_SpinBox.value()
        UV1 = self.V1uv_SpinBox.value()
        IP1 = self.I1P_SpinBox.value()
        IN1 = self.I1N_SpinBox.value()
        P1 = self.Power1_SpinBox.value()

        print(str(V1) + " " + str(UV1) + " " + str(IP1) + " " + str(IN1) + " " + str(P1))

    def setV2(self):
        # self.Top1_V1Spin.setMinimum(14)
        V2 = self.V2_SpinBox.value()
        UV2 = self.V2uv_SpinBox.value()
        IP2 = self.I2P_SpinBox.value()
        IN2 = self.I2N_SpinBox.value()
        P2 = self.Power2_SpinBox.value()
        print(str(V2) + " " + str(UV2) + " " + str(IP2) + " " + str(IN2) + " " + str(P2))

    def do(self):
        # print(self.checkBox.isChecked())
        if self.checkBox.isChecked() == True:
            self.Mode_Label.setText("MODE: BUCK CONVERTER")
            Mode = 1 # self.Mode
        else:
            self.Mode_Label.setText("MODE: BOOST CONVERTER")
            Mode = 0 # self.Mode


'''
class for SIGNALS QTHREAD

'''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI()
    win.show()
    app.exec()

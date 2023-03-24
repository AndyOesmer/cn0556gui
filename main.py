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
from pglive.sources.data_connector import DataConnector
from time import sleep
from threading import Thread

DISPLAY_HEIGHT = 600


class CN0556_GUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(500,500)

        self.setWindowTitle("CN0556 GUI")
        self.setWindowState(Qt.WindowMaximized)
        self.generalLayout = QHBoxLayout()
        
        parentWidget = QWidget(self)
        parentWidget.setLayout(self.generalLayout)
        self.setCentralWidget(parentWidget)
        
        self.top = QHBoxLayout()
        self.generalLayout.addLayout(self.top)
        self.bottom = QHBoxLayout()
        self.generalLayout.addLayout(self.bottom)

        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()
        self.col3 = QVBoxLayout()
        self.top.addLayout(self.col1)
        self.top.addLayout(self.col2)
        self.top.addLayout(self.col3)

        self._createDisplay()
        self.Write()
  
    def _createDisplay(self):
        topDisplay = QGridLayout()

        self.text1 = QLineEdit()
        #self.text1.setFixedHeight(DISPLAY_HEIGHT)
        self.text1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.text1.setReadOnly(False)
        topDisplay.addWidget(self.text1)
        
        self.col1.addLayout(topDisplay)

        self.text2 = QLineEdit()
        #self.text2.setFixedHeight(DISPLAY_HEIGHT)
        self.text2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.text2.setReadOnly(False)
        topDisplay.addWidget(self.text2)
        
        self.col1.addLayout(topDisplay)

    def Write(self):
        self.text1.setText(str("V1"))
        self.text2.setText(str("I1, In"))
def main():
    app = QApplication([])
    gui = CN0556_GUI()
    gui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
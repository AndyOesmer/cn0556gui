# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeaderFrame = QFrame(self.centralwidget)
        self.HeaderFrame.setObjectName(u"HeaderFrame")
        self.HeaderFrame.setMaximumSize(QSize(16777215, 60))
        self.HeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.HeaderFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.HeaderFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CheckBoxFrame = QFrame(self.HeaderFrame)
        self.CheckBoxFrame.setObjectName(u"CheckBoxFrame")
        self.CheckBoxFrame.setFrameShape(QFrame.StyledPanel)
        self.CheckBoxFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.CheckBoxFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox = QCheckBox(self.CheckBoxFrame)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_4.addWidget(self.checkBox)


        self.horizontalLayout_3.addWidget(self.CheckBoxFrame)

        self.Mode_Frame = QFrame(self.HeaderFrame)
        self.Mode_Frame.setObjectName(u"Mode_Frame")
        self.Mode_Frame.setFrameShape(QFrame.StyledPanel)
        self.Mode_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Mode_Frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Mode_Label = QLabel(self.Mode_Frame)
        self.Mode_Label.setObjectName(u"Mode_Label")

        self.verticalLayout_8.addWidget(self.Mode_Label)


        self.horizontalLayout_3.addWidget(self.Mode_Frame)

        self.ButtonsFrame = QFrame(self.HeaderFrame)
        self.ButtonsFrame.setObjectName(u"ButtonsFrame")
        self.ButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.ButtonsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.ButtonsFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.StartButton = QPushButton(self.ButtonsFrame)
        self.StartButton.setObjectName(u"StartButton")

        self.horizontalLayout_6.addWidget(self.StartButton)

        self.StopButton = QPushButton(self.ButtonsFrame)
        self.StopButton.setObjectName(u"StopButton")

        self.horizontalLayout_6.addWidget(self.StopButton)


        self.horizontalLayout_3.addWidget(self.ButtonsFrame)

        self.HeaderFrame4 = QFrame(self.HeaderFrame)
        self.HeaderFrame4.setObjectName(u"HeaderFrame4")
        self.HeaderFrame4.setFrameShape(QFrame.StyledPanel)
        self.HeaderFrame4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.HeaderFrame4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.HeaderFrame4)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.HeaderFrame4)


        self.verticalLayout.addWidget(self.HeaderFrame)

        self.TopFrame = QFrame(self.centralwidget)
        self.TopFrame.setObjectName(u"TopFrame")
        self.TopFrame.setFrameShape(QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.TopFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Top1 = QFrame(self.TopFrame)
        self.Top1.setObjectName(u"Top1")
        self.Top1.setFrameShape(QFrame.StyledPanel)
        self.Top1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Top1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Top1_FLabel = QFrame(self.Top1)
        self.Top1_FLabel.setObjectName(u"Top1_FLabel")
        self.Top1_FLabel.setMaximumSize(QSize(16777215, 50))
        self.Top1_FLabel.setFrameShape(QFrame.StyledPanel)
        self.Top1_FLabel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Top1_FLabel)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Top1_Label = QLabel(self.Top1_FLabel)
        self.Top1_Label.setObjectName(u"Top1_Label")

        self.verticalLayout_5.addWidget(self.Top1_Label)


        self.verticalLayout_4.addWidget(self.Top1_FLabel)

        self.Top1_FControl = QFrame(self.Top1)
        self.Top1_FControl.setObjectName(u"Top1_FControl")
        self.Top1_FControl.setFrameShape(QFrame.StyledPanel)
        self.Top1_FControl.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Top1_FControl)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Top1_V1Label = QLabel(self.Top1_FControl)
        self.Top1_V1Label.setObjectName(u"Top1_V1Label")

        self.gridLayout.addWidget(self.Top1_V1Label, 0, 0, 1, 1)

        self.Top1_V1Spin = QDoubleSpinBox(self.Top1_FControl)
        self.Top1_V1Spin.setObjectName(u"Top1_V1Spin")

        self.gridLayout.addWidget(self.Top1_V1Spin, 0, 1, 1, 1)

        self.Top1_VUVLabel = QLabel(self.Top1_FControl)
        self.Top1_VUVLabel.setObjectName(u"Top1_VUVLabel")

        self.gridLayout.addWidget(self.Top1_VUVLabel, 1, 0, 1, 1)

        self.Top1_VUVSpin = QDoubleSpinBox(self.Top1_FControl)
        self.Top1_VUVSpin.setObjectName(u"Top1_VUVSpin")

        self.gridLayout.addWidget(self.Top1_VUVSpin, 1, 1, 1, 1)

        self.Top1_I1PLabel = QLabel(self.Top1_FControl)
        self.Top1_I1PLabel.setObjectName(u"Top1_I1PLabel")

        self.gridLayout.addWidget(self.Top1_I1PLabel, 2, 0, 1, 1)

        self.Top1_I1PSpin = QDoubleSpinBox(self.Top1_FControl)
        self.Top1_I1PSpin.setObjectName(u"Top1_I1PSpin")

        self.gridLayout.addWidget(self.Top1_I1PSpin, 2, 1, 1, 1)

        self.Top1_I1NLabel = QLabel(self.Top1_FControl)
        self.Top1_I1NLabel.setObjectName(u"Top1_I1NLabel")

        self.gridLayout.addWidget(self.Top1_I1NLabel, 3, 0, 1, 1)

        self.Top1_I1NSpin = QDoubleSpinBox(self.Top1_FControl)
        self.Top1_I1NSpin.setObjectName(u"Top1_I1NSpin")

        self.gridLayout.addWidget(self.Top1_I1NSpin, 3, 1, 1, 1)

        self.Top1_PowerLabel = QLabel(self.Top1_FControl)
        self.Top1_PowerLabel.setObjectName(u"Top1_PowerLabel")

        self.gridLayout.addWidget(self.Top1_PowerLabel, 4, 0, 1, 1)

        self.Top1_P = QDoubleSpinBox(self.Top1_FControl)
        self.Top1_P.setObjectName(u"Top1_P")

        self.gridLayout.addWidget(self.Top1_P, 4, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.Top1_FControl)


        self.horizontalLayout.addWidget(self.Top1)

        self.Top2_FMiddle = QFrame(self.TopFrame)
        self.Top2_FMiddle.setObjectName(u"Top2_FMiddle")
        self.Top2_FMiddle.setFrameShape(QFrame.StyledPanel)
        self.Top2_FMiddle.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.Top2_FMiddle)

        self.Top3 = QFrame(self.TopFrame)
        self.Top3.setObjectName(u"Top3")
        self.Top3.setFrameShape(QFrame.StyledPanel)
        self.Top3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Top3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Top3_FLabel = QFrame(self.Top3)
        self.Top3_FLabel.setObjectName(u"Top3_FLabel")
        self.Top3_FLabel.setMaximumSize(QSize(16777215, 50))
        self.Top3_FLabel.setFrameShape(QFrame.StyledPanel)
        self.Top3_FLabel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Top3_FLabel)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Top3_Label = QLabel(self.Top3_FLabel)
        self.Top3_Label.setObjectName(u"Top3_Label")

        self.verticalLayout_7.addWidget(self.Top3_Label)


        self.verticalLayout_6.addWidget(self.Top3_FLabel)

        self.Top3_FControl = QFrame(self.Top3)
        self.Top3_FControl.setObjectName(u"Top3_FControl")
        self.Top3_FControl.setFrameShape(QFrame.StyledPanel)
        self.Top3_FControl.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.Top3_FControl)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Top3_V2Label = QLabel(self.Top3_FControl)
        self.Top3_V2Label.setObjectName(u"Top3_V2Label")

        self.gridLayout_2.addWidget(self.Top3_V2Label, 0, 0, 1, 1)

        self.Top3_V2Spin = QDoubleSpinBox(self.Top3_FControl)
        self.Top3_V2Spin.setObjectName(u"Top3_V2Spin")

        self.gridLayout_2.addWidget(self.Top3_V2Spin, 0, 1, 1, 1)

        self.Top3_VUVLabel = QLabel(self.Top3_FControl)
        self.Top3_VUVLabel.setObjectName(u"Top3_VUVLabel")

        self.gridLayout_2.addWidget(self.Top3_VUVLabel, 1, 0, 1, 1)

        self.Top3_VUVSpin = QDoubleSpinBox(self.Top3_FControl)
        self.Top3_VUVSpin.setObjectName(u"Top3_VUVSpin")

        self.gridLayout_2.addWidget(self.Top3_VUVSpin, 1, 1, 1, 1)

        self.Top3_I2PLabel = QLabel(self.Top3_FControl)
        self.Top3_I2PLabel.setObjectName(u"Top3_I2PLabel")

        self.gridLayout_2.addWidget(self.Top3_I2PLabel, 2, 0, 1, 1)

        self.Top3_I2PSpin = QDoubleSpinBox(self.Top3_FControl)
        self.Top3_I2PSpin.setObjectName(u"Top3_I2PSpin")

        self.gridLayout_2.addWidget(self.Top3_I2PSpin, 2, 1, 1, 1)

        self.Top3_I2NLabel = QLabel(self.Top3_FControl)
        self.Top3_I2NLabel.setObjectName(u"Top3_I2NLabel")

        self.gridLayout_2.addWidget(self.Top3_I2NLabel, 3, 0, 1, 1)

        self.Top3_I2NSpin = QDoubleSpinBox(self.Top3_FControl)
        self.Top3_I2NSpin.setObjectName(u"Top3_I2NSpin")

        self.gridLayout_2.addWidget(self.Top3_I2NSpin, 3, 1, 1, 1)

        self.Top3_PowerLabel = QLabel(self.Top3_FControl)
        self.Top3_PowerLabel.setObjectName(u"Top3_PowerLabel")

        self.gridLayout_2.addWidget(self.Top3_PowerLabel, 4, 0, 1, 1)

        self.Top3_P = QDoubleSpinBox(self.Top3_FControl)
        self.Top3_P.setObjectName(u"Top3_P")

        self.gridLayout_2.addWidget(self.Top3_P, 4, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.Top3_FControl)


        self.horizontalLayout.addWidget(self.Top3)


        self.verticalLayout.addWidget(self.TopFrame)

        self.BottomFrame = QFrame(self.centralwidget)
        self.BottomFrame.setObjectName(u"BottomFrame")
        self.BottomFrame.setFrameShape(QFrame.StyledPanel)
        self.BottomFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.BottomFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Bot1 = QFrame(self.BottomFrame)
        self.Bot1.setObjectName(u"Bot1")
        self.Bot1.setFrameShape(QFrame.StyledPanel)
        self.Bot1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.Bot1)

        self.Bot2 = QFrame(self.BottomFrame)
        self.Bot2.setObjectName(u"Bot2")
        self.Bot2.setFrameShape(QFrame.StyledPanel)
        self.Bot2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.Bot2)

        self.Bot3 = QFrame(self.BottomFrame)
        self.Bot3.setObjectName(u"Bot3")
        self.Bot3.setFrameShape(QFrame.StyledPanel)
        self.Bot3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.Bot3)


        self.verticalLayout.addWidget(self.BottomFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"BOOST (Default: BUCK)", None))
        self.Mode_Label.setText(QCoreApplication.translate("MainWindow", u"MODE: BUCK CONVERTER", None))
        self.StartButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.StopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CN0556", None))
        self.Top1_Label.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.Top1_V1Label.setText(QCoreApplication.translate("MainWindow", u"V1", None))
        self.Top1_VUVLabel.setText(QCoreApplication.translate("MainWindow", u"V1 UV", None))
        self.Top1_I1PLabel.setText(QCoreApplication.translate("MainWindow", u"I1 In P", None))
        self.Top1_I1NLabel.setText(QCoreApplication.translate("MainWindow", u"I1 In N", None))
        self.Top1_PowerLabel.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.Top3_Label.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.Top3_V2Label.setText(QCoreApplication.translate("MainWindow", u"V2", None))
        self.Top3_VUVLabel.setText(QCoreApplication.translate("MainWindow", u"V2 UV", None))
        self.Top3_I2PLabel.setText(QCoreApplication.translate("MainWindow", u"I2 In P", None))
        self.Top3_I2NLabel.setText(QCoreApplication.translate("MainWindow", u"I2 In N", None))
        self.Top3_PowerLabel.setText(QCoreApplication.translate("MainWindow", u"Power", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CN0556_GUI_Design.ui'
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
        MainWindow.resize(1350, 961)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CheckBox_Frame = QFrame(self.frame_2)
        self.CheckBox_Frame.setObjectName(u"CheckBox_Frame")
        self.CheckBox_Frame.setMaximumSize(QSize(255, 16777215))
        self.CheckBox_Frame.setFrameShape(QFrame.Box)
        self.CheckBox_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.CheckBox_Frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox = QCheckBox(self.CheckBox_Frame)
        self.checkBox.setObjectName(u"checkBox")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.checkBox.setFont(font)

        self.horizontalLayout_4.addWidget(self.checkBox)


        self.horizontalLayout_2.addWidget(self.CheckBox_Frame)

        self.Mode_Frame = QFrame(self.frame_2)
        self.Mode_Frame.setObjectName(u"Mode_Frame")
        self.Mode_Frame.setMaximumSize(QSize(280, 16777215))
        self.Mode_Frame.setFrameShape(QFrame.Box)
        self.Mode_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Mode_Frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Mode_Label = QLabel(self.Mode_Frame)
        self.Mode_Label.setObjectName(u"Mode_Label")
        self.Mode_Label.setFont(font)
        self.Mode_Label.setLayoutDirection(Qt.LeftToRight)
        self.Mode_Label.setAutoFillBackground(True)

        self.verticalLayout_8.addWidget(self.Mode_Label)


        self.horizontalLayout_2.addWidget(self.Mode_Frame)

        self.Buttons_Frame = QFrame(self.frame_2)
        self.Buttons_Frame.setObjectName(u"Buttons_Frame")
        self.Buttons_Frame.setMaximumSize(QSize(16777215, 50))
        self.Buttons_Frame.setFrameShape(QFrame.Box)
        self.Buttons_Frame.setFrameShadow(QFrame.Raised)
        self.startButton = QPushButton(self.Buttons_Frame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(11, 11, 121, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMaximumSize(QSize(200, 70))
        font1 = QFont()
        font1.setBold(True)
        self.startButton.setFont(font1)
        self.stopButton = QPushButton(self.Buttons_Frame)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(160, 10, 111, 21))
        self.stopButton.setFont(font1)
        self.resetButton = QPushButton(self.Buttons_Frame)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(296, 11, 121, 21))
        self.resetButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.Buttons_Frame)

        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(200, 16777215))
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label.setFont(font2)

        self.verticalLayout_16.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_14)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 300))
        self.frame_4.setFrameShape(QFrame.Panel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_15)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.V1_Label = QLabel(self.frame_15)
        self.V1_Label.setObjectName(u"V1_Label")
        self.V1_Label.setFont(font1)

        self.verticalLayout_9.addWidget(self.V1_Label)


        self.verticalLayout_4.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame_16)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.V1_SpinBox = QDoubleSpinBox(self.frame_16)
        self.V1_SpinBox.setObjectName(u"V1_SpinBox")

        self.gridLayout.addWidget(self.V1_SpinBox, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.V1uv_SpinBox = QDoubleSpinBox(self.frame_16)
        self.V1uv_SpinBox.setObjectName(u"V1uv_SpinBox")

        self.gridLayout.addWidget(self.V1uv_SpinBox, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.I1P_SpinBox = QDoubleSpinBox(self.frame_16)
        self.I1P_SpinBox.setObjectName(u"I1P_SpinBox")

        self.gridLayout.addWidget(self.I1P_SpinBox, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.I1N_SpinBox = QDoubleSpinBox(self.frame_16)
        self.I1N_SpinBox.setObjectName(u"I1N_SpinBox")

        self.gridLayout.addWidget(self.I1N_SpinBox, 3, 1, 1, 1)

        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.Power1_SpinBox = QDoubleSpinBox(self.frame_16)
        self.Power1_SpinBox.setObjectName(u"Power1_SpinBox")

        self.gridLayout.addWidget(self.Power1_SpinBox, 4, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_16)


        self.horizontalLayout.addWidget(self.frame_6)

        self.ArrowV1_Frame = QFrame(self.frame_4)
        self.ArrowV1_Frame.setObjectName(u"ArrowV1_Frame")
        self.ArrowV1_Frame.setMaximumSize(QSize(60, 16777215))
        self.ArrowV1_Frame.setFrameShape(QFrame.NoFrame)
        self.ArrowV1_Frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.ArrowV1_Frame)

        self.CN0556_IMAG = QFrame(self.frame_4)
        self.CN0556_IMAG.setObjectName(u"CN0556_IMAG")
        self.CN0556_IMAG.setMaximumSize(QSize(400, 16777215))
        self.CN0556_IMAG.setAutoFillBackground(True)
        self.CN0556_IMAG.setFrameShape(QFrame.Box)
        self.CN0556_IMAG.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.CN0556_IMAG)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.CN0556_IMAG)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(48)
        font3.setBold(True)
        self.label_2.setFont(font3)
        self.label_2.setAutoFillBackground(True)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.CN0556_IMAG)

        self.ArrowV2_Frame = QFrame(self.frame_4)
        self.ArrowV2_Frame.setObjectName(u"ArrowV2_Frame")
        self.ArrowV2_Frame.setMaximumSize(QSize(60, 16777215))
        self.ArrowV2_Frame.setFrameShape(QFrame.NoFrame)
        self.ArrowV2_Frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.ArrowV2_Frame)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Box)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_17 = QFrame(self.frame_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.V2_Label = QLabel(self.frame_17)
        self.V2_Label.setObjectName(u"V2_Label")
        self.V2_Label.setFont(font1)

        self.verticalLayout_10.addWidget(self.V2_Label)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_10)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Box)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_18)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_9 = QLabel(self.frame_18)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.V2_SpinBox = QDoubleSpinBox(self.frame_18)
        self.V2_SpinBox.setObjectName(u"V2_SpinBox")

        self.gridLayout_2.addWidget(self.V2_SpinBox, 0, 1, 1, 1)

        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.V2uv_SpinBox = QDoubleSpinBox(self.frame_18)
        self.V2uv_SpinBox.setObjectName(u"V2uv_SpinBox")

        self.gridLayout_2.addWidget(self.V2uv_SpinBox, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.I2P_SpinBox = QDoubleSpinBox(self.frame_18)
        self.I2P_SpinBox.setObjectName(u"I2P_SpinBox")

        self.gridLayout_2.addWidget(self.I2P_SpinBox, 2, 1, 1, 1)

        self.label_12 = QLabel(self.frame_18)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)

        self.I2N_SpinBox = QDoubleSpinBox(self.frame_18)
        self.I2N_SpinBox.setObjectName(u"I2N_SpinBox")

        self.gridLayout_2.addWidget(self.I2N_SpinBox, 3, 1, 1, 1)

        self.label_13 = QLabel(self.frame_18)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.Power2_SpinBox = QDoubleSpinBox(self.frame_18)
        self.Power2_SpinBox.setObjectName(u"Power2_SpinBox")

        self.gridLayout_2.addWidget(self.Power2_SpinBox, 4, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_18)


        self.horizontalLayout.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Panel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_19)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 40))
        self.frame_22.setFrameShape(QFrame.Box)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_22)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_14 = QLabel(self.frame_22)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_14)


        self.verticalLayout_6.addWidget(self.frame_22)

        self.V1_ADC_Graph = QFrame(self.frame_19)
        self.V1_ADC_Graph.setObjectName(u"V1_ADC_Graph")
        self.V1_ADC_Graph.setFrameShape(QFrame.Box)
        self.V1_ADC_Graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.V1_ADC_Graph)

        self.frame_24 = QFrame(self.frame_19)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 40))
        self.frame_24.setFrameShape(QFrame.Box)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_24)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_15 = QLabel(self.frame_24)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_15)


        self.verticalLayout_6.addWidget(self.frame_24)

        self.IMON1_ADC_Graph = QFrame(self.frame_19)
        self.IMON1_ADC_Graph.setObjectName(u"IMON1_ADC_Graph")
        self.IMON1_ADC_Graph.setFrameShape(QFrame.Box)
        self.IMON1_ADC_Graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.IMON1_ADC_Graph)


        self.horizontalLayout_3.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(325, 16777215))
        self.frame_20.setFrameShape(QFrame.Box)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_32 = QFrame(self.frame_20)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 70))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_32)

        self.frame_30 = QFrame(self.frame_20)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(16777215, 300))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_30)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_18 = QLabel(self.frame_30)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.V1_ADC_Value = QLabel(self.frame_30)
        self.V1_ADC_Value.setObjectName(u"V1_ADC_Value")
        self.V1_ADC_Value.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.V1_ADC_Value, 0, 1, 1, 1)

        self.label_19 = QLabel(self.frame_30)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.V2_ADC_Value = QLabel(self.frame_30)
        self.V2_ADC_Value.setObjectName(u"V2_ADC_Value")
        self.V2_ADC_Value.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.V2_ADC_Value, 1, 1, 1, 1)

        self.label_20 = QLabel(self.frame_30)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.gridLayout_3.addWidget(self.label_20, 2, 0, 1, 1)

        self.IMON1_Value = QLabel(self.frame_30)
        self.IMON1_Value.setObjectName(u"IMON1_Value")
        self.IMON1_Value.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.IMON1_Value, 2, 1, 1, 1)

        self.label_21 = QLabel(self.frame_30)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.gridLayout_3.addWidget(self.label_21, 3, 0, 1, 1)

        self.IMON2_Value = QLabel(self.frame_30)
        self.IMON2_Value.setObjectName(u"IMON2_Value")
        self.IMON2_Value.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.IMON2_Value, 3, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_20)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 70))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_31)


        self.horizontalLayout_3.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_5)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_21)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_26 = QFrame(self.frame_21)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 40))
        self.frame_26.setFrameShape(QFrame.Box)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_26)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_16 = QLabel(self.frame_26)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_16)


        self.verticalLayout_7.addWidget(self.frame_26)

        self.V2_ADC_Graph = QFrame(self.frame_21)
        self.V2_ADC_Graph.setObjectName(u"V2_ADC_Graph")
        self.V2_ADC_Graph.setFrameShape(QFrame.Box)
        self.V2_ADC_Graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.V2_ADC_Graph)

        self.frame_28 = QFrame(self.frame_21)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 40))
        self.frame_28.setFrameShape(QFrame.Box)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_28)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_17 = QLabel(self.frame_28)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_17)


        self.verticalLayout_7.addWidget(self.frame_28)

        self.IMON2_ADC_Graph = QFrame(self.frame_21)
        self.IMON2_ADC_Graph.setObjectName(u"IMON2_ADC_Graph")
        self.IMON2_ADC_Graph.setFrameShape(QFrame.Box)
        self.IMON2_ADC_Graph.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.IMON2_ADC_Graph)


        self.horizontalLayout_3.addWidget(self.frame_21)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1350, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"BUCK (Default Unchecked: BOOST)", None))
        self.Mode_Label.setText(QCoreApplication.translate("MainWindow", u"MODE: BOOST CONVERTER", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CN0556", None))
        self.V1_Label.setText(QCoreApplication.translate("MainWindow", u"INPUT", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"V1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"V1 Undervoltage", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"I1 InputP", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"I1 InputN", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Power 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"   CN0556", None))
        self.V2_Label.setText(QCoreApplication.translate("MainWindow", u"OUTPUT", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"V2", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"V2 Undervoltage", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"I2 Input P", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"I2 Input N", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Power 2", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"V1 ADC", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"IMON 1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"V1_ADC", None))
        self.V1_ADC_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"V2_ADC", None))
        self.V2_ADC_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"IMON1", None))
        self.IMON1_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"IMON2", None))
        self.IMON2_Value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"V2 ADC", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"IMON 2", None))
    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 777)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.acceleration = QDoublespinboxAndQSlider(self.centralwidget)
        self.acceleration.setObjectName("acceleration")
        self.verticalLayout.addWidget(self.acceleration)
        self.v_max = QDoublespinboxAndQSlider(self.centralwidget)
        self.v_max.setObjectName("v_max")
        self.verticalLayout.addWidget(self.v_max)
        self.distance = QDoublespinboxAndQSlider(self.centralwidget)
        self.distance.setObjectName("distance")
        self.verticalLayout.addWidget(self.distance)
        self.steps = QDoublespinboxAndQSlider(self.centralwidget)
        self.steps.setObjectName("steps")
        self.verticalLayout.addWidget(self.steps)
        self.decimals = QDoublespinboxAndQSlider(self.centralwidget)
        self.decimals.setObjectName("decimals")
        self.verticalLayout.addWidget(self.decimals)
        self.lead = QDoublespinboxAndQSlider(self.centralwidget)
        self.lead.setObjectName("lead")
        self.verticalLayout.addWidget(self.lead)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plotwidget_ta = PlotWidget(self.centralwidget)
        self.plotwidget_ta.setObjectName("plotwidget_ta")
        self.verticalLayout_2.addWidget(self.plotwidget_ta)
        self.plotwidget_tv = PlotWidget(self.centralwidget)
        self.plotwidget_tv.setObjectName("plotwidget_tv")
        self.verticalLayout_2.addWidget(self.plotwidget_tv)
        self.plotwidget_tx = PlotWidget(self.centralwidget)
        self.plotwidget_tx.setObjectName("plotwidget_tx")
        self.verticalLayout_2.addWidget(self.plotwidget_tx)
        self.plotwidget_trev = PlotWidget(self.centralwidget)
        self.plotwidget_trev.setObjectName("plotwidget_trev")
        self.verticalLayout_2.addWidget(self.plotwidget_trev)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MotorGraph"))
        self.label.setText(_translate("MainWindow", "acceleration type"))
        self.comboBox.setItemText(0, _translate("MainWindow", "trapezoid"))
        self.comboBox.setItemText(1, _translate("MainWindow", "triangle"))
        self.comboBox.setItemText(2, _translate("MainWindow", "parabola"))
from pyqtgraph import PlotWidget
from qdoublespinbox_and_qslider import QDoublespinboxAndQSlider

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import listdevise
import tabset
import os, sys
import threading

class myform22(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.window_height = 300
        self.window_width = 500
        self.setObjectName("menu")

        self.setFixedSize(self.window_height, self.window_width)
        self.setWindowIcon(QIcon('logo1.png'))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.setFont(font)
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.setStyleSheet("background-color: #dce1f7;")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 20, 101, 20))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.listdevise = QtWidgets.QPushButton(self)
        self.listdevise.setFont(font)
        self.listdevise.setObjectName("listdevise")
        self.listdevise.setGeometry(QtCore.QRect(90, 80, 141, 23))
        self.listdevise.clicked.connect(self.Wdev)

        self.listparam = QtWidgets.QPushButton(self)
        self.listparam.setGeometry(QtCore.QRect(90, 140, 141, 23))
        self.listparam.setFont(font)
        self.listparam.setObjectName("listparam")
        self.listparam.clicked.connect(self.Wop)

        self.rezerv = QtWidgets.QPushButton(self)
        self.rezerv.setGeometry(QtCore.QRect(90, 200, 141, 23))

        self.rezerv.setFont(font)
        self.rezerv.setObjectName("rezerv")
        self.exit = QtWidgets.QPushButton(self)
        self.exit.setGeometry(QtCore.QRect(90, 250, 141, 23))

        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(QCoreApplication.instance().quit)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Teco monitoring"))
        self.label.setText(_translate("self", "Your choice"))
        self.listdevise.setText(_translate("self", "List Devise"))
        self.listparam.setText(_translate("self", "Current values"))
        self.rezerv.setText(_translate("self", "Rezerv"))
        self.exit.setText(_translate("self", "Quit"))

    def Wdev(self):
#        print('ok')
        self.ui = listdevise.Widget()
        self.ui.show()

    def Wop(self):
#        print('ok')
        self.ui = tabset.Widget()
        self.ui.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    F2_window = myform22()
    F2_window.show()
    sys.exit(app.exec_())
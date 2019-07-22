from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tkinter
import myform2
from tkinter import messagebox
import os, sys
import threading

class W1(QWidget):
    def __init__(self, parent=None):
        super(W1, self).__init__(parent)

        self.window_height = 300
        self.window_width = 400
        self.setWindowIcon(QIcon('logo1.png'))
        self.setObjectName("Teco")
        self.setFixedSize(self.window_height, self.window_width)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)

        self.enter = QtWidgets.QPushButton(self)
        self.enter.setGeometry(QtCore.QRect(60, 200, 75, 23))
        self.enter.setObjectName("enter")
        self.enter.setToolTip('Next page')
        self.enter.clicked.connect(self.fireupWindows2)

        self.quit = QtWidgets.QPushButton(self)
        self.quit.setGeometry(QtCore.QRect(160, 200, 75, 23))
        self.quit.setObjectName("Quit")
        self.quit.clicked.connect(QCoreApplication.instance().quit)

        self.login = QLineEdit(self)
        self.login.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.login.setObjectName("login")

        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setGeometry(QtCore.QRect(90, 150, 113, 20))
        self.password.setObjectName("password")

        layout = QFormLayout()
        layout.addRow('Login:', self.login)
        layout.addRow('Password:', self.password)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 20, 120, 41))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 141, 41))

        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.setStyleSheet("background-color: #dce1f7;")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Teco Monitoring"))
        self.enter.setText(_translate("self", "Enter"))
        self.quit.setText(_translate("self", "Quit"))
        self.label.setText(_translate("self", "Enter your name:"))
        self.label_2.setText(_translate("self", "Enter your pass:"))

    def fireupWindows2(self):
        root = tkinter.Tk()
        root.withdraw()
        logInZ = "dima"
        passWdZ = '123'
        self.login = self.login.text()
        self.password = self.password.text()
#        print(str(self.login), str(self.password))
        if (self.login in logInZ):
            if (self.password == passWdZ):
                messagebox.showinfo("Hello", self.login)
                self.myformshow()
                self.destroy()

            else:
                messagebox.showerror("Mo Passord")
                self.destroy()
        else:
            messagebox.showerror("No login", self.login)
            self.destroy()

    def myformshow(self):
        self.ui = myform2.myform22()
        self.ui.show()
if __name__ == "__main__":
    main_app = QApplication(sys.argv)
    M_window = W1()
    M_window.show()
    sys.exit(main_app.exec_())
import time
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql.cursors
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

class Widget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.starw()

    def starw(self):
        self.kolstrok = 1
        self.kolst()

        self.window_height = 300
        self.window_width = 400
        self.setFixedSize(self.window_height, self.window_width)
        self.setWindowIcon(QIcon('logo1.png'))
        self.setWindowTitle("Teco monitoring")
        layout = QtWidgets.QVBoxLayout(self)
        btn_layout = QtWidgets.QHBoxLayout()
        btn1 = QtWidgets.QPushButton("Previous")
        btn2 = QtWidgets.QPushButton("Quit")
        btn3 = QtWidgets.QPushButton("Next")
        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        btn_layout.addWidget(btn3)
        btn1.clicked.connect(self.minus)
        btn2.clicked.connect(QCoreApplication.instance().quit)
        btn3.clicked.connect(self.plus)

        self.table = QtWidgets.QTableWidget()
        self.setStyleSheet("""QTableWidget{color: blue;}""")
        self.table.setRowCount(10)
        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels(["Mark", "Devise"])

        header = self.table.horizontalHeader()

        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        layout.addWidget(self.table)
        layout.addLayout(btn_layout)

        self.baza()

    def baza(self):
        db = MySQLdb.connect("1", "d", "I", "teco_app1")
        cursor = db.cursor()
        cursor.execute("select * from list_device  WHERE device_id=" + str(self.kolstrok))
        for dan in cursor.fetchall():
            self.table.setItem(0, 0, QTableWidgetItem("IP"))
            self.table.setItem(0, 1, QTableWidgetItem(str(dan[1])))
            self.table.setItem(1, 0, QTableWidgetItem("mac"))
            self.table.setItem(1, 1, QTableWidgetItem(str(dan[2])))
            self.table.setItem(2, 0, QTableWidgetItem("title"))
            self.table.setItem(2, 1, QTableWidgetItem(str(dan[3])))
            self.table.setItem(3, 0, QTableWidgetItem("geo"))
            self.table.setItem(3, 1, QTableWidgetItem(str(dan[4])))
            self.table.setItem(4, 0, QTableWidgetItem("type"))
            self.table.setItem(4, 1, QTableWidgetItem(str(dan[5])))
            self.table.setItem(5, 0, QTableWidgetItem("view"))
            self.table.setItem(5, 1, QTableWidgetItem(str(dan[6])))
            self.table.setItem(6, 0, QTableWidgetItem("region"))
            self.table.setItem(6, 1, QTableWidgetItem(str(dan[7])))
            self.table.setItem(7, 0, QTableWidgetItem("address"))
            self.table.setItem(7, 1, QTableWidgetItem(str(dan[8])))
            self.table.setItem(8, 0, QTableWidgetItem("info"))
            self.table.setItem(8, 1, QTableWidgetItem(str(dan[9])))
            self.table.setItem(9, 0, QTableWidgetItem("status"))
            self.table.setItem(9, 1, QTableWidgetItem(str(dan[10])))
        cursor.close()

    def kolst(self):
        db = MySQLdb.connect("1", "d", "I", "teco_app1")
        self.kolstrok = 1
        cursor = db.cursor()
        cursor.execute("select count(*) from list_device")
        self.kolnew = str(cursor.fetchone()[0])
        cursor.close()

    def plus(self):
        self.kolstrok = str(self.kolstrok + 1)
        if (self.kolstrok > str(self.kolnew)):
            self.kolstrok = 1
        else:
            self.kolstrok = 2
        self.baza()

    def minus(self):
        self.kolstrok = self.kolstrok - 1
        if (self.kolstrok == 0):
            self.kolstrok = 1
        self.baza()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    w = Widget()
    w.show()
    app.exec()
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
        self.window_width = 700
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
        self.table.setRowCount(20)
        self.table.setColumnCount(2)

        self.table.setHorizontalHeaderLabels(["Mark", "Devise"])
#        self.table.setHorizontalHeaderLabels(QtGui.QColor(0, 255, 0))

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
        cursor.execute("select device_id, ip from list_device  WHERE device_id=" + str(self.kolstrok))
        for row_ip in cursor.fetchall():
            ip = row_ip[1]
            cursor.execute("select * from _data_in_memory  WHERE device_id=" + str(self.kolstrok))
            for dan in cursor.fetchall():
                self.table.setItem(0, 0, QTableWidgetItem("IP"))
#                self.table.item(0, 0).setBackground(QtGui.QColor(150, 205, 205))
                self.table.setItem(0, 1, QTableWidgetItem(str(ip)))
                self.table.setItem(1, 0, QTableWidgetItem("internal temperature C"))
                self.table.setItem(1, 1, QTableWidgetItem(str(dan[2])))
                self.table.setItem(2, 0, QTableWidgetItem("ambient temperature C"))
                self.table.setItem(2, 1, QTableWidgetItem(str(dan[3])))
                self.table.setItem(3, 0, QTableWidgetItem("fan speed"))
                self.table.setItem(3, 1, QTableWidgetItem(str(dan[4])))
                self.table.setItem(4, 0, QTableWidgetItem("air conditioner temp. AC1"))
                self.table.setItem(4, 1, QTableWidgetItem(str(dan[5])))
                self.table.setItem(5, 0, QTableWidgetItem("working hours AC1,hour"))
                self.table.setItem(5, 1, QTableWidgetItem(str(dan[6])))
                self.table.setItem(6, 0, QTableWidgetItem("heater time, hour"))
                self.table.setItem(6, 1, QTableWidgetItem(str(dan[7])))
                self.table.setItem(7, 0, QTableWidgetItem("system time, FC,hour"))
                self.table.setItem(7, 1, QTableWidgetItem(str(dan[8])))
                self.table.setItem(8, 0, QTableWidgetItem("heater, KV hou"))
                self.table.setItem(8, 1, QTableWidgetItem(str(dan[9])))
                self.table.setItem(9, 0, QTableWidgetItem("systems FC, KV hour"))
                self.table.setItem(9, 1, QTableWidgetItem(str(dan[10])))
                self.table.setItem(10, 0, QTableWidgetItem("high temperature"))
                self.table.setItem(10, 1, QTableWidgetItem(str(dan[11])))
                self.table.setItem(11, 0, QTableWidgetItem("system malfunction"))
                self.table.setItem(11, 1, QTableWidgetItem(str(dan[12])))
                self.table.setItem(12, 0, QTableWidgetItem("dirty filter"))
                self.table.setItem(12, 1, QTableWidgetItem(str(dan[13])))
                self.table.setItem(13, 0, QTableWidgetItem("set cooling temperature"))
                self.table.setItem(13, 1, QTableWidgetItem(str(dan[14])))
                self.table.setItem(14, 0, QTableWidgetItem("preset heating temperature"))
                self.table.setItem(14, 1, QTableWidgetItem(str(dan[15])))
                self.table.setItem(15, 0, QTableWidgetItem("emergency switch-on temperature"))
                self.table.setItem(15, 1, QTableWidgetItem(str(dan[16])))
                self.table.setItem(16, 0, QTableWidgetItem("air conditioning, AC1, KV-H"))
                self.table.setItem(16, 1, QTableWidgetItem(str(dan[17])))
                self.table.setItem(17, 0, QTableWidgetItem("fire alarm"))
                self.table.setItem(17, 1, QTableWidgetItem(str(dan[18])))
                self.table.setItem(18, 0, QTableWidgetItem("air conditioner crash AC2"))
                self.table.setItem(18, 1, QTableWidgetItem(str(dan[19])))
                self.table.setItem(19, 0, QTableWidgetItem("air conditioner crash AC1"))
                self.table.setItem(19, 1, QTableWidgetItem(str(dan[20])))




            cursor.close()
        cursor.close()

    def kolst(self):
        db = MySQLdb.connect("10", "d", "I", "teco_app1")
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
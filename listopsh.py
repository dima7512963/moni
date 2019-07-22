from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QMessageBox
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql.cursors
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
 
class Winop(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.kolst()
        self.Bazaset()

    def kolst(self):
        db = MySQLdb.connect("192.168.7.90", "dima", "Ikar7512963", "teco_app1")
#        QMessageBox.about(self, 'Connection', 'Database Connected Successfully')
        self.kolstrok = 1
        cursor = db.cursor()
        cursor.execute("select count(*) from list_device")
        self.kolnew = cursor.fetchone()[0]
        cursor.close()


    def Bazaset(self):
        ip = 0
        self.Winset()

# db------------------------------------------------------------------------------------

        db = MySQLdb.connect("192.168.7.90", "dima", "Ikar7512963", "teco_app1")
        cursor = db.cursor()
        cursor.execute("select device_id, ip from list_device  WHERE device_id=" +str(self.kolstrok))

        for row_ip in cursor.fetchall():
            ip = row_ip[1]
            cursor.execute("select * from _data_in_memory  WHERE device_id=" +str(self.kolstrok))
            self.label.lab = QtWidgets.QLabel(self)
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            self.setFont(font)
            font.setPointSize(10)
            self.label.lab.setFont(font)
            self.label.lab.setGeometry(QtCore.QRect(10, 20, 295, 20))
            self.label.lab.setText("Ip                           " + ip)
#            print('1 ip --', ip)

            for row_dan in cursor.fetchall():

                self.label.lab1 = QtWidgets.QLabel(self)
                self.label.lab1.setGeometry(QtCore.QRect(10, 40, 140, 20))
                self.label.lab1.setText("internal temperature °C")
                self.label.lab11 = QtWidgets.QLabel(self)
                self.label.lab11.setGeometry(QtCore.QRect(160, 40, 100, 20))
                self.label.lab11.setText(row_dan[2])
#                print('2 ip----', row_dan[2])
                self.label.lab2 = QtWidgets.QLabel(self)
                self.label.lab2.setGeometry(QtCore.QRect(10, 55, 140, 20))
                self.label.lab2.setText("ambient temperature °C")
                self.label.lab22 = QtWidgets.QLabel(self)
                self.label.lab22.setGeometry(QtCore.QRect(160, 55, 100, 20))
                self.label.lab22.setText(row_dan[3])
                self.label.lab3 = QtWidgets.QLabel(self)
                self.label.lab3.setGeometry(QtCore.QRect(10, 70, 140, 20))
                self.label.lab3.setText("fan speed")
                self.label.lab33 = QtWidgets.QLabel(self)
                self.label.lab33.setGeometry(QtCore.QRect(160, 70, 100, 20))
                self.label.lab33.setText(row_dan[4])
                self.label.lab4 = QtWidgets.QLabel(self)
                self.label.lab4.setGeometry(QtCore.QRect(10, 85, 140, 20))
                self.label.lab4.setText("air conditioner temp. АС1")
                self.label.lab44 = QtWidgets.QLabel(self)
                self.label.lab44.setGeometry(QtCore.QRect(160, 85, 100, 20))
                self.label.lab44.setText(row_dan[5])
                self.label.lab5 = QtWidgets.QLabel(self)
                self.label.lab5.setGeometry(QtCore.QRect(10, 100, 140, 20))
                self.label.lab5.setText("working hours АС1,hour")
                self.label.lab55 = QtWidgets.QLabel(self)
                self.label.lab55.setGeometry(QtCore.QRect(160, 100, 100, 20))
                self.label.lab55.setText(row_dan[6])
                self.label.lab6 = QtWidgets.QLabel(self)
                self.label.lab6.setGeometry(QtCore.QRect(10, 115, 140, 20))
                self.label.lab6.setText("heater time, hour")
                self.label.lab66 = QtWidgets.QLabel(self)
                self.label.lab66.setGeometry(QtCore.QRect(160, 115, 100, 20))
                self.label.lab66.setText(row_dan[7])
                self.label.lab7 = QtWidgets.QLabel(self)
                self.label.lab7.setGeometry(QtCore.QRect(10, 130, 140, 20))
                self.label.lab7.setText("system time, FC,hour")
                self.label.lab77 = QtWidgets.QLabel(self)
                self.label.lab77.setGeometry(QtCore.QRect(160, 130, 100, 20))
                self.label.lab77.setText(row_dan[8])
                self.label.lab8 = QtWidgets.QLabel(self)
                self.label.lab8.setGeometry(QtCore.QRect(10, 145, 140, 20))
                self.label.lab8.setText("heater, Kv·hour")
                self.label.lab88 = QtWidgets.QLabel(self)
                self.label.lab88.setGeometry(QtCore.QRect(160, 145, 100, 20))
                self.label.lab88.setText(row_dan[9])
                self.label.lab9 = QtWidgets.QLabel(self)
                self.label.lab9.setGeometry(QtCore.QRect(10, 160, 140, 20))
                self.label.lab9.setText("systems FC, Kv·hour")
                self.label.lab99 = QtWidgets.QLabel(self)
                self.label.lab99.setGeometry(QtCore.QRect(160, 160, 100, 20))
                self.label.lab99.setText(row_dan[10])
                self.label.lab10 = QtWidgets.QLabel(self)
                self.label.lab10.setGeometry(QtCore.QRect(10, 175, 140, 20))
                self.label.lab10.setText("high temperature")
                self.label.lab101 = QtWidgets.QLabel(self)
                self.label.lab101.setGeometry(QtCore.QRect(160, 175, 100, 20))
                self.label.lab101.setText(row_dan[11])
                self.label.lab11 = QtWidgets.QLabel(self)
                self.label.lab11.setGeometry(QtCore.QRect(10, 190, 140, 20))
                self.label.lab11.setText("system malfunction")
                self.label.lab111 = QtWidgets.QLabel(self)
                self.label.lab111.setGeometry(QtCore.QRect(160, 190, 100, 20))
                self.label.lab111.setText(row_dan[12])
                self.label.lab12 = QtWidgets.QLabel(self)
                self.label.lab12.setGeometry(QtCore.QRect(10, 205, 140, 20))
                self.label.lab12.setText("dirty filter")
                self.label.lab112 = QtWidgets.QLabel(self)
                self.label.lab112.setGeometry(QtCore.QRect(160, 205, 100, 20))
                self.label.lab112.setText(row_dan[13])
                self.label.lab13 = QtWidgets.QLabel(self)
                self.label.lab13.setGeometry(QtCore.QRect(10, 220, 140, 20))
                self.label.lab13.setText("set cooling temperature")
                self.label.lab113 = QtWidgets.QLabel(self)
                self.label.lab113.setGeometry(QtCore.QRect(160, 220, 100, 20))
                self.label.lab113.setText(row_dan[14])
                self.label.lab14 = QtWidgets.QLabel(self)
                self.label.lab14.setGeometry(QtCore.QRect(10, 235, 140, 20))
                self.label.lab14.setText("preset heating temperature")
                self.label.lab114 = QtWidgets.QLabel(self)
                self.label.lab114.setGeometry(QtCore.QRect(160, 235, 100, 20))
                self.label.lab114.setText(row_dan[15])
                self.label.lab15 = QtWidgets.QLabel(self)
                self.label.lab15.setGeometry(QtCore.QRect(10, 250, 140, 20))
                self.label.lab15.setText("emergency switch-on temperature")
                self.label.lab115 = QtWidgets.QLabel(self)
                self.label.lab115.setGeometry(QtCore.QRect(160, 250, 100, 20))
                self.label.lab115.setText(row_dan[16])
                self.label.lab16 = QtWidgets.QLabel(self)
                self.label.lab16.setGeometry(QtCore.QRect(10, 265, 140, 20))
                self.label.lab16.setText("air conditioning, АС1, Kv·h")
                self.label.lab116 = QtWidgets.QLabel(self)
                self.label.lab116.setGeometry(QtCore.QRect(160, 265, 100, 20))
                self.label.lab116.setText(row_dan[17])
                self.label.lab17 = QtWidgets.QLabel(self)
                self.label.lab17.setGeometry(QtCore.QRect(10, 280, 140, 20))
                self.label.lab17.setText("fire alarm")
                self.label.lab117 = QtWidgets.QLabel(self)
                self.label.lab117.setGeometry(QtCore.QRect(160, 280, 100, 20))
                self.label.lab117.setText(row_dan[18])
                self.label.lab18 = QtWidgets.QLabel(self)
                self.label.lab18.setGeometry(QtCore.QRect(10, 295, 140, 20))
                self.label.lab18.setText("air conditioner crash AC2")
                self.label.lab118 = QtWidgets.QLabel(self)
                self.label.lab118.setGeometry(QtCore.QRect(160, 295, 100, 20))
                self.label.lab118.setText(row_dan[19])
                self.label.lab19 = QtWidgets.QLabel(self)
                self.label.lab19.setGeometry(QtCore.QRect(10, 310, 140, 20))
                self.label.lab19.setText("air conditioner crash AC1")
                self.label.lab119 = QtWidgets.QLabel(self)
                self.label.lab119.setGeometry(QtCore.QRect(160, 310, 100, 20))
                self.label.lab119.setText(row_dan[20])
            cursor.close()
        cursor.close()
#            db.close()
#        sys.exit(1)
# db --------------------------------------------------------------------------------

    def Winset(self):
        self.window_height = 300
        self.window_width = 500
        self.setObjectName("menu")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.setFont(font)
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.setFixedSize(self.window_height, self.window_width)
        self.setWindowIcon(QIcon('logo1.png'))
        self.setWindowTitle("Teco monitoring")
        oImage = QImage("6706.jpg")
        sImage = oImage.scaled(QSize(self.window_height, self.window_width))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.label = QtWidgets.QLabel(self)
        self.label.setFont(font)
        self.label.setGeometry(QtCore.QRect(100, 5, 101, 20))
        self.label.setText("Current values")

        self.previous = QtWidgets.QPushButton(self)
        self.previous.setGeometry(QtCore.QRect(20, 450, 70, 23))
        self.previous.setFont(font)
        self.previous.setObjectName("Previous")
        self.previous.clicked.connect(self.minus)
        self.previous.setText("Previous")

        self.next = QtWidgets.QPushButton(self)
        self.next.setGeometry(QtCore.QRect(200, 450, 70, 23))
        self.next.setFont(font)
        self.next.setObjectName("Next")
        self.next.clicked.connect(self.plus)
        self.next.setText("Next")

    def plus(self):
        self.kolstrok = self.kolstrok + 1
        if (self.kolstrok > self.kolnew):
            self.kolstrok = 1
        else:
            self.kolstrok = 2
        self.Bazaset()

    def minus(self):
        self.kolstrok = self.kolstrok - 1
        if (self.kolstrok == 0):
            self.kolstrok = 1
        self.Bazaset()

# END ------------------------------------------------------------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    F2_window = Winop()
    F2_window.show()
    sys.exit(app.exec_())
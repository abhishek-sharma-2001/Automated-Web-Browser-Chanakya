from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_LoginWindow
from snake_game import *

class Ui_MainWindow(object):
    def gotologin(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def gotobrowser(self):
        from browser_file import Browser
        MainWindow.hide()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1211, 825)
        MainWindow.setStyleSheet("")
        MainWindow.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 1211, 801))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../1.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 900, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0,0,0);")
        self.label_2.setObjectName("label_2")
        self.skipbutton = QtWidgets.QPushButton(MainWindow)
        self.skipbutton.setGeometry(QtCore.QRect(560, 390, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.skipbutton.setFont(font)
        self.skipbutton.clicked.connect(self.gotobrowser)
        self.skipbutton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 255);")
        self.skipbutton.setObjectName("skipbutton")
        self.loginbutton = QtWidgets.QPushButton(MainWindow)
        self.loginbutton.setGeometry(QtCore.QRect(560, 230, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 255);")
        self.loginbutton.setObjectName("loginbutton")
        self.gamebutton = QtWidgets.QPushButton(MainWindow)
        self.loginbutton.clicked.connect(self.gotologin)
        # self.loginbutton.clicked.connect(MainWindow.close)
        self.gamebutton.setGeometry(QtCore.QRect(690, 620, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.gamebutton.setFont(font)
        self.gamebutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0,0,165);")
        self.gamebutton.setObjectName("gamebutton")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.gamebutton.clicked.connect(Snake_game)
        self.label_3.setGeometry(QtCore.QRect(430, 620, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 170, 0);")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.label_2.setText(_translate("MainWindow", "WELCOME TO CHANAKYA BROWSER"))
        self.skipbutton.setText(_translate("MainWindow", "SKIP"))
        self.loginbutton.setText(_translate("MainWindow", "LOGIN"))
        self.gamebutton.setText(_translate("MainWindow", "click here"))
        self.label_3.setText(_translate("MainWindow", "wanna play a game?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import time
import statistics
from statistics import mode
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
global emailid
# emailid = self.email_2.text()
def call_browser(emailid):
    # print(emailid)
    # emailid = self.email_2.text()
    # exec(open('browser_file.py').read())
    
    from browser_file import user_values
    user_values(emailid)
    from browser_file import Browser
    # # emailid = self.email_2.text()
    # from browser_file import MainWindow
    # self.message = "hii rahul"
    # LoginWindow.hide()
    # # from browser_file import MainWindow

class Ui_LoginWindow(object):



    def show_invalidpass(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Enter email and password !")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    def show_info(self):
        msg = QMessageBox()
        msg.setWindowTitle("Welcome")
        msg.setText("Login Successful")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    def show_nouser(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Enter valid email and password !")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
    def database_login(self):
        if len(self.password_2.text()) <= 1:
            self.show_invalidpass()

        else:
            emailid = self.email_2.text()
            password = self.password_2.text()

            conn = sqlite3.connect('userinfo.db')
            cursor = conn.cursor()

            cursor.execute("SELECT emailid,password FROM user")
            val = cursor.fetchall()

            if len(val) >= 1:
                for x in val:
                    if emailid in x[0] and password in x[1]:
                        self.show_info()
                        call_browser(emailid)
                        break
                        # return emailid
                else:
                    self.show_nouser()
            # else:
                # self.show_nouser()

    def gotomainwindow(self):
        from mainwindow import Ui_MainWindow
        self.window = QtWidgets.QDialog()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def gotocreateacc(self):
        from signup import  Ui_SignupWindow
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_SignupWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def gotoeditfav(self):
        from edit_favourite import  Ui_EditfavWindow
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_EditfavWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def gotoforgotpass(self):
        from forgot_pass import Ui_ForgotWindow
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_ForgotWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(565, 694)
        LoginWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.Login = QtWidgets.QLabel(LoginWindow)
        self.Login.setGeometry(QtCore.QRect(200, 40, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Login.setFont(font)
        self.Login.setStyleSheet("color: rgb(238, 238, 238);\n"
"font: 28pt \"Helvetica\";\n"
"")
        self.Login.setAlignment(QtCore.Qt.AlignCenter)
        self.Login.setObjectName("Login")
        self.email = QtWidgets.QLabel(LoginWindow)
        self.email.setGeometry(QtCore.QRect(40, 190, 71, 41))
        self.email.setStyleSheet("font: 15pt \"Verdana\";\n"
"color: rgb(255, 0, 255);")
        self.email.setObjectName("email")
        self.email_2 = QtWidgets.QLineEdit(LoginWindow)
        self.email_2.setGeometry(QtCore.QRect(190, 180, 281, 51))
        self.email_2.setStyleSheet("font: 12pt \"Verdana\";\n"
"color: rgb(240, 240, 240);")
        self.email_2.setText("")
        self.email_2.setObjectName("email_2")
        self.password = QtWidgets.QLabel(LoginWindow)
        self.password.setGeometry(QtCore.QRect(40, 300, 121, 61))
        self.password.setStyleSheet("font: 15pt \"Verdana\";\n"
"color: rgb(255, 0, 255);")
        self.password.setObjectName("password")
        self.password_2 = QtWidgets.QLineEdit(LoginWindow)
        self.password_2.setGeometry(QtCore.QRect(190, 300, 281, 51))
        self.password_2.setStyleSheet("font: 12pt \"Verdana\";\n"
"color: rgb(240, 240, 240);")
        self.password_2.setText("")
        self.password_2.setObjectName("password_2")
        self.loginbutton = QtWidgets.QPushButton(LoginWindow)
        self.loginbutton.clicked.connect(self.database_login)
        self.loginbutton.clicked.connect(LoginWindow.close)
        self.loginbutton.setGeometry(QtCore.QRect(330, 560, 151, 51))
        self.loginbutton.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 14pt \"Verdana\";")
        self.loginbutton.setObjectName("loginbutton")
        self.backlogin = QtWidgets.QPushButton(LoginWindow)
        self.backlogin.setGeometry(QtCore.QRect(70, 560, 151, 51))
        self.backlogin.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 14pt \"Verdana\";")
        self.backlogin.setObjectName("backlogin")
        self.createacc = QtWidgets.QPushButton(LoginWindow)
        self.backlogin.clicked.connect(self.gotomainwindow)
        self.backlogin.clicked.connect(LoginWindow.close)
        self.createacc.setGeometry(QtCore.QRect(380, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.createacc.setFont(font)
        self.createacc.setStyleSheet("color: rgb(254, 254, 254);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 75 8pt \"Verdana\";")
        self.createacc.setObjectName("createacc")
        self.label_3 = QtWidgets.QLabel(LoginWindow)
        self.createacc.clicked.connect(self.gotocreateacc)
        self.createacc.clicked.connect(LoginWindow.close)
        self.label_3.setGeometry(QtCore.QRect(180, 390, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(231, 231, 231);")
        self.label_3.setObjectName("label_3")
        self.editfavbtn = QtWidgets.QPushButton(LoginWindow)
        self.editfavbtn.setGeometry(QtCore.QRect(330, 470, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.editfavbtn.setFont(font)
        self.editfavbtn.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 12pt \"Verdana\";")
        self.editfavbtn.setObjectName("editfavbtn")
        self.forgotpassbtn = QtWidgets.QPushButton(LoginWindow)
        self.editfavbtn.clicked.connect(self.gotoeditfav)
        self.editfavbtn.clicked.connect(LoginWindow.close)
        self.forgotpassbtn.setGeometry(QtCore.QRect(70, 470, 151, 51))
        self.forgotpassbtn.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 10pt \"Verdana\";")
        self.forgotpassbtn.setObjectName("forgotpassbtn")
        self.forgotpassbtn.clicked.connect(self.gotoforgotpass)
        self.forgotpassbtn.clicked.connect(LoginWindow.close)
        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Dialog"))
        self.Login.setToolTip(_translate("LoginWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Login</span></p></body></html>"))
        self.Login.setWhatsThis(_translate("LoginWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.Login.setText(_translate("LoginWindow", "Login"))
        self.email.setText(_translate("LoginWindow", "Email"))
        self.password.setText(_translate("LoginWindow", "Password"))
        self.loginbutton.setText(_translate("LoginWindow", "Login"))
        self.backlogin.setText(_translate("LoginWindow", "Back"))
        self.createacc.setText(_translate("LoginWindow", "SIGN UP"))
        self.label_3.setText(_translate("LoginWindow", "Don\'t have an acccount?"))
        self.editfavbtn.setText(_translate("LoginWindow", "Edit Favourite"))
        self.forgotpassbtn.setText(_translate("LoginWindow", "Forgot Password?"))


if __name__== "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QDialog()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
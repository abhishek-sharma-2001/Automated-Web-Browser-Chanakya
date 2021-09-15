from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox


class Ui_ForgotWindow(object):
    def show_invalidemail(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Enter a email !")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    def show_forgot(self):
        msg = QMessageBox()
        msg.setWindowTitle("Load")
        msg.setText("Load Successful")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    def show_noemail(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("email connot be found")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
    def load_pass(self):
        emailid = self.email_6.text()
        conn = sqlite3.connect('userinfo.db')
        cursor = conn.cursor()

        pas=cursor.execute("SELECT password FROM user where emailid=?",(emailid,))
        pas = str(cursor.fetchone())
        convertpas=pas.translate({ord(i): None for i in ",('')"})

        self.email_3.setText(convertpas)

    def database_forgot(self):
        if len(self.email_6.text()) <= 1:
            self.show_invalidemail()

        else:
            emailid = self.email_6.text()

            conn = sqlite3.connect('userinfo.db')
            cursor = conn.cursor()

            cursor.execute("SELECT emailid FROM user ")
            val = cursor.fetchall()

            if len(val) >= 1:
                for x in val:
                    if emailid in x[0] :
                        self.load_pass()
                        self.show_forgot()
                        break
                else:
                    self.show_noemail()
            # else:
            #     self.show_noemail()

    def gotologin(self):
        from login import  Ui_LoginWindow
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, ForgotWindow):
        ForgotWindow.setObjectName("ForgotWindow")
        ForgotWindow.resize(537, 679)
        ForgotWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(ForgotWindow)
        self.label.setGeometry(QtCore.QRect(120, 40, 311, 51))
        self.label.setStyleSheet("font: 75 24pt \"Helveticar\";\n"
"color: rgb(235, 235, 235);")
        self.label.setObjectName("label")
        self.loadbtn = QtWidgets.QPushButton(ForgotWindow)
        self.loadbtn.setGeometry(QtCore.QRect(70, 280, 151, 51))
        self.loadbtn.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 14pt \"Verdana\";")
        self.loadbtn.setObjectName("loadbtn")
        self.email_4 = QtWidgets.QLabel(ForgotWindow)
        self.loadbtn.clicked.connect(self.database_forgot)
        self.email_4.setGeometry(QtCore.QRect(70, 130, 121, 41))
        self.email_4.setStyleSheet("font: 15pt \"Verdana\";\n"
"color: rgb(255, 0, 255);")
        self.email_4.setObjectName("email_4")
        self.email_6 = QtWidgets.QLineEdit(ForgotWindow)
        self.email_6.setGeometry(QtCore.QRect(70, 200, 371, 51))
        self.email_6.setStyleSheet("font: 12pt \"Verdana\";\n"
"color: rgb(240, 240, 240);")
        self.email_6.setText("")
        self.email_6.setObjectName("email_6")
        self.email_3 = QtWidgets.QLineEdit(ForgotWindow)
        self.email_3.setGeometry(QtCore.QRect(70, 450, 381, 51))
        self.email_3.setStyleSheet("font: 12pt \"Verdana\";\n"
"color: rgb(240, 240, 240);")
        self.email_3.setText("")
        self.email_3.setObjectName("email_3")
        self.email_5 = QtWidgets.QLabel(ForgotWindow)
        self.email_5.setGeometry(QtCore.QRect(70, 380, 121, 41))
        self.email_5.setStyleSheet("font: 15pt \"Verdana\";\n"
"color: rgb(255, 0, 255);")
        self.email_5.setObjectName("email_5")
        self.backforgotbtn = QtWidgets.QPushButton(ForgotWindow)
        self.backforgotbtn.setGeometry(QtCore.QRect(70, 550, 151, 51))
        self.backforgotbtn.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 14pt \"Verdana\";")
        self.backforgotbtn.setObjectName("backforgotbtn")
        self.backforgotbtn.clicked.connect(self.gotologin)
        self.backforgotbtn.clicked.connect(ForgotWindow.close)

        self.retranslateUi(ForgotWindow)
        QtCore.QMetaObject.connectSlotsByName(ForgotWindow)

    def retranslateUi(self, ForgotWindow):
        _translate = QtCore.QCoreApplication.translate
        ForgotWindow.setWindowTitle(_translate("ForgotWindow", "Dialog"))
        self.label.setText(_translate("ForgotWindow", "Forgot Password"))
        self.loadbtn.setText(_translate("ForgotWindow", "LOAD"))
        self.email_4.setText(_translate("ForgotWindow", "Email"))
        self.email_5.setText(_translate("ForgotWindow", "Password"))
        self.backforgotbtn.setText(_translate("ForgotWindow", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotWindow = QtWidgets.QDialog()
    ui = Ui_ForgotWindow()
    ui.setupUi(ForgotWindow)
    ForgotWindow.show()
    sys.exit(app.exec_())

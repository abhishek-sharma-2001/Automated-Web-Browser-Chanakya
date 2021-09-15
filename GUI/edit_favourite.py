from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Ui_EditfavWindow(object):
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
    def show_confirm(self):
        msg = QMessageBox()
        msg.setWindowTitle("Load")
        msg.setText("Update Successful")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
    def show_noemail(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("email connot be found")
        msg.setIcon(QMessageBox.Question)
        msg.exec_()
    def show_noload(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Please fill valid email !")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
    def load_pass(self):
        global emailid
        emailid = self.email_6.text()
        conn = sqlite3.connect('userinfo.db')
        cursor = conn.cursor()

        pas=cursor.execute("SELECT favourite1 FROM user where emailid=?",(emailid,))
        pas = str(cursor.fetchone())
        convertpas=pas.translate({ord(i): None for i in ",('')"})

        self.email_3.setText(convertpas)
        cursor.close()
        conn.close()
        conn = sqlite3.connect('userinfo.db')
        cursor = conn.cursor()

        pas=cursor.execute("SELECT favourite2 FROM user where emailid=?",(emailid,))
        pas = str(cursor.fetchone())
        convertpas=pas.translate({ord(i): None for i in ",('')"})

        self.email_8.setText(convertpas)

    def database_check(self):
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
                    if emailid in x[0]:
                        self.load_pass()
                        self.show_forgot()
                        break
                else:
                    self.show_noemail()


    def database_update(self):
        if self.email_6.text() == '':
            self.show_noload()
        else:
            emailid = self.email_6.text()
            txt_fav1 = self.email_3.text()
            txt_fav2 = self.email_8.text()

            conn = sqlite3.connect('userinfo.db')
            cursor = conn.cursor()
            cursor.execute("Update user set favourite1 = ? where emailid = ? ",(txt_fav1,emailid))
            cursor.execute("Update user set favourite2 = ? where emailid = ?  ",(txt_fav2,emailid))
            conn.commit()
            cursor.close()
            conn.close()

            self.show_confirm()
            self.email_3.setText("")
            self.email_8.setText("")


    def gotologin(self):
        from login import Ui_LoginWindow
        self.window = QtWidgets.QDialog()
        self.ui =  Ui_LoginWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, EditfavWindow):
        EditfavWindow.setObjectName("EditfavWindow")
        EditfavWindow.resize(562, 679)
        EditfavWindow.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(EditfavWindow)
        self.label.setGeometry(QtCore.QRect(160, 50, 241, 41))
        self.label.setStyleSheet("font: 75 24pt \"Helveticar\";\n"
"color: rgb(235, 235, 235);")
        self.label.setObjectName("label")
        self.loginbutton = QtWidgets.QPushButton(EditfavWindow)
        self.loginbutton.setGeometry(QtCore.QRect(340, 230, 151, 51))
        self.loginbutton.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 14pt \"Verdana\";")
        self.loginbutton.setObjectName("loginbutton")
        self.email_4 = QtWidgets.QLabel(EditfavWindow)
        self.loginbutton.clicked.connect(self.database_check)
        self.email_4.setGeometry(QtCore.QRect(40, 130, 81, 41))
        self.email_4.setStyleSheet("font: 15pt \"Verdana\";\n"
"color: rgb(255, 0, 255);")
        self.email_4.setObjectName("email_4")
        self.email_6 = QtWidgets.QLineEdit(EditfavWindow)
        self.email_6.setGeometry(QtCore.QRect(160, 130, 371, 51))
        self.email_6.setStyleSheet("font: 12pt \"Verdana\";\n"
"color: rgb(240, 240, 240);")
        self.email_6.setText("")
        self.email_6.setObjectName("email_6")
        self.email_3 = QtWidgets.QLineEdit(EditfavWindow)
        self.email_3.setGeometry(QtCore.QRect(150, 340, 381, 51))
        self.email_3.setStyleSheet("font: 12pt \"Verdana\";\n"
"color: rgb(240, 240, 240);")
        self.email_3.setText("")
        self.email_3.setObjectName("email_3")
        self.email_7 = QtWidgets.QLabel(EditfavWindow)
        self.email_7.setGeometry(QtCore.QRect(80, 430, 31, 41))
        self.email_7.setStyleSheet("font: 15pt \"Verdana\";\n"
"color: rgb(255, 0, 255);")
        self.email_7.setObjectName("email_7")
        self.email_5 = QtWidgets.QLabel(EditfavWindow)
        self.email_5.setGeometry(QtCore.QRect(80, 340, 31, 41))
        self.email_5.setStyleSheet("font: 15pt \"Verdana\";\n"
"color: rgb(255, 0, 255);")
        self.email_5.setObjectName("email_5")
        self.email_8 = QtWidgets.QLineEdit(EditfavWindow)
        self.email_8.setGeometry(QtCore.QRect(150, 430, 381, 51))
        self.email_8.setStyleSheet("font: 12pt \"Verdana\";\n"
"color: rgb(240, 240, 240);")
        self.email_8.setText("")
        self.email_8.setObjectName("email_8")
        self.loginbutton_2 = QtWidgets.QPushButton(EditfavWindow)
        self.loginbutton_2.clicked.connect(self.database_update)
        self.loginbutton_2.setGeometry(QtCore.QRect(340, 550, 151, 51))
        self.loginbutton_2.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 14pt \"Verdana\";")
        self.loginbutton_2.setObjectName("loginbutton_2")
        self.backfavbtn = QtWidgets.QPushButton(EditfavWindow)
        self.backfavbtn.setGeometry(QtCore.QRect(80, 550, 151, 51))
        self.backfavbtn.setStyleSheet("color: rgb(244, 244, 244);\n"
"background-color: rgb(153, 153, 153);\n"
"font: 14pt \"Verdana\";")
        self.backfavbtn.setObjectName("backfavbtn")
        self.backfavbtn.clicked.connect(self.gotologin)
        self.backfavbtn.clicked.connect(EditfavWindow.close)

        self.retranslateUi(EditfavWindow)
        QtCore.QMetaObject.connectSlotsByName(EditfavWindow)

    def retranslateUi(self, EditfavWindow):
        _translate = QtCore.QCoreApplication.translate
        EditfavWindow.setWindowTitle(_translate("EditfavWindow", "Dialog"))
        self.label.setText(_translate("EditfavWindow", "Edit Favourite"))
        self.loginbutton.setText(_translate("EditfavWindow", "LOAD"))
        self.email_4.setText(_translate("EditfavWindow", "Email"))
        self.email_7.setText(_translate("EditfavWindow", "2."))
        self.email_5.setText(_translate("EditfavWindow", "1."))
        self.loginbutton_2.setText(_translate("EditfavWindow", "UPDATE"))
        self.backfavbtn.setText(_translate("EditfavWindow", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditfavWindow = QtWidgets.QDialog()
    ui = Ui_EditfavWindow()
    ui.setupUi(EditfavWindow)
    EditfavWindow.show()
    sys.exit(app.exec_())

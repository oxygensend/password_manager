from PyQt5 import QtCore, QtGui, QtWidgets
from psycopg2.errors import UniqueViolation


class Ui_Generate_Password(object):

    def __init__(self, Form, widget, pm):
        self.setupUi(Form)
        self.Form = Form
        self.widget = widget
        self.pm = pm

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 603)
        self.app_line = QtWidgets.QLineEdit(Form)
        self.app_line.setGeometry(QtCore.QRect(50, 50, 231, 31))
        self.app_line.setObjectName("app_line")
        self.email_line = QtWidgets.QLineEdit(Form)
        self.email_line.setGeometry(QtCore.QRect(50, 140, 231, 31))
        self.email_line.setObjectName("email_line")
        self.user_line = QtWidgets.QLineEdit(Form)
        self.user_line.setGeometry(QtCore.QRect(50, 230, 231, 31))
        self.user_line.setObjectName("user_line")
        self.password_line = QtWidgets.QLineEdit(Form)
        self.password_line.setGeometry(QtCore.QRect(50, 320, 231, 31))
        self.password_line.setObjectName("password_line")
        self.website_line = QtWidgets.QLineEdit(Form)
        self.website_line.setGeometry(QtCore.QRect(50, 410, 231, 31))
        self.website_line.setObjectName("website_line")
        self.length_line = QtWidgets.QLineEdit(Form)
        self.length_line.setGeometry(QtCore.QRect(50, 500, 231, 31))
        self.length_line.setObjectName("length_line")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 211, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 221, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 211, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 231, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 380, 141, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 470, 141, 20))
        self.label_6.setObjectName("label_6")
        self.submit_button = QtWidgets.QPushButton(Form)
        self.submit_button.setGeometry(QtCore.QRect(450, 470, 191, 51))
        self.submit_button.setObjectName("submit_button")
        self.submit_button.clicked.connect(self.submit_event)

        self.label_output = QtWidgets.QLabel(Form)
        self.label_output.setGeometry(QtCore.QRect(450, 60, 341, 161))
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(450, 540, 191, 51))
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(self.back_event)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter application name"))
        self.label_2.setText(_translate("Form", "Address email for this account"))
        self.label_3.setText(_translate("Form", "Enter username(if needed)"))
        self.label_4.setText(_translate("Form", "Enter easy password to hash"))
        self.label_5.setText(_translate("Form", "Enter website link"))
        self.label_6.setText(_translate("Form", "Enter password length(default 10)"))
        self.submit_button.setText(_translate("Form", "sumbit"))
        self.back_button.setText(_translate("Form", "back"))

    def check_lines(self):

        return 1 if self.app_line.text() and self.email_line.text() \
        and self.password_line.text() else 0

    def back_event(self):
        self.widget.setCurrentIndex(0)

    def clear_lines(self):

        self.email_line.clear()
        self.website_line.clear()
        self.app_line.clear()
        self.password_line.clear()
        self.user_line.clear()
        self.length_line.clear()

    def submit_event(self):
            
        msg = QtWidgets.QMessageBox()
        if  not self.check_lines:
            QtWidgets.QMessageBox.warning(msg,"","EROR",QtWidgets.QMessageBox.Ok)
            return
        
        if not self.user_line.text():
            self.user_line.setText('')

        if not self.length_line.text():
            self.length_line.setText('10')

        try:
            result = self.pm.generate_password(self.app_line.text(), self.email_line.text(),
                                  self.password_line.text(), self.user_line.text(),
                                  self.website_line.text(), int(self.length_line.text()))
        
            self.label_output.setText(f'Your password for this account is {result}')

            answer = QtWidgets.QMessageBox.question(msg,"",
                                        "Record inserted.\nYour password is: "+result+"\nDo you mind enter another account?",
                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            
            if answer == QtWidgets.QMessageBox.Yes:
                    #msg.exec_()
                    self.clear_lines()
                    self.label_output.setText('')
            else:
                    #msg.exec_()
               self.back_event()
            
            

        except UniqueViolation:
                    QtWidgets.QMessageBox.warning(msg, 
                                    "ERROR", 
                                    "Entry all needed data",
                                    QtWidgets.QMessageBox.Ok)


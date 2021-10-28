from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Generate_Password(object):

    def __init__(self, Form, widget):
        self.setupUi(Form)
        self.Form = Form
        self.widget = widget

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
        self.submit_button = QtWidgets.QPushButton(Form)
        self.submit_button.setGeometry(QtCore.QRect(70, 470, 191, 51))
        self.submit_button.setObjectName("submit_button")
        self.label_output = QtWidgets.QLabel(Form)
        self.label_output.setGeometry(QtCore.QRect(360, 60, 341, 161))
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(70, 540, 191, 51))
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
        self.submit_button.setText(_translate("Form", "sumbit"))
        self.back_button.setText(_translate("Form", "back"))

    def back_event(self):
        self.widget.setCurrentIndex(0)

    def submit_event(self):
        pass

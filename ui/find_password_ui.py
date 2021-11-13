from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Find_Password(object):

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
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 211, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 221, 20))
        self.label_2.setObjectName("label_2")
        self.submit_button = QtWidgets.QPushButton(Form)
        self.submit_button.setGeometry(QtCore.QRect(70, 470, 191, 51))
        self.submit_button.setObjectName("submit_button")
        self.submit_button.clicked.connect(self.submit_event)
        
        
        
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

        self.submit_button.setText(_translate("Form", "sumbit"))
        self.back_button.setText(_translate("Form", "back"))

    def back_event(self):
        self.widget.setCurrentIndex(0)


    def check_lines(self):

        return 1  if self.email_line and self.app_line else 0   
        
    def clean_lines(self):
        
        self.email_line.clear()
        self.app_line.clear()

    def submit_event(self):
        
        msg = QtWidgets.QMessageBox()
        msg.setGeometry(QtCore.QRect(450,300,200,300))

        if  not self.check_lines:
            QtWidgets.QMessageBox.warning(msg,"","EROR",QtWidgets.QMessageBox.Ok)
            return

        result = self.pm.find_password(self.app_line.text(), self.email_line.text())

        if result:
            self.label_output.setText("This is your password for this account: " + result[0])
        else:
            self.label_output.setText("There is no data in DB with entered parameters")

    
      
        self.clean_lines()
      

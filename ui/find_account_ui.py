from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Find_Accounts():

    def __init__(self, Form, widget):
        self.setupUi(Form)
        self.Form = Form
        self.widget = widget

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 603)
      
        self.email_line = QtWidgets.QLineEdit(Form)
        self.email_line.setGeometry(QtCore.QRect(50, 50, 231, 31))
        self.email_line.setObjectName("email_line")
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 20, 211, 20))
        self.label.setObjectName("label")
        
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
        self.label.setText(_translate("Form", "Address email for this account"))

        self.submit_button.setText(_translate("Form", "sumbit"))
        self.back_button.setText(_translate("Form", "back"))

    def back_event(self):
        self.widget.setCurrentIndex(0)

    def submit_event(self):
        pass
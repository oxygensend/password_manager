# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from generate_password_ui import Ui_Generate_Password
from find_password_ui import Ui_Find_Password
from change_password_ui import Ui_Change_Password
from find_account_ui import Ui_Find_Accounts
from store_new_account_ui import  Ui_New_Account
from delete_account_ui import Ui_Delete_Account

class Ui_MenuWindow(object):

     
    def __init__(self, MainWindow, Form, Form_gp, Form_cp, Form_fp, Form_fa, Form_da, widget):

        self.setupUi(MainWindow)
        self.ui_new_account = Ui_New_Account(Form, widget)
        self.ui_generate_passsword = Ui_Generate_Password(Form_gp, widget)
        self.ui_find_password = Ui_Find_Password(Form_fp, widget)
        self.ui_change_password = Ui_Change_Password(Form_cp, widget)
        self.ui_find_accounts = Ui_Find_Accounts(Form_fa, widget)
        self.ui_delete_account = Ui_Delete_Account(Form_da, widget)
        self.Form_na = Form
        self.Form_gp = Form_gp
        self.Form_fp = Form_fp
        self.Form_cp = Form_cp
        self.Form_fa = Form_fa
        self.Form_da = Form_da
        self.widget = widget
        self.widget.addWidget(MainWindow)
        self.widget.addWidget(self.Form_na)
        self.widget.addWidget(self.Form_gp)
        self.widget.addWidget(self.Form_cp)
        self.widget.addWidget(self.Form_fp)
        self.widget.addWidget(self.Form_fa)
        self.widget.addWidget(self.Form_da)

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 90, 251, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_event)



        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 160, 251, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.generate_event)


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 230, 251, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.change_password_event)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 300, 251, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.find_password_event)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 370, 251, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.find_accounts_event)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 440, 251, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.delete_account_event)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 22))
        self.menubar.setObjectName("menubar")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuedit.addAction(self.actioncopy)
        self.menuedit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuedit.menuAction())
        self.menuedit.setObjectName("menuedit")

        
        MainWindow.setMenuBar(self.menubar)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Add existing account"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate password"))
        self.pushButton_3.setText(_translate("MainWindow", "Change password"))
        self.pushButton_4.setText(_translate("MainWindow", "Find password"))
        self.pushButton_5.setText(_translate("MainWindow", "Find all accounts connected to email"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete account"))
        self.menuedit.setTitle(_translate("MainWindow", "Edit"))
        self.actioncopy.setText(_translate("MainWindow", "Copy"))
        self.actioncopy.setStatusTip(_translate("MainWindow", "Copy text"))
        self.actioncopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Paste text"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))


   
    def add_event(self):
       
       
      self.widget.setCurrentIndex(self.widget.indexOf(self.Form_na))

    def generate_event(self):

        self.widget.setCurrentIndex(self.widget.indexOf(self.Form_gp))

    def change_password_event(self):

        self.widget.setCurrentIndex(self.widget.indexOf(self.Form_cp))

    def find_password_event(self):

        self.widget.setCurrentIndex(self.widget.indexOf(self.Form_fp))

    def find_accounts_event(self):
        
        self.widget.setCurrentIndex(self.widget.indexOf(self.Form_fa))

    def delete_account_event(self):
        
        self.widget.setCurrentIndex(self.widget.indexOf(self.Form_da))
#    MenuWindow = QtWidgets.QMainWindow()




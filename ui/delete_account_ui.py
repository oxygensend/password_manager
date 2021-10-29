from PyQt5 import QtCore, QtGui, QtWidgets
from find_password_ui import Ui_Find_Password


class Ui_Delete_Account(Ui_Find_Password):

    def __init__(self, Form, widget, pm):
        super().__init__(Form, widget, pm)



    def submit_event(self):
        
        msg = QtWidgets.QMessageBox()
        if  not self.check_lines:
            QtWidgets.QMessageBox.warning(msg,"","EROR",QtWidgets.QMessageBox.Ok)
            return



        answer = QtWidgets.QMessageBox.question(msg,"",
          "Are you sure?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if answer == QtWidgets.QMessageBox.Yes:

            result = self.pm.delete_account(self.app_line.text(), self.email_line.text())
            self.label_output.setText("Account delete from DB")
        else:
            self.clean_lines()
            return

    
        answer = QtWidgets.QMessageBox.question(msg,"",
          " Do you want try again?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if answer == QtWidgets.QMessageBox.Yes:            
        
            self.clean_lines()
        
        else:
            #msg.exec_()
            self.back_event()


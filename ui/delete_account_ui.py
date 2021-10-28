from PyQt5 import QtCore, QtGui, QtWidgets
from find_password_ui import Ui_Find_Password


class Ui_Delete_Account(Ui_Find_Password):

    def __init__(self, Form, widget):
        super().__init__(Form, widget)
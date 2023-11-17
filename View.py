from PyQt5 import QtWidgets, QtGui
from login.login_UDEA import Ui_Form
from PyQt5.QtWidgets import QMessageBox


class LoginWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, model):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.model = model

    def show_error_message(self):
        QMessageBox.warning(self, 'Error', 'Las credenciales son incorrectas')

from PyQt5 import QtWidgets
from login.login_UDEA import Ui_Form
from PyQt5.QtWidgets import QMessageBox
from content.dicom_interfaz import Ui_MainWindow


class LoginWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, model):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.model = model

    def show_error_message(self):
        QMessageBox.warning(self, 'Error', 'Las credenciales son incorrectas')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

from PyQt5.QtWidgets import QMessageBox, QWidget, QMainWindow
from PyQt5.uic import loadUi


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('login/login_UDEA.ui', self)
        self.setup()

    def setup(self):
        self.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        continue_login = self.controller.recieve_login_data(username, password)
        if continue_login:
            self.close()
            self.main_window = MainWindow()
            self.main_window.show()
        else:
            self.show_error_message()

    def show_error_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Usuario y/o contraseña incorrectos")
        msg.exec_()

    def assing_controller(self, controller):
        self.controller = controller


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('content/dicom_interfaz.ui', self)
        self.setup()

    def setup(self):
        pass

    def assing_controller(self, controller):
        self.controller = controller

from PyQt5 import QtWidgets
from login.login_UDEA import Ui_Form


class LoginWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self, model):
        super(LoginWindow, self).__init__()
        self.setupUi(self)  # Este método se genera automáticamente con pyuic5 y configura todos los widgets de la interfaz de usuario
        self.model = model
        self.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if self.model.verify_credentials(username, password):
            # Si las credenciales son correctas, puedes abrir la ventana de la imagen DICOM
            print("Las credenciales son correctas")
        else:
            print("Las credenciales son incorrectas")

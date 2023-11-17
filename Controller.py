from Model import User
from View import LoginWindow
import sys
from PyQt5.QtWidgets import QApplication


class Controller:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.model = User('medicoAnalitico', 'bio12345')
        self.view = LoginWindow(self.model)
        self.view.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.view.lineEdit.text()
        password = self.view.lineEdit_2.text()
        if self.model.verify_credentials(username, password):
            print("Las credenciales son correctas")
        else:
            print("Las credenciales son incorrectas")

    def run(self):
        self.view.show()
        sys.exit(self.app.exec_())


def main():
    controller = Controller()
    controller.run()


if __name__ == '__main__':
    main()

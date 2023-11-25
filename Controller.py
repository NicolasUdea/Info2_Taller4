from Model import User
from View import LoginWindow
from PyQt5.QtWidgets import QApplication
import sys


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def recieve_login_data(self, username, password):
        return self.model.verify_credentials(username, password)

    def get_images(self, images):
        data = self.model.load_folder(images)
        return data

    def handle_folder_path(self, path):
        return self.model.load_folder(path)


def main():
    app = QApplication(sys.argv)
    my_view = LoginWindow()
    my_model = User('medicoAnalitico', 'bio12345')
    my_controller = Controller(my_view, my_model)  # Corregido aquí
    my_view.assing_controller(my_controller)
    my_view.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

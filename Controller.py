from Model import User, DICOMImage
from View import LoginWindow, MainWindow
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QFileDialog, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
import os
import sys


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
            self.view.close()
            self.view = MainWindow()
            self.view.pushButton_4.clicked.connect(self.cargarImagenes)
            self.view.verticalSlider.valueChanged.connect(
                self.cambiarImagen)
            self.view.show()
            self.cargarImagenes()
        else:
            self.view.show_error_message()

    def cargarImagenes(self):
        self.carpeta = QFileDialog.getExistingDirectory(self.view, "Cargar Archivo")
        if self.carpeta:
            self.archivos_dicom = [f for f in os.listdir(self.carpeta) if f.endswith(".dcm")]
            self.view.verticalSlider.setMaximum(len(self.archivos_dicom) - 1)

    def cambiarImagen(self, valor):
        try:
            archivo_dicom = DICOMImage(os.path.join(self.carpeta, self.archivos_dicom[valor]))
            archivo_dicom.load_image()
            archivo_dicom.extract_metadata()

            # Convertir la imagen DICOM en un QPixmap
            image = archivo_dicom.image  # Asegúrate de que esto devuelve un array de numpy
            height, width = image.shape
            bytes_per_line = width
            image = QImage(image.data, width, height, bytes_per_line, QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(image)
            self.view.centralwidget.body.main_body.dicom_ima.label_dmt.setScaledContents(True)

            # Establecer el QPixmap en el QLabel
            self.view.centralwidget.body.main_body.dicom_ima.label_dmt.setPixmap(pixmap)

        except Exception as e:
            print(f"Error: {e}")

    def run(self):
        self.view.show()
        sys.exit(self.app.exec_())


def main():
    controller = Controller()
    controller.run()


if __name__ == '__main__':
    main()

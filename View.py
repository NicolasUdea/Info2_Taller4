from PyQt5.QtWidgets import QMessageBox, QWidget, QMainWindow, QFileDialog, QSlider, QLabel
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pydicom


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
            self.main_window.assing_controller(self.controller)
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
        self.slider = self.findChild(QSlider, "verticalSlider")
        self.setup()

    def setup(self):
        self.graphicator = MyGraphCanvas(self.dicom_img)
        self.load_folder.clicked.connect(self.open_directory_dialog)
        self.slider.valueChanged.connect(self.slider_moved)
        self.set_dicom_info()

    def open_directory_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.images = self.controller.handle_folder_path(folder_path)
        self.slider.setMaximum(len(self.images) - 1)  # Set the maximum value of the slider
        self.display_dicom_image()

    def display_dicom_image(self):
        """Displays a DICOM image on the QLabel dicom_img."""
        self.graphicator.graphicate(self.images[self.slider.value()])

    def slider_moved(self):
        self.display_dicom_image()  # Update the image when the slider is moved

    def assing_controller(self, controller):
        self.controller = controller

    def set_dicom_info(self):
        label_names = ["label", "label_2", "label_3", "label_4", "label_5"]
        dicom_file_test = pydicom.dcmread("data/1-001.dcm")
        for name in label_names:
            if name == "label":
                self.findChild(QLabel, name).setText("PatientID: " + dicom_file_test.PatientID)
            elif name == "label_2":
                self.findChild(QLabel, name).setText("StudyDate: " + dicom_file_test.StudyDate)
            elif name == "label_3":
                self.findChild(QLabel, name).setText("Modality: " + dicom_file_test.Modality)
            elif name == "label_4":
                self.findChild(QLabel, name).setText("Manufacturer: " + dicom_file_test.Manufacturer)
            elif name == "label_5":
                self.findChild(QLabel, name).setText("BodyPartExamined: " + dicom_file_test.BodyPartExamined)


class MyGraphCanvas(FigureCanvas):
    def __init__(self, layout=None, parent=None, width=20, height=20, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, self.fig)
        layout.addWidget(self)

    def graphicate(self, image):
        self.fig.clf()
        self.axes = self.fig.add_subplot(1, 1, 1)
        self.axes.imshow(image["image"], cmap="gray")
        self.axes.set_title(image["name"])
        self.axes.figure.tight_layout()
        self.axes.figure.canvas.draw()

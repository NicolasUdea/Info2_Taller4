import matplotlib.pyplot as plt
from Model import DICOMImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
from PyQt5.QtCore import Qt


class ImageDisplay(QMainWindow):
    def __init__(self, image_list, slider_controller):
        super().__init__()
        self.image_list = image_list
        self.slider_controller = slider_controller
        self.initUI()

    def initUI(self):
        """Initializes the user interface."""
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('DICOM Image Viewer')

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(200, 550, 400, 30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(len(self.image_list) - 1)
        self.slider.valueChanged[int].connect(self.changeValue)

        self.show()

    def changeValue(self, value):
        """Updates the displayed image when the slider value changes."""
        self.slider_controller.current_value = value
        self.show_current_image()

    def show_current_image(self):
        """Displays the current image based on the slider's value."""
        plt.imshow(self.image_list[self.slider_controller.current_value], cmap=plt.cm.bone)
        plt.show()


class MockSliderController:
    def __init__(self):
        self.current_value = 0
        self.max_value = 0

    def increment(self):
        pass

    def decrement(self):
        pass


import os
import numpy as np

# Define the path to the folder containing your DICOM files
folder_path = 'data/'

# Get a list of all DICOM files in the folder
file_names = os.listdir(folder_path)
dicom_files = [os.path.join(folder_path, file_name) for file_name in file_names if file_name.endswith('.dcm')]

# Create a DICOMImage object for each file and load the image data
image_list = []
for dicom_file in dicom_files:
    dicom_image = DICOMImage(dicom_file)
    dicom_image.load_image()
    image_list.append(dicom_image.image)

app = QApplication([])
slider_controller = MockSliderController()
image_display = ImageDisplay(image_list, slider_controller)
app.exec_()


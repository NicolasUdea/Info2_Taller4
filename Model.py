from PyQt5.QtGui import QImage
import numpy as np
import pydicom
import os


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__images = None

    def verify_credentials(self, input_username, input_password):
        return self.__username == input_username and self.__password == input_password

    def load_image(self, path: str):
        if path.endswith('.dcm'):
            file = pydicom.dcmread(path)
            image = file.pixel_array
            return image, file
        else:
            return None, None

    def load_folder(self, folder_path: str):
        """Loads a folder of DICOM images."""
        image_list = []
        for path in os.listdir(folder_path):
            image, file = self.load_image(folder_path + '/' + path)
            metadata = self.extract_metadata(file)
            image_list.append({"name": path, "metadata": metadata, "image": image})

        print(image_list[0]["image"].shape)
        return image_list

    def extract_metadata(self, dicom_file):
        """Extracts the metadata from the DICOM file."""
        self._metadata = {
            'PatientID': dicom_file.PatientID,
            'StudyDate': dicom_file.StudyDate,
            'Modality': dicom_file.Modality,
            'Manufacturer': dicom_file.Manufacturer,
            'BodyPartExamined': dicom_file.BodyPartExamined,
        }

#    @property
#    def return_images(self):
#        return self.__images


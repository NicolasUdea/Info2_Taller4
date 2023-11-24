from PyQt5.QtGui import QImage
import numpy as np
import pydicom
import os


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def verify_credentials(self, input_username, input_password):
        return self.__username == input_username and self.__password == input_password


class DICOMImage:
    def __init__(self):
        self.__file_path = ""
        self._metadata = None
        self.__image = None

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
            image_list.append({"name": path, "file": file, "image": image})

    def extract_metadata(self):
        """Extracts the metadata from the DICOM file."""
        dicom_file = pydicom.dcmread(self.__file_path)
        self._metadata = {
            'PatientID': dicom_file.PatientID,
            'StudyDate': dicom_file.StudyDate,
            'Modality': dicom_file.Modality,
            'Manufacturer': dicom_file.Manufacturer,
            'BodyPartExamined': dicom_file.BodyPartExamined,
        }

    @property
    def metadata(self):
        return self._metadata

    @property
    def image(self):
        return self.__image


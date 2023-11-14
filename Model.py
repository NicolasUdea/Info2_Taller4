import pydicom


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def verify_credentials(self, input_username, input_password):
        return self.__username == input_username and self.__password == input_password


user = User('medicoAnalitico', 'bio12345')
print(user.verify_credentials('medicoAnalitico', 'bio12345'))  # prints: True
print(user.verify_credentials('wrongUsername', 'wrongPassword'))  # prints: False


class DICOMImage:
    def __init__(self, file_path):
        self.__file_path = file_path
        self._metadata = None
        self.__image = None

    def load_image(self):
        """Loads the image data from the DICOM file."""
        dicom_file = pydicom.dcmread(self.__file_path)
        self.__image = dicom_file.pixel_array

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


dicom_image = DICOMImage('data/1-001.dcm')
dicom_image.load_image()
dicom_image.extract_metadata()
print(dicom_image.metadata)  # prints the extracted metadata

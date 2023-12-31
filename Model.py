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
        files = os.listdir(folder_path)
        if files:
            # Extract metadata from the first file
            _, first_file = self.load_image(folder_path + '/' + files[0])
            metadata = self.extract_metadata(first_file)

            for path in files:
                image, _ = self.load_image(folder_path + '/' + path)
                image_list.append({"name": path, "metadata": metadata, "image": image})

        return image_list

    def extract_metadata(self, dicom_file):
        """Extracts the metadata from the DICOM file."""
        metadata_dicom = {
            'PatientID': dicom_file.PatientID,
            'StudyDate': dicom_file.StudyDate,
            'Modality': dicom_file.Modality,
            'Manufacturer': dicom_file.Manufacturer,
            'BodyPartExamined': dicom_file.BodyPartExamined,
        }
        return metadata_dicom

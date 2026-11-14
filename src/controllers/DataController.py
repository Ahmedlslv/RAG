from .BaseControllers import BaseController
from fastapi import UploadFile
from models import ResponseSignal

class DataController(BaseController):

    def __init__(self):
        super().__init__()

        self.size_scale = 1024 * 1024  # convert MB to bytes
        self.Max_size = self.app_settings.FILE_MAX_SIZE

    def validate_uploaded_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size is None:
            return False, ResponseSignal.FILE_SIZE_UNKNOWN.value

        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, f"file_size({round(file.size/self.size_scale, 2)}MB) excedded {self.Max_size}MB limt"

        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value

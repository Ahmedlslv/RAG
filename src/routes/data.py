from fastapi import FastAPI, APIRouter, Depends ,UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):
    
    # validate the file properties 
    
    is_valid, resault_signal = DataController().validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            content={
                "signal": resault_signal
                },
            status_code=status.HTTP_400_BAD_REQUEST
        )
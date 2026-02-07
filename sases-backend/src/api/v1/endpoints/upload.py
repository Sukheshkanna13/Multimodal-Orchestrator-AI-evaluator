from fastapi import APIRouter, File, UploadFile
from typing import List

router = APIRouter()

@router.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    Endpoint to upload files.
    """
    uploaded_files = []
    for file in files:
        contents = await file.read()
        # Here you can process the file contents as needed
        uploaded_files.append({"filename": file.filename, "content_size": len(contents)})
    
    return {"uploaded_files": uploaded_files}
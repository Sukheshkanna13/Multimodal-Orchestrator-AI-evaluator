from fastapi import APIRouter, UploadFile, File, HTTPException
from src.services.alignment import align_images

router = APIRouter()

@router.post("/align")
async def align_endpoint(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    try:
        aligned_image = await align_images(file)
        return {"message": "Image aligned successfully", "aligned_image": aligned_image}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import APIRouter
from .endpoints import upload, align, evaluate

router = APIRouter()

router.include_router(upload.router, prefix="/upload", tags=["upload"])
router.include_router(align.router, prefix="/align", tags=["align"])
router.include_router(evaluate.router, prefix="/evaluate", tags=["evaluate"])
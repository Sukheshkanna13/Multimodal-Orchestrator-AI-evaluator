from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.ocr import evaluate_answers

router = APIRouter()

class EvaluationRequest(BaseModel):
    aligned_image: str  # Base64 encoded image or image path
    answer_key: list    # List of correct answers

class EvaluationResponse(BaseModel):
    score: float
    details: dict

@router.post("/evaluate", response_model=EvaluationResponse)
async def evaluate(request: EvaluationRequest):
    try:
        score, details = evaluate_answers(request.aligned_image, request.answer_key)
        return EvaluationResponse(score=score, details=details)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
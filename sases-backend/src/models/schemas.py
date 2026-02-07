from pydantic import BaseModel
from typing import List, Optional

class ImageSchema(BaseModel):
    id: str
    url: str
    processed: bool

class EvaluationResult(BaseModel):
    question_id: str
    detected_answer: str
    correct_answer: str
    score: float

class TemplateMapSchema(BaseModel):
    question_id: str
    coordinates: List[int]  # [x_start, y_start, x_end, y_end]

class UploadResponse(BaseModel):
    message: str
    image: ImageSchema

class AlignmentResponse(BaseModel):
    message: str
    aligned_image_url: str

class EvaluationResponse(BaseModel):
    results: List[EvaluationResult]
    total_score: float
    max_score: float
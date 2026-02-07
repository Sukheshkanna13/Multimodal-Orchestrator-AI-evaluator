import pytest
from src.api.v1.endpoints.evaluate import evaluate_answers

def test_evaluate_answers_correct():
    # Simulate input for correct answers
    aligned_image = "path/to/aligned_image.jpg"
    expected_result = {"score": 3.0, "details": "All answers correct."}
    
    result = evaluate_answers(aligned_image)
    
    assert result == expected_result

def test_evaluate_answers_incorrect():
    # Simulate input for incorrect answers
    aligned_image = "path/to/aligned_image_incorrect.jpg"
    expected_result = {"score": 1.5, "details": "Some answers incorrect."}
    
    result = evaluate_answers(aligned_image)
    
    assert result == expected_result

def test_evaluate_answers_unanswered():
    # Simulate input for unanswered questions
    aligned_image = "path/to/aligned_image_unanswered.jpg"
    expected_result = {"score": 0.0, "details": "No answers provided."}
    
    result = evaluate_answers(aligned_image)
    
    assert result == expected_result

def test_evaluate_answers_invalid_image():
    # Simulate input for an invalid image
    aligned_image = "path/to/invalid_image.jpg"
    
    with pytest.raises(ValueError):
        evaluate_answers(aligned_image)
import pytest
from src.services.alignment import align_images

def test_align_images():
    # Test case for aligning two images
    template_image_path = 'tests/test_images/template.jpg'
    student_image_path = 'tests/test_images/student.jpg'
    expected_output_path = 'tests/test_images/aligned_output.jpg'

    aligned_image = align_images(template_image_path, student_image_path)

    # Save the aligned image for verification
    aligned_image.save(expected_output_path)

    # Load the expected output for comparison
    expected_output = Image.open(expected_output_path)

    # Assert that the aligned image matches the expected output
    assert aligned_image == expected_output, "The aligned image does not match the expected output."
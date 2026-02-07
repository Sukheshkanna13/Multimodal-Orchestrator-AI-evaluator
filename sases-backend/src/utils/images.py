def load_image(image_path):
    """Load an image from the specified path."""
    import cv2
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
    return image

def save_image(image, save_path):
    """Save an image to the specified path."""
    import cv2
    success = cv2.imwrite(save_path, image)
    if not success:
        raise IOError(f"Failed to save image at path: {save_path}")

def resize_image(image, width, height):
    """Resize the image to the specified width and height."""
    import cv2
    return cv2.resize(image, (width, height))

def convert_to_grayscale(image):
    """Convert the image to grayscale."""
    import cv2
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def normalize_image(image):
    """Normalize the image to have pixel values between 0 and 1."""
    return image / 255.0
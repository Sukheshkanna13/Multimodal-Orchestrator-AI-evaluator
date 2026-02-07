from fastapi import HTTPException
import cv2
import numpy as np

def align_images(template_img: np.ndarray, scanned_img: np.ndarray) -> np.ndarray:
    if template_img is None or scanned_img is None:
        raise HTTPException(status_code=400, detail="Images must not be None")

    height, width = template_img.shape[:2]
    center = (width // 2, height // 2)

    # SIMULATION: Rotation, Scaling, and Translation
    angle = 7  # Example rotation angle
    scale = 1.08  # Example scale
    translation_x = 50  # Example translation

    # Rotation and Scaling Matrix
    M_rot = cv2.getRotationMatrix2D(center, angle, scale)
    M_rot[0, 2] += translation_x
    M_rot[1, 2] += 20  # Small vertical shift

    # Apply distortion
    distorted_img = cv2.warpAffine(scanned_img, M_rot, (width, height), borderMode=cv2.BORDER_REPLICATE)

    # Convert to grayscale for feature matching
    template_gray = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    distorted_gray = cv2.cvtColor(distorted_img, cv2.COLOR_BGR2GRAY)

    # Feature matching using ORB
    orb = cv2.ORB_create(nfeatures=5000)
    kp_template, des_template = orb.detectAndCompute(template_gray, None)
    kp_distorted, des_distorted = orb.detectAndCompute(distorted_gray, None)

    if des_template is None or des_distorted is None:
        raise HTTPException(status_code=400, detail="Could not find sufficient features for alignment.")

    # Match features
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des_template, des_distorted)
    matches = sorted(matches, key=lambda x: x.distance)[:300]  # Use top 300 matches

    # Extract location of keypoints
    src_pts = np.float32([kp_template[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp_distorted[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    # Find the Homography matrix for perspective transformation
    M, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

    # Apply the transformation to align the scanned image
    aligned_img = cv2.warpPerspective(distorted_img, M, (width, height))

    return aligned_img
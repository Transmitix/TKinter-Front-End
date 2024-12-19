import cv2
import numpy as np

def calculate_error_rate(image1_path, image2_path):
    img1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Check if images have the same dimensions
    if img1.shape != img2.shape:
        print("The images have changed dimensions")
        return None

    # Calculate the number of differing pixels
    error_pixels = np.sum(img1 != img2)
    total_pixels = img1.size

    # Calculate the percentage of error
    error_rate = (error_pixels / total_pixels) * 100

    return error_rate

# Example usage
image1_path = '/home/thevinduk/Transmitix/Main/2.Image/jpeg/Test4.jpeg'
image2_path = '/home/thevinduk/Transmitix/Main/2.Image/jpeg/output_no_pre_no_del.jpeg'
error_rate = calculate_error_rate(image1_path, image2_path)
print(f"Error Rate: {error_rate:.2f}%")
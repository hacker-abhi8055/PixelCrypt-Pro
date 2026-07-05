import os
import cv2
import numpy as np


class ImageAnalyzer:
    """
    Analyze image properties and statistics.
    """

    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)

        if self.image is None:
            raise FileNotFoundError(f"Unable to load image: {image_path}")

    def analyze(self):

        height, width, channels = self.image.shape

        total_pixels = width * height

        file_size = os.path.getsize(self.image_path) / 1024

        mean_blue = np.mean(self.image[:, :, 0])
        mean_green = np.mean(self.image[:, :, 1])
        mean_red = np.mean(self.image[:, :, 2])

        return {
            "File Name": os.path.basename(self.image_path),
            "Width": width,
            "Height": height,
            "Channels": channels,
            "Total Pixels": total_pixels,
            "Aspect Ratio": round(width / height, 2),
            "Image Size (KB)": round(file_size, 2),
            "Average Red": round(mean_red, 2),
            "Average Green": round(mean_green, 2),
            "Average Blue": round(mean_blue, 2),
            "Data Type": self.image.dtype,
        }
import cv2
import os


class ImageLoader:
    """
    Responsible for loading and validating images.
    """

    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = None

    def load_image(self):
        """
        Load image from disk.
        """
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Image not found: {self.image_path}")

        self.image = cv2.imread(self.image_path)

        if self.image is None:
            raise ValueError("Failed to load image.")

        return self.image

    def get_image_info(self):
        """
        Return image information.
        """
        if self.image is None:
            raise ValueError("Load image first.")

        height, width, channels = self.image.shape

        return {
            "Width": width,
            "Height": height,
            "Channels": channels,
            "Data Type": self.image.dtype,
        }

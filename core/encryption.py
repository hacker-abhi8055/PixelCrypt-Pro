import cv2
import numpy as np


class EncryptionEngine:

    def __init__(self, key=123):
        self.key = key

    def encrypt(self, image):

        encrypted = np.bitwise_xor(image, self.key)

        return encrypted

    def save(self, image, output_path):

        cv2.imwrite(output_path, image)
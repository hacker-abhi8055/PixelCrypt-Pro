"""
-----------------------------------------------------
PixelCrypt Pro

Encryption Service

Author : Abhishek Biradar

Version : 2.0
-----------------------------------------------------
"""

from core.image_loader import ImageLoader
from core.image_analyzer import ImageAnalyzer
from core.encryption import EncryptionEngine
from utils.logger import logger


class EncryptionService:
    """
    Coordinates the image encryption workflow.
    """

    def __init__(self, image_path: str):

        self.image_path = image_path

        self.loader = ImageLoader(image_path)

        self.analyzer = ImageAnalyzer(image_path)

        self.engine = EncryptionEngine()

    def execute(self):

        logger.info("Encryption Service Started")

        self.loader.load_image()

        image_info = self.loader.get_image_info()

        analysis = self.analyzer.analyze()

        encrypted = self.engine.encrypt(self.loader.image)

        output_path = "images/encrypted/encrypted_test.png"

        self.engine.save(
            encrypted,
            output_path
        )

        logger.info("Encryption Service Finished")

        return {
            "image_info": image_info,
            "analysis": analysis,
            "output": output_path
        }
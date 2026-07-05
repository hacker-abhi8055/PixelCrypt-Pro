from core.image_loader import ImageLoader
from core.image_analyzer import ImageAnalyzer
from core.encryption import EncryptionEngine
from utils.logger import logger


def main():
    logger.info("Application Started")

    print("=" * 50)
    print("        PixelCrypt Pro v1.0")
    print("=" * 50)

    image_path = "images/original/test.jpg"

    # -----------------------------
    # Load Image
    # -----------------------------
    loader = ImageLoader(image_path)
    loader.load_image()

    logger.info("Image Loaded Successfully")

    info = loader.get_image_info()

    print("\nIMAGE INFORMATION\n")

    for key, value in info.items():
        print(f"{key}: {value}")

    # -----------------------------
    # Analyze Image
    # -----------------------------
    analyzer = ImageAnalyzer(image_path)

    report = analyzer.analyze()

    logger.info("Image Analysis Completed")

    print("\n" + "=" * 50)
    print("IMAGE ANALYSIS REPORT")
    print("=" * 50)

    for key, value in report.items():
        print(f"{key}: {value}")

    # -----------------------------
    # Encrypt Image
    # -----------------------------
    logger.info("Encryption Started")

    engine = EncryptionEngine()

    encrypted_image = engine.encrypt(loader.image)

    output_path = "images/encrypted/encrypted_test.png"

    engine.save(encrypted_image, output_path)

    logger.info("Encrypted Image Saved")

    print("\n" + "=" * 50)
    print("IMAGE ENCRYPTION")
    print("=" * 50)
    print("Image Encrypted Successfully!")
    print(f"Saved at : {output_path}")

    logger.info("Application Finished")


if __name__ == "__main__":
    main()
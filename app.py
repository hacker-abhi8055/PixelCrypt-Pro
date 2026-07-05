from core.image_loader import ImageLoader


def main():
    print("=" * 50)
    print("      PixelCrypt Pro v1.0")
    print("=" * 50)

    image_path = "images/original/test.jpg"

    loader = ImageLoader(image_path)

    loader.load_image()

    info = loader.get_image_info()

    print("\nImage Loaded Successfully!\n")

    for key, value in info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
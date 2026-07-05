from core.image_loader import ImageLoader

loader = ImageLoader("images/original/test.jpg")

image = loader.load_image()

info = loader.get_image_info()

print("\n===== IMAGE INFO =====")

for key, value in info.items():
    print(f"{key}: {value}")

import os
import PIL.Image

input_dir = "C:/Users/Вероника/Desktop/Исходные изображения"

output_dir = "C:/Users/Вероника/Desktop/Обработанные изображения"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if not filename.endswith(".jpg") and not filename.endswith(".png"):
        continue

    image_path = os.path.join(input_dir, filename)
    image = PIL.Image.open(image_path)

    image = image.resize((image.width // 2, image.height // 2))

    output_path = os.path.join(output_dir, filename)
    image.save(output_path)

    print(f"Обработано изображение: {filename}")

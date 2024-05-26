from PIL import Image, ImageDraw, ImageFont

image = Image.open("C:\Users\User\Desktop\открытка.jpg")
im_crop = image.crop((100, 75, 300, 150))
name = input("Введите имя того, кого хотите поздравить: ")

draw = ImageDraw.Draw(im_crop)
font = ImageFont.truetype("arial.ttf", 36)
color = (255, 255, 0)
position = (im_crop.width // 2 - 100, im_crop.height // 2 - 100)
draw.text(position, f"{name}, поздравляю!", font=font, fill=color)
new_filename = f"открытка2_{name}.png"
im_crop.save(new_filename, quality=95)

print(f"Новая открытка сохранена в файл {new_filename}.")

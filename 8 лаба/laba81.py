from PIL import Image

image = Image.open("C:\Users\User\Desktop\открытка.jpg")
im_crop = im.crop((100, 75, 300, 150))
im_crop.save('открытка2.jpg', quality=95)

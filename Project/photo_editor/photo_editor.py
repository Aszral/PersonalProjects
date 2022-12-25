from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./edited_photos"
path_Out = "./unedited_photos"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN)
    clean_name = os.path.splitext(filename)[0]
    edit.save(f".{path_Out}/{clean_name}_edited.jpg")

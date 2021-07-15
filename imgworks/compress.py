from PIL import Image
import os

def compress(img_path, quality: int):
    img = Image.open(img_path)

    output_dir, img_name = os.path.split(img_path)

    if not os.path.exists(output_dir + r"\output"):
        os.makedirs(output_dir + r"\output")

    output_path = output_dir + r"\output" + "\\" + img_name

    img.save(output_path, optimize=True, quality=quality)
    return output_path, img.size
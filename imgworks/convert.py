from PIL import Image
import glob
import os


def convert(img_path, req_format):

    output_dir = os.path.split(img_path)+r"\output"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = Image.open(img_path)
    out_path = output_dir + '\\' + os.path.splitext(os.path.basename(img_path))[0] + "." + req_format
    img.save(out_path, optimize=False)

def folder_convert_img(folder_path,req_format):

    output_dir = folder_path+r"\output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    formats = ['*.jpg','*.png',"*.jpeg","*.raw","*.svg"]
    for format in formats:
        for photo in glob.glob(os.path.join(folder_path, format)):
            img = Image.open(photo)
            out_path = output_dir + '\\' + os.path.splitext(os.path.basename(photo))[0] + "." + req_format
            img.save(out_path, optimize=False)

def folder_convert_pdf(folder_path, filename):

    img_list = []
    formats = ['*.jpg', '*.png', "*.jpeg", "*.raw", "*.svg"]
    for format in formats:
        for photo in glob.glob(os.path.join(folder_path, format)):
            img_list.append(Image.open(photo))

    cover = img_list.pop(0)
    file_path = os.path.join(folder_path,filename+".pdf")
    cover.save(file_path,"PDF", resolution=100.0, save_all=True, append_images=img_list)
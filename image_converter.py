from PIL import Image
import os
import sys

images = sys.argv[1]
path = r"C:\Devang\Python\PycharmProjects\Udemy_Course\venv\\" + f'{images}'
file_list = os.listdir(path)
parent_dir = r"C:\Devang\Python\PycharmProjects\Udemy_Course\venv\\"
dir_path = os.path.join(parent_dir, sys.argv[2])
for image in file_list:
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        pass
    temp = image.split('.')
    image_png = f'{temp[0]}' + '.png'
    with open(f'{dir_path}\\{image_png}', 'w') as my_dir:
        img = Image.open(image)
        img.save(image_png, 'png')

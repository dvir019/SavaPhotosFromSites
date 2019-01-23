from os import path, listdir

image_extensions = [".png", ".jpg", ".gif", 'bmp']

def get_images_by_folder(folder):
    images = []
    return __recursive_get_images_by_folder(folder, images)

def __recursive_get_images_by_folder(folder, images):
    for f in listdir(folder):
        try:
            full_path=path.join(folder, f)
            if path.isdir(full_path):
                __recursive_get_images_by_folder(full_path, images)
            elif path.isfile(full_path):
                file_name, file_extension = path.splitext(f)
                if file_extension in image_extensions and full_path not in images:
                    images.append(full_path)
        except WindowsError:  # If access was denied
            pass
    return images


from shutil import copyfile
#copyfile(r"C:\Users\Horim\Desktop\tic3.gif", r"C:\Users\Horim\Desktop\checkadd\tic3.gif")
print path.split(r"C:\Users\Horim\Desktop\tic3.gif")
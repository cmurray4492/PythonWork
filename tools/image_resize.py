# this script resizes images in a directory to a specified size

import os
from PIL import Image


def resize_images(directory, target_size=(96, 96)):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            with Image.open(filepath) as img:
                # Resize the image if it's not already the target size
                if img.size != target_size:
                    img = img.resize(target_size)
                    img.save(filepath)
                    print(f"Resized: {filename}")
                else:
                    print(f"Kept: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


# Replace 'path_to_directory' with your actual directory containing images
directory = r'C:\Users\South\Downloads\kagglecatsanddogs_5340\PetImages\Dog'
# print(directory)
resize_images(directory)

"""
The script below could be used to develop a delete script.

import os
from PIL import Image

def filter_images(directory, target_size=(96, 96)):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        try:
            with Image.open(filepath) as img:
                if img.size != target_size:
                    os.remove(filepath)
                    print(f"Deleted: {filename}")
                else:
                    print(f"Kept: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Replace 'path_to_directory' with your actual directory containing images
directory = 'path_to_directory'
filter_images(directory)


"""

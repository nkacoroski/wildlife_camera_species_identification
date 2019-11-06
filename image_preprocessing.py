# Functions to preprocess image: update datetimes, crop off information bars, and rename.

import datetime
from exif import Image
import os
import re

def change_datetimes(image_path, time_delta):
    """Take in image file and time change as a time delta object.
    Change exif datetime, datetime_digitized, and datetime_original
    Save file with updated exif datetimes."""
    # Open image.
    with open(image_path, 'rb') as image_file:
        image = Image(image_file)
    # Generate new datetime.
    old_datetime = datetime.datetime.strptime(image.datetime, '%Y:%m:%d %H:%M:%S')
    new_datetime  = (old_datetime + time_delta).strftime("%Y:%m:%d %H:%M:%S")
    # Replace all exif datetimes with new datetime.
    image.datetime = new_datetime
    image.datetime_digitized = new_datetime
    image.datetime_original = new_datetime
    # Rewrite image file.
    with open(image_path, 'wb') as new_image_file:
        new_image_file.write(image.get_file()) 
    print(f"{image_path[7::]} datetime fixed!")
    

def rename_image(image_path):
    """Take in image path and rename image by site,
    camera, and datetime."""
    # Get image datetime.
    with open(image_path, 'rb') as image_file:
        image = Image(image_file)
    datetime = image.datetime
    dt = re.sub(r"\s+", "", datetime)
    dt = re.sub(r"\:+", "", dt)
    camera = ""
    if image_path.startswith('IMG'):
        camera += 'c2'
    else:
        camera += 'c1'
    name = "./data/s1" + camera + "_" + dt + ".jpg"
    os.rename(image_path, name)
    print(f"{image_path[7::]} renamed!")


# TO-DO: get pyexif dump working and extract temperature data,
# consider tessaract python OCR instead?

def change_exif_datetimes_pyexif(image_path, time_delta):
    """Take in image file and time change as a time delta object.
    Change exif datetime, datetime_digitized, and datetime_original
    Save file with updated exif datetimes."""
    # open image
    img = Image.open(image_path)
    # load exif data into dictionary
    exif_dict = piexif.load(img.info['exif'])
    # generate updated datetime
    old_dt_str = exif_dict["0th"][306]
    print(old_dt_str)
    new_dt_str = change_datetime(old_dt_str, time_delta)
    # replace exif datetimes with updated value
    exif_dict["0th"][306] = new_dt_str.encode("utf-8")
    print(exif_dict['0th'][306])
    exif_dict["Exif"][36868] = new_dt_str.encode("utf-8")
    exif_dict["Exif"][36867] = new_dt_str.encode("utf-8")
    # Convert into bytes and put in image file
    exif_bytes = piexif.dump(exif_dict)
    piexif.insert(exif_bytes, image_path)
    print(f"Updated exif datetimes!")
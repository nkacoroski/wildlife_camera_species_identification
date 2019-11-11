# Functions to preprocess image: 
# correct datetimes
# rename with unique names by camera, datetime, and sequence number or iteration
# crop out information bars

import datetime
from exif import Image
import os
import os.path
import re
import exiftool

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
    """Take in image path and rename image by site, camera, and datetime."""
    # Get image datetime.
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(image_path)
    datetime_string = re.sub('[^0-9]+', '', metadata['EXIF:DateTimeOriginal'])
    if metadata["EXIF:Make"] == "RECONYX":
        if metadata['MakerNotes:Sequence'][1] != " ":
            sequence_number_string = str(metadata['MakerNotes:Sequence'][0:2])
        else:
            sequence_number_string = str(metadata['MakerNotes:Sequence'][0])
        name = "./data/s1c1_" + datetime_string + "_" + sequence_number_string + ".jpg"
        os.rename(image_path, name)
    else:
        i = 0
        name = "./data/s1c2_" + datetime_string + "_" + str(i) + ".jpg"
        while os.path.exists(name):
            i += 1
            name = "./data/s1c2_" + datetime_string + "_" + str(i) + ".jpg"
        os.rename(image_path, name)
    print(f"{image_path[7::]} renamed to {name}!")

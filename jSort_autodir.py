# This script renames JPEG images based on their date. Executable from the directory the script is in. 
import os
import re
from datetime import datetime
from PIL import Image, ExifTags

# Function to extract the date the photo was taken from its EXIF metadata
def get_image_date_taken(path):
    try:
        # Open the image using PIL
        image = Image.open(path)
        # Get the EXIF metadata from the image
        exif = image._getexif()
        
        # If no EXIF data is found, return None
        if exif is None:
            return None

        # Iterate through the EXIF data to find the 'DateTimeOriginal' tag
        for tag, value in exif.items():
            tag_name = ExifTags.TAGS.get(tag, tag)
            if tag_name == 'DateTimeOriginal':
                # Return the date as a datetime object
                return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        # Handle any exceptions that occur (e.g., file not readable, no EXIF data)
        print(f"Error reading EXIF data from {path}: {e}")
    return None

# Function to rename images in a directory based on their date taken
def rename_images_by_date(directory):
    # List to store tuples of (date_taken, full_path, filename)
    images = []
    
    # Loop through all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is a JPEG image (matches .jpg or .jpeg, case insensitive)
        if re.match(r'.*\.(jpg|jpeg)$', filename, re.IGNORECASE):
            # Get the full path of the image
            full_path = os.path.join(directory, filename)
            # Get the date the image was taken
            date_taken = get_image_date_taken(full_path)
            
            if date_taken:
                # Append the image information to the list
                images.append((date_taken, full_path, filename))
            else:
                # If the date taken could not be found, print a message
                print(f"Date taken not found for: {filename}")
    
    # Sort the images by the date they were taken (oldest to newest)
    images.sort(key=lambda x: x[0])
    
    # Counter to keep track of the number of images renamed
    image_counter = 1
    
    # Rename the images based on the sorted order
    for date_taken, full_path, filename in images:
        # Format the date in the desired format (DayMonthYear)
        date_str = date_taken.strftime('%d%b%Y').upper()
        
        # Create the new filename with the counter (e.g., "01 - 03DEC2023")
        new_filename = f"{image_counter:02} - {date_str}.jpg"
        new_full_path = os.path.join(directory, new_filename)
        
        # Ensure no duplicate file names exist before renaming
        if not os.path.exists(new_full_path):
            os.rename(full_path, new_full_path)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            # If the new filename already exists, skip renaming to avoid overwriting
            print(f"Skipping rename, {new_filename} already exists")
        
        # Increment the counter after renaming
        image_counter += 1

if __name__ == "__main__":
    # Automatically use the directory the script is in
    directory_path = os.getcwd()
    # Call the function to rename images by date
    rename_images_by_date(directory_path)
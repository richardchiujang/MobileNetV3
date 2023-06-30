import os
from PIL import Image

def convert_images_to_jpg(folder_path):
    # Get a list of all files in the folder
    file_list = os.listdir(folder_path)

    # Iterate through each file
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is an image
        if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpeg', '.jpg', '.gif')):
            # Open the image file
            image = Image.open(file_path)

            # Convert the image to JPEG format (if it's not already)
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Get the original file name (without the extension)
            file_name_without_ext = os.path.splitext(file_name)[0]

            # Save the image in JPEG format with the original file name
            output_path = os.path.join(folder_path, f'{file_name_without_ext}.jpg')
            image.save(output_path, 'JPEG')

            print(f"Converted {file_name} to {file_name_without_ext}.jpg")

# Provide the folder path where the image files are located
folder_path = './\custos/AI/BYO Tableware/No'
convert_images_to_jpg(folder_path)

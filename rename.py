import os

# Specify the path to the folder containing the images
folder_path = 'dataset\Mouse'

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    # Check if the filename matches the pattern "image_xxx"
    if filename.startswith('image_') and filename.endswith('.jpg'):
        # Extract the numeric part of the filename (e.g., "001" from "image_001.jpg")
        numeric_part = filename.split('_')[1].split('.')[0]
        
        # Rename the file to "car_xxx"
        new_filename = f'mouse_{numeric_part.zfill(3)}.jpg'
        
        # Construct the full paths for the old and new filenames
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_filename}')

print('Renaming complete.')

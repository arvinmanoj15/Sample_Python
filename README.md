# Simple Python Repository

This repository contains two Python scripts: `cap_image.py` and `rename.py`. These scripts are designed for different purposes and can be used as standalone utilities.

## 1. cap_image.py

### Description
`cap_image.py` is a Python script that captures images from a webcam and saves them in a specified directory. It allows you to control the number of images captured and adds a counter to each captured image for easy identification.

### Usage
1. Make sure you have OpenCV (cv2) installed in your Python environment.
2. Run the script by executing the following command:
   ```
   python cap_image.py
   ```
3. The script will capture 125 images by default, displaying each frame from the webcam with a counter. After capturing every 25 images, it will pause for 5 seconds.
4. To exit the image capture process, press the 'q' key.
5. The captured images will be saved in a directory named 'captured_images'.

## 2. rename.py

### Description
`rename.py` is a Python script that renames files in a specified directory based on a naming pattern. It is designed to rename image files that match the pattern "image_xxx.jpg" to "mouse_xxx.jpg," where "xxx" is a numeric sequence. This script is useful for organizing and renaming image files in bulk.

### Usage
1. Edit the `folder_path` variable in `rename.py` to specify the path to the folder containing the images you want to rename.
2. Run the script by executing the following command:
   ```
   python rename.py
   ```
3. The script will rename all files in the specified folder that match the pattern "image_xxx.jpg" to "mouse_xxx.jpg," where "xxx" is padded with leading zeros to ensure a consistent filename format.
4. After running the script, you will see the renaming progress displayed in the console.
5. Once the renaming process is complete, all files will be renamed as per the specified pattern.

## Note
Please ensure you have the necessary permissions to access and modify the specified directories when using these scripts. The scripts are provided as-is and can be customized to suit your specific requirements. If you encounter any issues or have suggestions for improvements, feel free to contribute to this repository or report issues. Enjoy using these Python utilities!

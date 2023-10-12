import cv2
import os
import time

# Create a directory to save the captured images
output_directory = 'captured_images'
os.makedirs(output_directory, exist_ok=True)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 indicates the default camera (usually the built-in webcam)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Counter for the captured images
image_count = 0

while image_count < 125:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Save the captured frame as an image
    image_count += 1
    image_filename = os.path.join(output_directory, f"image_{image_count:03d}.jpg")
    cv2.imwrite(image_filename, frame)

    # Display the current image count on the frame
    cv2.putText(frame, f"Image {image_count}/125", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Webcam Capture", frame)

    # Capture 25 images and then wait for 5 seconds
    if image_count % 25 == 0:
        print(f"Captured {image_count} images. Waiting for 5 seconds...")
        cv2.waitKey(5000)  # 5000 milliseconds (5 seconds)

    # Press 'q' to quit capturing images
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

print(f"{image_count} images captured and saved in '{output_directory}'.")

*Real-Time Red Color Detection using OpenCV
This project demonstrates real-time detection of red objects using OpenCV and Python. The script captures video from a webcam, processes each frame to identify red regions, and highlights them with bounding boxes and labels.

*Key Features*
HSV Color Space Conversion: The input frames are converted to HSV color space for easier and more precise color segmentation.
Color Range Masking: A mask is applied to isolate pixels within the specified red color range.
Contour Detection: Contours of the detected red regions are extracted to identify distinct objects.
Bounding Box and Labeling: Red regions exceeding a defined size are highlighted with a green bounding box, and labeled with the text "Red."
Real-Time Processing: Continuously processes video frames from the webcam, allowing real-time detection.

*How It Works*
The webcam captures a video feed.
Each frame is converted to HSV and masked using a defined range for the red color.
Contours are detected from the masked image.
Contours meeting the size criteria are highlighted with a bounding box and labeled.
Press q to exit the program.

*Dependencies*
OpenCV
NumPy

*Usage*
Run the script, and the program will display the webcam feed with detected red objects highlighted. Ensure you have a webcam connected and configured for your system.


import cv2
import numpy as np

# Initialize the webcam
webcam = cv2.VideoCapture(0)

# Define HSV color ranges for detecting red
# Lower red range
red_lower_1 = np.array([0, 120, 70])  # Lower bounds for red
red_upper_1 = np.array([10, 255, 255])  # Upper bounds for red

# Upper red range
red_lower_2 = np.array([170, 120, 70])  # Lower bounds for red
red_upper_2 = np.array([180, 255, 255])  # Upper bounds for red

while True:
    # Read a frame from the webcam
    ret, webcam_frame = webcam.read()

    # Convert the captured frame from BGR to HSV color space
    webcam_hsv = cv2.cvtColor(webcam_frame, cv2.COLOR_BGR2HSV)

    # Create masks for both red ranges
    mask1 = cv2.inRange(webcam_hsv, red_lower_1, red_upper_1)
    mask2 = cv2.inRange(webcam_hsv, red_lower_2, red_upper_2)

    # Combine the masks to detect all shades of red
    webcam_mask = cv2.bitwise_or(mask1, mask2)

    # Find contours from the combined mask
    contours, hierarchy = cv2.findContours(webcam_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour
    for i, cnt in enumerate(contours):
        # Check if the contour area is large enough and if it's a parent contour
        if cv2.contourArea(cnt) > 1500 and hierarchy[0][i][3] == -1:
            # Get the bounding box coordinates of the contour
            x1, y1, w, h = cv2.boundingRect(cnt)

            # Draw a green rectangle around the detected red object
            cv2.rectangle(webcam_frame, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

            # Label the detected object as 'Red'
            cv2.putText(webcam_frame, 'Red', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Display the live feed with the detected objects
    cv2.imshow('frame', webcam_frame)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()

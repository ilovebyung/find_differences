import cv2

# Create a Background Subtractor object
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

video_path = 'input_video.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Apply the background subtraction
    foreground_mask = bg_subtractor.apply(frame)

    # Optionally, you can apply morphological operations to improve the results
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    foreground_mask = cv2.morphologyEx(foreground_mask, cv2.MORPH_OPEN, kernel)

    # Display the foreground
    cv2.imshow('Moving Foreground', foreground_mask)

    if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
        break

    cap.release()
    cv2.destroyAllWindows()





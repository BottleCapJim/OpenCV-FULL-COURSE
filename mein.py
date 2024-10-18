import math
import cv2

eye_cascade = cv2.CascadeClassifier('Resources\haarcascade_eye.xml')

if eye_cascade.empty():
    raise IOError('Unable to load the eye cascade classifier XML file')

cap = cv2.VideoCapture(0)
ds_factor = 0.5
ret, frame = cap.read()
contours = []

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x_eye, y_eye, w_eye, h_eye) in eyes:
        # Adjust the ROI dimensions for iris detection
        roi_scale = 0.3  # Specify the scaling factor for ROI size
        roi_width = int(w_eye * roi_scale)
        roi_height = int(h_eye * roi_scale)
        x_offset = int((w_eye - roi_width) / 2)
        y_offset = int((h_eye - roi_height) / 2)

        iris_frame = gray[y_eye + y_offset:y_eye + y_offset + roi_height,
                          x_eye + x_offset:x_eye + x_offset + roi_width]
        cv2.imshow("iris_frame", iris_frame)

        # Apply any necessary preprocessing steps specific to iris detection
        # For example, you can use thresholding, adaptive thresholding, or other techniques

        # Detect contours in the iris frame
        contours, hierarchy = cv2.findContours(iris_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            perimeter = cv2.arcLength(contour, True)
            circularity = 4 * math.pi * (area / (perimeter * perimeter))

            # Apply conditions to filter out iris contours
            # Adjust these conditions based on your specific scenario
            area_condition = (50 <= area <= 500)
            circularity_condition = (0.7 <= circularity <= 1.2)

            if area_condition and circularity_condition:
                # Draw a circle around the detected iris
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.circle(frame, (int(x_eye + x + x_offset + w / 2), int(y_eye + y + y_offset + h / 2)),
                           int((w + h) / 4), (0, 180, 0), 2)

    cv2.imshow('Iris Detector', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

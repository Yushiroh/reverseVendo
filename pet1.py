import torch
import cv2
from ultralytics import YOLO

model = YOLO('petbottlesv8_v1.pt')

class_labels = model.names if hasattr(model, 'names') else ['class_0', 'class_1', 'class_2'] 

# Initialize the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit() 

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('Camera Feed - Press "s" to Capture and Classify', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # When 's' key is pressed
        results = model(frame)

        # Get the predicted label and confidence for classification
        for result in results:
            class_id = result.probs.top1  # Index of the class with the highest probability
            confidence = result.probs.top1conf.item()  # Confidence score for the top-1 class
            label = class_labels[class_id]  # Get the label from class ID

            # Display the label and confidence
            print(f"Label: {label}, Confidence: {confidence:.2f}")
            cv2.putText(frame, f"{label} {confidence:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # serial data here

        cv2.imshow('Captured Image - Classification Result', frame)
        
    elif key == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
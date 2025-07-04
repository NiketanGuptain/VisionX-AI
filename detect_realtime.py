import torch
model = torch.hub.load('yolov5', 'yolov5s', source='local')

import cv2
import numpy as np

# Load the pre-trained YOLOv5 model (YOLOv5s = small and fast)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert image from BGR (OpenCV) to RGB (YOLOv5 expects this)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get predictions
    results = model(img_rgb)

    # Parse results
    detections = results.xyxy[0].numpy()  # (x1, y1, x2, y2, confidence, class)

    for *box, conf, cls in detections:
        x1, y1, x2, y2 = map(int, box)
        label = model.names[int(cls)]
        confidence = f"{conf:.2f}"

        # Draw rectangle and label
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} {confidence}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    # Show the frame
    cv2.imshow('YOLOv5 Object Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

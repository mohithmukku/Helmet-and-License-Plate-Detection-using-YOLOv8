from ultralytics import YOLO

# Load the YOLO model
model = YOLO('yolov8n.pt')  # Load a pre-trained YOLO model (you can change to yolov8s.pt or yolov8m.pt)

# Train the model
model.train(data='data.yaml', epochs=50, imgsz=640)

# Save the trained model with a specific name
model.save('numberplate_detection_model.pt')  # Save your trained model

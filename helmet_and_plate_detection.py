from ultralytics import YOLO

# Load your custom YOLOv8 model (ensure the path is correct)
model = YOLO('numberplate_detection_model.pt')  # Change to your custom-trained model path

# Take user input
print("Type your corresponding choice for taking your input (i.e. 'image', 'video', 'camera')")
input_choice = input("Type here: ")

# Set source based on user input
if input_choice == "image":
    source = 'path_to_your_image.jpg'  # Change this to your image path
elif input_choice == "video":
    source = 'path_to_your_video.mp4'  # Change this to your video path
elif input_choice == "camera":
    source = 0  # Webcam input
else:
    print("Invalid input choice!")
    source = None

if source is not None:
    # Run the detection model
    results = model.predict(source=source, save=True, conf=0.5)

    # Loop through the results to find relevant detections
    for result in results:
        # Parse the detected classes from the result
        detected_classes = result.names
        for box in result.boxes:
            class_id = int(box.cls)
            class_name = detected_classes[class_id]
            
            if class_name == 'rider':
                # Check if helmet is detected on the same rider
                helmet_detected = False
                for other_box in result.boxes:
                    other_class_id = int(other_box.cls)
                    other_class_name = detected_classes[other_class_id]
                    
                    # Add logic to ensure the helmet is on the rider
                    if other_class_name == 'with helmet':
                        helmet_detected = True
                        break
                
                if not helmet_detected:
                    print("Rider detected without helmet.")
                    
                    # Now check for vehicle and number plate
                    for plate_box in result.boxes:
                        plate_class_id = int(plate_box.cls)
                        plate_class_name = detected_classes[plate_class_id]
                        if plate_class_name == 'number plate':
                            print("License plate detected:", plate_box.xyxy)  # You can extract coordinates or use OCR here

        # Save the processed results (image/video with detected boxes)
        result.save()

print("Processing complete.")

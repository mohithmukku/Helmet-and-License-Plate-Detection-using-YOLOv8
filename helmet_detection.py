from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')  # Change to your model if you trained a custom one

print("Type your corresponding choice for taking your input i.e 'image' 'video' 'camera'")
i=input("Type here:")

# For image detection
if(i=="image"):
    results = model.predict(source='path_to_your_image.jpg', save=True, conf=0.5)
    print("Processing completed")

# For video detection
elif(i=="video"):
    results = model.predict(source='path_to_your_video.mp4', save=True, conf=0.5)

# For real-time webcam detection
elif(i=="camera"):
    print("please press ctrl+c after completion of recording")
    results = model.predict(source=0, save=True, conf=0.5)
else:
    print("please enter valid input")
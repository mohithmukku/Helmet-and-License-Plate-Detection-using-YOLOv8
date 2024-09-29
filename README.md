# Helmet-and-License-Plate-Detection-using-YOLOv8
This project detects individuals not wearing helmets and identifies vehicle license plates using a custom-trained YOLOv8 model. It supports image, video, and real-time (webcam) input, and can be used for safety monitoring in areas like traffic enforcement. The model is trained to detect helmets, the absence of helmets, and license plates.

here are the steps clearly mentioned below:
To set up *YOLOv8* for detecting license plates of individuals who are not wearing helmets using *Visual Studio Code*, follow these steps:

### Step 1: *Install Visual Studio Code*
- Download and install Visual Studio Code from [here](https://code.visualstudio.com/Download).
- We can run in cmd prompt if python is downloaded.


### Step 2: *Install Python and Necessary Extensions*
1. *Python Installation*: Download and install Python 3.x from [python.org](https://www.python.org/downloads/).
2. *Install Python Extensions*:
   - Open VS Code.
   - Go to the Extensions tab (Ctrl+Shift+X).
   - Search for and install the *Python* extension by Microsoft.


### Step 3: *Install Required Python Packages*
Open a terminal in VS Code (Terminal > New Terminal) and install the required packages:

bash
pip install ultralytics opencv-python


### Step 4: *Download YOLOv8 Repository *
If you prefer to work with the YOLOv8 source code directly to get all requirements:
1. In the terminal, run, to download from git repository:
   bash
   git clone https://github.com/ultralytics/ultralytics.git
   cd ultralytics

2. Install additional dependencies if needed:
   bash
   pip install -r requirements.txt
   
   **If requirements.txt is not present then in terminal run**
   pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118
   pip install ultralytics opencv-python
   pip install torch torchvision torchaudio

Note:if any cmd is not working or downloading properly then use :python -m pip install --upgrade pip

   

### Step 5: *Prepare Your Dataset*
1. *Collect Images*: Gather images of:
   - People wearing helmets.
   - People not wearing helmets.
   - Vehicles with visible license plates.
2. *Label Your Dataset*: Use a tool like [LabelImg](https://github.com/tzutalin/labelImg) to annotate:
   - Class 1: rider
   - Class 2: with helmet
   - Class 3: without helmet
   - Class 4: number plate

### Step 6: *Organize Your Dataset*
if you just want to detect helmet and non helmet riders then default trained yolo v8 is enough and no need to download any dataset, but disadvantage is that if want to detect number plate then this yolo v8 dataset is not sufficient .
else
Then now download the dataset(https://www.kaggle.com/datasets/aneesarom/rider-with-helmet-without-helmet-number-plate) and do 
Structure your dataset as follows :

/datasets

->/datset

--->/images
  
    ->/train
    ->/val
 --->/labels
  
    ->/train
    ->/val



### Step 7: **Create data.yaml File**
Create a data.yaml file in your dataset directory with the following content:

yaml
train: C:/Users/MOHITH/helmet_detection/datasets/dataset/images/train
val: C:/Users/MOHITH/helmet_detection/datasets/dataset/images/val
nc: 4  # number of classes
names: ['rider', 'with helmet', 'without helmet', 'number plate']

Note:For default trained model classes are more than 80 but **number plate** is not there, if we dont want it then we can proceed with default dataset.



### Step 8: *Train the YOLOv8 Model*
Train the model using your dataset. In the terminal, run:

bash
yolo detect train data=data.yaml model=yolov8n.pt epochs=50 imgsz=640

If above cmd is not working properly then go with python code for training the model(dataset):
train_yolo.py
Note:if you downloaded the dataset then only train the dataset model ,because if you are using default yolov8 model then trained model is present (yolov8n.pt).



### Step 9: *Create a Python Script for Detection*
1. In VS Code, create a new Python script named helmet_and_plate_detection.py or helmet_detection.py.
2. Write the following script for detecting license plates of individuals not wearing helmets then go with :helmet_and_plate_detection.py
3. If you dont want number plate then go with :helmet_detection.py

# Load the trained YOLOv8 model
model = YOLO('runs/train/exp/weights/best.pt')  # Adjust the path as needed



### Step 10: *Run the Script*
To run the script, navigate to your working directory in the terminal and execute:

bash
python helmet_and_plate_detection.py
or 
python helmet_detection.py


### Step 11: *Check Outputs*
The results will be saved in** runs/detect **. Check the images or videos to verify the detection results.



### Summary
This setup will allow you to detect license plates of individuals who are not wearing helmets using YOLOv8 in Visual Studio Code, processing both image and video inputs.

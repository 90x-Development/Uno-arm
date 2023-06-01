# Uno-arm ![download](https://github.com/90x-Development/Uno-arm/assets/64578167/29d12c0d-6dd8-4fb9-9320-f50de5bd5153)

Python-controlled Robotic Arm with OpenCV, Arduino Uno and PCA9638


# Python-controlled Arm with Arduino Uno and PCA9638

This project implements a Python-controlled robotic arm using an Arduino Uno and PCA9638 servo motor controller. The arm is programmed to track and follow the direction of a green block (paper) using OpenCV for object detection and angle calculation.

## Prerequisites

To run this project, you'll need the following components:
- Arduino Uno: The microcontroller that interfaces with the servo motor and receives commands from Python. PCA9638 Servo Motor Controller: Controls the servo motor and provides smooth movement.
Servo Motor: The motor that moves the arm to different positions.
- Webcam: Used for capturing the video feed to detect the green block.
You'll also need to install the following software:
- Python: Version 3.9.
- OpenCV: Used for object detection and angle calculation. - PySerial: To establish serial communication between Python and Arduino.
- (Arduino ) Install adfruit Module for PCA9685 PWM

# Setup

1. Connect the Arduino Uno to the PCA9638 servo motor controller.
2. Connect the servo motor to the PCA9638 controller.
3. Connect the webcam to your computer.
4. Install OpenCV


# Usage

Connect the Arduino Uno to your computer.
Upload the Arduino sketch provided in the repository to the Arduino Uno.
Run the Python script to start the robotic arm.

```
bash python main.py
```
# Config 

1. Go to code/control.py and config port
2. When the code is running config the picture to see green block only using track bars 


![arduni](https://github.com/90x-Development/Uno-arm/assets/64578167/9f0b377e-79bd-476f-adef-49b90e877d66)
![cv](https://github.com/90x-Development/Uno-arm/assets/64578167/4f1b6673-cf88-4ee5-931c-ea8c8070d83f)
![py](https://github.com/90x-Development/Uno-arm/assets/64578167/abb77e9f-ca70-42f6-acc7-691cb69c22e0)

The webcam feed will open, and the Python program will start detecting the green block.
The servo motor will move the arm to track the direction of the green block.
#License
This project is licensed under the MIT License.

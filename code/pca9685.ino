#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

//https://github.com/90x-Development/Uno-arm
//version 9.87

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(50);
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == 'b') {
      int angle = Serial.parseInt();
      moveServo(0, angle); 
    }
  }
}

void moveServo(uint8_t servoNum, int degrees) {
  int pulse = map(degrees, 0, 180, 102, 512);
  pwm.setPWM(servoNum, 0, pulse);
}

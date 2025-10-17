// Central controller for truck vision system
// Arduino Portenta H7 + Vision Shield

#include <Arduino.h>
#include <Ethernet.h>
#include "motion_detection.h"

// Pins
#define REVERSE_PIN A0
#define PIR_PIN D0

void setup() {
  Serial.begin(115200);
  pinMode(REVERSE_PIN, INPUT);
  pinMode(PIR_PIN, INPUT);
  
  // Initialize Vision Shield camera (OV5640)
  // ... (camera init code)
  
  // Start Ethernet
  Ethernet.begin(mac, ip);
}

void loop() {
  bool inReverse = digitalRead(REVERSE_PIN);
  bool motionDetected = digitalRead(PIR_PIN) || detectMotionFromFrames();
  
  if (motionDetected && !inReverse) {
    startRecording(); // Save to microSD
  }
  
  // Stream appropriate view to Pi Zero clients
  if (inReverse) {
    streamRearCamera();
  } else {
    streamSideViews();
  }
  
  delay(50); // 20 FPS target
}

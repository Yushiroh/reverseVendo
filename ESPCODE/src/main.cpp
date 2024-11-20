#include <Arduino.h>
#include <ESP32Servo.h>

Servo myservo;

int but1 = 36;
int but2 = 39;

int pos = 0; 

void setup() {

  Serial.begin(9600);
  pinMode(but1, INPUT);
  pinMode(but2, INPUT);
  myservo.attach(23,1000,2000);

}

void loop() {

  int but1State = digitalRead(but1);
  int but2State = digitalRead(but2);

  if(but1State == 0){

    Serial.print("A");
    

  }else if(but2State == 0){

    Serial.print("B");
  }else{
    
  }


}

#include <Arduino.h>

int but1 = 36;
int but2 = 39;

void setup() {

  Serial.begin(9600);
  pinMode(but1, INPUT);
  pinMode(but2, INPUT);

}

void loop() {

  int but1State = digitalRead(but1);
  int but2State = digitalRead(but2);

  if(but1State == 0){

    Serial.print("A");
    delay(1000);

  }else if(but2State == 0){

    Serial.print("B");
    delay(1000);

  }else{
    //Serial.println("NO INPUT");
  }



}


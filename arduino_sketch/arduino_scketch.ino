/*
 Name:    Sketch.ino
 Created: 09/11/2023
 Author:  FacundoProg
*/

#include <SD.h>
#include <SPI.h>


#define chipSelect 10
String programFilename = "program.asm";
String controlFilename = "control.asm";

char data;

//UB       LB
//D3,D2,D1,D0
int outputs[4] = { A3, A2, A1, A0 };

byte clock = 2;
byte rstBuffer = 3;
byte CSProgramMemory = 4;
byte CSControlMemory = 5;


int buffer = 6;
int bits[4] = { 0, 0, 0, 0 };

int speedClock = 0;
int timePulse = 0;

unsigned long timeLedStatus = 0;

byte buttonPrograming = 7;
byte programingSignal = 8;

byte pinLedStatus = 9;
bool status = false;
int speedBlyncLed = 800;



void setup() {
  Serial.begin(9600);

  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);

  pinMode(clock, OUTPUT);
  pinMode(rstBuffer, OUTPUT);
  pinMode(CSProgramMemory, OUTPUT);
  pinMode(CSControlMemory, OUTPUT);
  pinMode(buffer, OUTPUT);
  pinMode(buttonPrograming, INPUT_PULLUP);
  pinMode(programingSignal, OUTPUT);
  pinMode(pinLedStatus, OUTPUT);

  digitalWrite(rstBuffer, HIGH);
  digitalWrite(CSProgramMemory, HIGH);
  digitalWrite(CSControlMemory, HIGH);
  digitalWrite(buffer, LOW);
  digitalWrite(programingSignal, LOW);
  digitalWrite(clock, LOW);
  digitalWrite(pinLedStatus, LOW);

  digitalWrite(A0, LOW);
  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
  digitalWrite(A3, LOW);

  if (!SD.begin(chipSelect)) {
    speedBlyncLed = 80;
    Serial.print("Error SD");
  }
}





void loop() {

  if (digitalRead(buttonPrograming) == LOW) {
    while (digitalRead(buttonPrograming) == LOW) {
      delay(2);
    }
    lecturaSD();
  }


  if (millis() > timeLedStatus + speedBlyncLed) {
    status = !status;
    digitalWrite(pinLedStatus, status);
    timeLedStatus = millis();
  }

  delay(10);
}




void lecturaSD() {
  ////////////////////////////////////////////// Begin programing ///////////////////////////////////////////////////////

  File programMemory = SD.open(programFilename, FILE_READ); // Program file

  digitalWrite(programingSignal, HIGH);
  digitalWrite(pinLedStatus, HIGH);
  digitalWrite(buffer, HIGH);

  if (programMemory) {

    while (programMemory.available()) {

      for (int i = 0; i < 8; i++) {

        for (int a = 0; a < 4; a++) {

          data = (char)programMemory.read();

          if (data == '0') {
            bits[a] = 0;
          } else if (data == '1') {
            bits[a] = 1;
          }
        }

        for (int b = 0; b < 4; b++) {
          digitalWrite(outputs[b], bits[b]);
          Serial.print(bits[b]);
        }

        Serial.print(" ");

        digitalWrite(clock, HIGH);
        delay(timePulse);
        digitalWrite(clock, LOW);
      }


      Serial.println("");

      ////// Save program memory //////
      digitalWrite(CSProgramMemory, LOW);
      delay(speedClock);
      digitalWrite(CSProgramMemory, HIGH);

      ////// Reset duffer //////
      digitalWrite(rstBuffer, LOW);
      delay(timePulse);
      digitalWrite(rstBuffer, HIGH);
    }

    digitalWrite(CSProgramMemory, HIGH);
    programMemory.close();  // Close file
  } else {
    Serial.print("Error to open program.asm");
  }



  delay(500);
  Serial.println("");



  File controlMemory = SD.open(controlFilename, FILE_READ);// Control file

  if (controlMemory) {

    while (controlMemory.available()) {

      for (int i = 0; i < 8; i++) {

        for (int a = 0; a < 4; a++) {

          data = (char)controlMemory.read();

          if (data == '0') {
            bits[a] = 0;
          } else if (data == '1') {
            bits[a] = 1;
          }
        }

        for (int b = 0; b < 4; b++) {
          digitalWrite(outputs[b], bits[b]);
          Serial.print(bits[b]);
        }
        Serial.print(" ");

        digitalWrite(clock, HIGH);
        delay(timePulse);
        digitalWrite(clock, LOW);
      }

      Serial.println("");

      // Save control memory
      digitalWrite(CSControlMemory, LOW);
      delay(speedClock);
      digitalWrite(CSControlMemory, HIGH);

      // Reset buffer
      digitalWrite(rstBuffer, LOW);
      delay(timePulse);
      digitalWrite(rstBuffer, HIGH);
    }

    digitalWrite(CSControlMemory, HIGH);
    controlMemory.close();
  } else {
    Serial.print("Error on open file control.asm");
  }


  digitalWrite(rstBuffer, HIGH);
  digitalWrite(buffer, LOW);
  digitalWrite(programingSignal, LOW);
  digitalWrite(clock, LOW);

  /////////////////////////////// End programing //////////////////////////////////
}


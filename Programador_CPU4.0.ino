/*
 Name:    Programador_CPU4.0.ino
 Created: 23/06/2019 17:22:45
 Author:  Facundo Carroz
*/

#include <SD.h>
#include <SPI.h>


#define chipSelect 10
String programa = "programa.asm"; //Archivo con datos de Programa en ensamblador
String control = "control.asm";  //Archivo con datos de Control en ensamblador

char dato;

                //UB       LB
                //D3,D2,D1,D0
int salidas[4] = {A3,A2,A1,A0};
int RELOJ = 2;
int direcciones[3] = {A5,A4,3};//Pines de direccion de la memoria de programa, usado solo al programar
int CS_M1 = 4;
int CS_M2 = 5;


int buffer = 6;
int bits[4] = {0,0,0,0};

int velocidadClk = 4;//Delay entre datos programados en la memoria 
int tiempoPulso = 1;//Para el regitro de desplazamiento

unsigned long tiempoLedEstado = 0;

int botonInicio = 7;
int pinProgramacion = 8;

int ledEstado = 9;
bool estado = false;
int velocidadLed = 800;





void setup() {

  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  pinMode(A3, OUTPUT);
  pinMode(A4, OUTPUT);
  pinMode(A5, OUTPUT);
  pinMode(3, OUTPUT);
  
  pinMode(RELOJ, OUTPUT);
  pinMode(CS_M1, OUTPUT);
  pinMode(CS_M2, OUTPUT);
  pinMode(buffer, OUTPUT);
  pinMode(botonInicio, INPUT);
  pinMode(pinProgramacion, OUTPUT);
  pinMode(ledEstado, OUTPUT);
  

  digitalWrite(CS_M1, HIGH);
  digitalWrite(CS_M2, HIGH);
  digitalWrite(buffer, LOW);
  digitalWrite(pinProgramacion, LOW);
  digitalWrite(RELOJ, LOW);
  digitalWrite(ledEstado, LOW);

  digitalWrite(A0, LOW);
  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
  digitalWrite(A3, LOW);
  digitalWrite(A4, LOW);
  digitalWrite(A5, LOW);
  digitalWrite(3, LOW);


  if(!SD.begin(chipSelect)){
    velocidadLed = 80;
  }
  
}





void loop() {

  if(digitalRead(botonInicio) == LOW){
    while(digitalRead(botonInicio) == LOW){
      delay(5);
    }
   lecturaSD();
  }


 if(millis() > tiempoLedEstado + velocidadLed){
  estado = !estado;
  digitalWrite(ledEstado, estado);
  tiempoLedEstado = millis();
  }

 delay(10);
}







void lecturaSD(){

////////////////////////////////////////////// Archivo 1 ///////////////////////////////////////////////////////
  digitalWrite(ledEstado, HIGH);
  digitalWrite(pinProgramacion, HIGH);
  delay(100);
  
  File M1 = SD.open(programa, FILE_READ);

  digitalWrite(buffer, HIGH);
  digitalWrite(CS_M1, HIGH);
  digitalWrite(CS_M2, HIGH);
  digitalWrite(A4, LOW);
  digitalWrite(A5, LOW);
  digitalWrite(3, LOW);


  if(M1){
  
    while(M1.available()){

      for(int i=0;i < 3;i++){
        dato = (char)M1.read();
        
        if(dato == '1'){
          digitalWrite(direcciones[i], HIGH);
        }
        else{
          digitalWrite(direcciones[i], LOW);
        }
        
      }


      for(int i=0;i < 7;i++){

        for(int a=0;a < 4;a++){ 
        
          dato = (char)M1.read();
          
          if(dato == '0'){
            bits[a] = 0;
            }
          else if(dato == '1'){
            bits[a] = 1;
          }

        }
          
        for(int b=0;b < 4;b++){
          digitalWrite(salidas[b], bits[b]);
        }

          
        digitalWrite(RELOJ, HIGH);
        delay(tiempoPulso);
        digitalWrite(RELOJ, LOW);
      }

      
      ////// Guarda en la M1 //////
      digitalWrite(CS_M1, LOW);
      delay(velocidadClk);
      digitalWrite(CS_M1, HIGH);
    }
    
    digitalWrite(CS_M1, HIGH);
    M1.close();
  }
  else{
    velocidadLed = 80;
  }



  delay(100);



  ////////////////////////////////////////////////////// Archivo 2 /////////////////////////////////////////////////////////////

  File M2 = SD.open(control, FILE_READ);

  digitalWrite(CS_M1, HIGH);
  digitalWrite(CS_M2, HIGH);
  digitalWrite(A4, LOW);
  digitalWrite(A5, LOW);
  digitalWrite(3, LOW);


  if(M2) {

    while(M2.available()){

      for(int i=0;i < 7;i++){

        for(int a=0;a < 4;a++){ 
        
          dato = (char)M2.read();
          
          if(dato == '0'){
            bits[a] = 0;
          }
          else if(dato == '1'){
            bits[a] = 1;
          }
        }
          
        for(int b=0;b < 4;b++){
          digitalWrite(salidas[b], bits[b]);
        }
        
        digitalWrite(RELOJ, HIGH);
        delay(tiempoPulso);
        digitalWrite(RELOJ, LOW);
      }


      ////// Guarda en la M2 //////
      digitalWrite(CS_M2, LOW);
      delay(velocidadClk);
      digitalWrite(CS_M2, HIGH);
    }
  
    digitalWrite(CS_M2, HIGH);
    M2.close(); 
  }
  else{
    velocidadLed = 80;
  }




  ///////////////////////////////Fin de la Programacion/////////////////////////////

  digitalWrite(buffer, LOW);
  digitalWrite(RELOJ, LOW);
  digitalWrite(pinProgramacion, LOW);


  for(int i=0;i < 3;i++){
    digitalWrite(ledEstado, HIGH);
    delay(100);
    digitalWrite(ledEstado, LOW);
    delay(100);
  }
}

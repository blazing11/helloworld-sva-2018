#include <FastLED.h>
#define LED_PIN     7
#define NUM_LEDS    112  //112
CRGB leds[NUM_LEDS];

const int numReadings = 10;

int incomingByte;

int standard = 180;

int readings[numReadings];      // the readings from the analog input
int readIndex = 0;              // the index of the current reading
int total = 0;                  // the running total
int average = 0;                // the average

int readingsB[numReadings];      // the readings from the analog input
int readIndexB = 0;              // the index of the current reading
int totalB = 0;                  // the running total
int averageB = 0;                // the average

int readingsC[numReadings];      // the readings from the analog input
int readIndexC = 0;              // the index of the current reading
int totalC = 0;                  // the running total
int averageC = 0;                // the average

int readingsD[numReadings];      // the readings from the analog input
int readIndexD = 0;              // the index of the current reading
int totalD = 0;                  // the running total
int averageD = 0;                // the average

int readingsE[numReadings];      // the readings from the analog input
int readIndexE = 0;              // the index of the current reading
int totalE = 0;                  // the running total
int averageE = 0;                // the average

int readingsF[numReadings];      // the readings from the analog input
int readIndexF = 0;              // the index of the current reading
int totalF = 0;                  // the running total
int averageF = 0;                // the average

int readingsG[numReadings];      // the readings from the analog input
int readIndexG = 0;              // the index of the current reading
int totalG = 0;                  // the running total
int averageG = 0;                // the average

int readingsH[numReadings];      // the readings from the analog input
int readIndexH = 0;              // the index of the current reading
int totalH = 0;                  // the running total
int averageH = 0;                // the average

int readingsI[numReadings];      // the readings from the analog input
int readIndexI = 0;              // the index of the current reading
int totalI = 0;                  // the running total
int averageI = 0;                // the average

int count = 0;

boolean limbDownA = false;
boolean limbDownB = false;
boolean limbDownC = false;
boolean limbDownD = false;
boolean limbDownE = false;
boolean limbDownF = false;
boolean limbDownG = false;
boolean limbDownH = false;
boolean limbDownI = false;

boolean detA = false;
boolean detB = false;
boolean detC = false;
boolean detD = false;
boolean detE = false;
boolean detF = false;
boolean detG = false;
boolean detH = false;
boolean detI = false;

int SerialInputA = 0;
int SerialInputB = 0;
int SerialInputC = 0;
int SerialInputD = 0;
int SerialInputE = 0;
int SerialInputF = 0;
int SerialInputG = 0;
int SerialInputH = 0;
int SerialInputI = 0;

void setup() {
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  Serial.begin(9600);

  for (int thisReading = 0; thisReading < numReadings; thisReading++) {
    readings[thisReading] = 0;
  }


}
void loop() {
  SerialInputA = analogRead(A0);
  SerialInputB = analogRead(A1);
  SerialInputC = analogRead(A2);
  SerialInputD = analogRead(A3);
  SerialInputE = analogRead(A4);
  SerialInputF = analogRead(A5);
  SerialInputG = analogRead(A6);
  SerialInputH = analogRead(A7);
  SerialInputI = analogRead(A8);

  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
  }

  total = total - readings[readIndex];
  readings[readIndex] = SerialInputA;
  total = total + readings[readIndex];
  readIndex = readIndex + 1;
  if (readIndex >= numReadings) {
    readIndex = 0;
  }

  average = total / numReadings;




  totalB = totalB - readingsB[readIndexB];
  readingsB[readIndexB] = SerialInputB;
  totalB = totalB + readingsB[readIndexB];
  readIndexB = readIndexB + 1;
  if (readIndexB >= numReadings) {
    readIndexB = 0;
  }

  averageB = totalB / numReadings;

  totalC = totalC - readingsC[readIndexC];
  readingsC[readIndexC] = SerialInputC;
  totalC = totalC + readingsC[readIndexC];
  readIndexC = readIndexC + 1;
  if (readIndexC >= numReadings) {
    readIndexC = 0;
  }

  averageC = totalC / numReadings;


  totalD = totalD - readingsD[readIndexD];
  readingsD[readIndexD] = SerialInputD;
  totalD = totalD + readingsD[readIndexD];
  readIndexD = readIndexD + 1;
  if (readIndexD >= numReadings) {
    readIndexD = 0;
  }

  averageD = totalD / numReadings;


  totalE = totalE - readingsE[readIndexE];
  readingsE[readIndexE] = SerialInputE;
  totalE = totalE + readingsE[readIndexE];
  readIndexE = readIndexE + 1;
  if (readIndexE >= numReadings) {
    readIndexE = 0;
  }

  averageE = totalE / numReadings;

  totalF = totalF - readingsF[readIndexF];
  readingsF[readIndexF] = SerialInputF;
  totalF = totalF + readingsF[readIndexF];
  readIndexF = readIndexF + 1;
  if (readIndexF >= numReadings) {
    readIndexF = 0;
  }

  averageF = totalF / numReadings;

  totalG = totalG - readingsG[readIndexG];
  readingsG[readIndexG] = SerialInputG;
  totalG = totalG + readingsG[readIndexG];
  readIndexG = readIndexG + 1;
  if (readIndexG >= numReadings) {
    readIndexG = 0;
  }

  averageG = totalG / numReadings;

  totalH = totalH - readingsH[readIndexH];
  readingsH[readIndexH] = SerialInputH;
  totalH = totalH + readingsH[readIndexH];
  readIndexH = readIndexH + 1;
  if (readIndexH >= numReadings) {
    readIndexH = 0;
  }

  averageH = totalH / numReadings;

  totalI = totalI - readingsI[readIndexI];
  readingsI[readIndexI] = SerialInputI;
  totalI = totalI + readingsI[readIndexI];
  readIndexI = readIndexI + 1;
  if (readIndexI >= numReadings) {
    readIndexI = 0;
  }

  averageI = totalI / numReadings;




  




  if (incomingByte == 'A') {
    detA = true;
  }
  if (incomingByte == 'J') {
    detA = false;
  }

  if (incomingByte == 'B') {
    detB = true;
  }
  if (incomingByte == 'K') {
    detB = false;
  }

  if (incomingByte == 'C') {
    detC = true;
  }
  if (incomingByte == 'L') {
    detC = false;
  }

  if (incomingByte == 'D') {
    detD = true;
  }
  if (incomingByte == 'M') {
    detD = false;
  }

  if (incomingByte == 'E') {
    detE = true;
  }
  if (incomingByte == 'N') {
    detE = false;
  }

  if (incomingByte == 'F') {
    detF = true;
  }
  if (incomingByte == 'O') {
    detF = false;
  }

  if (incomingByte == 'G') {
    detG = true;
  }
  if (incomingByte == 'P') {
    detG = false;
  }

  if (incomingByte == 'H') {
    detH = true;
  }
  if (incomingByte == 'Q') {
    detH = false;
  }

  if (incomingByte == 'I') {
    detI = true;
  }
  if (incomingByte == 'R') {
    detI = false;
  }

  

  pressA();
  detectA();

  pressB();
  detectB();

  pressC();
  detectC();

  pressD();
  detectD();

  pressE();
  detectE();

  pressF();
  detectF();

  pressG();
  detectG();

  pressH();
  detectH();

  pressI();
  detectI();

//  Serial.println(SerialInputF);
  //
  //  Serial.print("A: ");
  //  Serial.println(average);
  //
  //  Serial.print("B: ");
  //  Serial.println(averageB);





  //
  //  Serial.print ("Average A: ");
  //  Serial.print (average);
  //  Serial.print(" ,");
  //  Serial.println(count);
  //
  //
  //
  //  Serial.print ("Average B: ");
  //  Serial.print (averageB);
  //  Serial.print(" ,");
  //
  //  Serial.println(count);
  //
  //  Serial.println("pressed:A ");
  //  Serial.println
}

void pressA() {

  if (average > standard && !limbDownA) {
    if (count % 2 == 0) {
      LedAwhite();
    }

    if (count % 2 == 1) {
      LedAgreen();
    }
    FastLED.show();
    count += 1;

    limbDownA = true;

  }

  if (average < standard) {
    limbDownA = false;
    for ( int i = 0; i < 14; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    FastLED.show();
  }

}

void detectA() {
  if (detA) {
    if (average < standard) {
      loseSequence();
    }
  }
}

void pressB() {

  if (averageB > standard && !limbDownB) {
    if (count % 2 == 0) {
      LedBwhite();
    }

    if (count % 2 == 1) {
      LedBgreen();
    }
    count += 1;
    limbDownB = true;
    FastLED.show();

  }

  if (averageB < standard) {
    for ( int i = 77; i < 84; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    limbDownB = false;
    FastLED.show();
  }

}

void detectB() {
  if (detB) {
    if (averageB < standard) {
      loseSequence();
    }
  }
}

void pressC() {
  if (averageC > standard && !limbDownC) {
    if (count % 2 == 0) {
      LedCwhite();
    }

    if (count % 2 == 1) {
      LedCgreen();
    }
    count += 1;
    limbDownC = true;
    FastLED.show();

  }

  if (averageC < standard) {
    for ( int i = 63; i < 77; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    limbDownC = false;
    FastLED.show();
  }
}

void detectC() {
  if (detC) {
    if (averageC < standard) {
      loseSequence();
    }
  }
}

void pressD() {
  if (averageD > standard && !limbDownD) {
    if (count % 2 == 0) {
      LedDwhite();
    }

    if (count % 2 == 1) {
      LedDgreen();
    }
    count += 1;
    limbDownD = true;
    FastLED.show();

  }

  if (averageD < standard) {
    for ( int i = 14; i < 21; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    limbDownD = false;
    FastLED.show();
  }
}

void detectD() {
  if (detD) {
    if (averageD < standard) {
      loseSequence();
    }
  }
}

void pressE() {
  if (averageE > standard && !limbDownE) {
    if (count % 2 == 0) {
      LedEwhite();
    }

    if (count % 2 == 1) {
      LedEgreen();
    }
    count += 1;
    limbDownE = true;
    FastLED.show();

  }

  if (averageE < standard) {
    for ( int i = 84; i < 112; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    limbDownE = false;
    FastLED.show();
  }
}

void detectE() {
  if (detE) {
    if (averageE < standard) {
      loseSequence();
    }
  }
}

void pressF() {
  if (averageF > standard && !limbDownF) {
    if (count % 2 == 0) {
      LedFwhite();
    }

    if (count % 2 == 1) {
      LedFgreen();
    }
    count += 1;
    limbDownF = true;
    FastLED.show();

  }

  if (averageF < standard) {
    for ( int i = 56; i < 63; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    limbDownF = false;
    FastLED.show();
  }
}

void detectF() {
  if (detF) {
    if (averageF < standard) {
      loseSequence();
    }
  }
}

void pressG() {
  if (averageG > standard && !limbDownG) {
    if (count % 2 == 0) {
      LedGwhite();
    }

    if (count % 2 == 1) {
      LedGgreen();
    }
    count += 1;
    limbDownG = true;
    FastLED.show();

  }

  if (averageG < standard) {
    for ( int i = 21; i < 35; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    limbDownG = false;
    FastLED.show();
  }
}

void detectG() {
  if (detG) {
    if (averageG < standard) {
      loseSequence();
    }
  }
}

void pressH() {
  if (averageH > standard && !limbDownH) {
    if (count % 2 == 0) {
      LedHwhite();
    }

    if (count % 2 == 1) {
      LedHgreen();
    }
    count += 1;
    limbDownH = true;
    FastLED.show();

  }

  if (averageH < standard) {
    for ( int i = 35; i < 42; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    limbDownH = false;
    FastLED.show();
  }
}

void detectH() {
  if (detH) {
    if (averageH < standard) {
      loseSequence();
    }
  }
}

void pressI() {
  if (averageI > standard && !limbDownI) {
    if (count % 2 == 0) {
      LedIwhite();
    }

    if (count % 2 == 1) {
      LedIgreen();
    }
    count += 1;
    limbDownI = true;
    FastLED.show();

  }

  if (averageI < standard) {
    for ( int i = 42; i < 56; i++) {
      leds[i] = CRGB(0, 0, 0);
    }
    limbDownI = false;
    FastLED.show();
  }
}

void detectI() {
  if (detI) {
    if (averageI < standard) {
      loseSequence();
    }
  }
}



void LedAwhite() {
  for ( int i = 0; i < 14; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedAgreen() {
  for ( int i = 0; i < 14; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void LedBwhite() {
  for ( int i = 77; i < 84; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedBgreen() {
  for ( int i = 77; i < 84; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void LedCwhite() {
  for ( int i = 63; i < 77; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedCgreen() {
  for ( int i = 63; i < 77; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void LedDwhite() {
  for ( int i = 14; i < 21; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedDgreen() {
  for ( int i = 14; i < 21; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void LedEwhite() {
  for ( int i = 84; i < 112; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedEgreen() {
  for ( int i = 84; i < 112; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void LedFwhite() {
  for ( int i = 56; i < 63; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedFgreen() {
  for ( int i = 56; i < 63; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void LedGwhite() {
  for ( int i = 21; i < 35; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedGgreen() {
  for ( int i = 21; i < 35; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void LedHwhite() {
  for ( int i = 35; i < 42; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedHgreen() {
  for ( int i = 35; i < 42; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void LedIwhite() {
  for ( int i = 42; i < 56; i++) {
    leds[i] = CRGB(255, 255, 255);
  }
}

void LedIgreen() {
  for ( int i = 42; i < 56; i++) {
    leds[i] = CRGB(0, 255, 0);
  }
}

void loseSequence() {
  for (int i; i < 112; i++) {
    leds[i] = CRGB(0, 0, 255);
  }
  FastLED.show();
  Serial.println("lose");
}

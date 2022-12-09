#include <SoftwareSerial.h>
#define BT_RX 2
#define BT_TX 3

int led = 13;
int flame = 7;
int state = 0;
int speaker = 8;

SoftwareSerial HM10(BT_RX, BT_TX);

void setup() {
  pinMode(led, OUTPUT);
  pinMode(flame, INPUT);
  Serial.begin(9600);
  HM10.begin(9600);
}

void loop() {
  state = digitalRead(flame);
  digitalWrite(led, LOW);

  if(!state) {
    digitalWrite(led, HIGH);
    if(HM10.available()) {
      if(Serial.available()) {
        Serial.println("1");
      }
      Serial.println("대피하세요!!");
      for(int i = 0; i < 50; i++) {
        tone(speaker, 988, 250);
        delay(300);
        noTone(speaker);
      }
    }
    else {
      if(Serial.available()) {
        Serial.println("0");
      }
      Serial.println("초기 진화를 하세요!!");
      for(int i = 0; i < 50; i++) {
        tone(speaker, 488, 250);
        delay(300);
        noTone(speaker);
      }
    }
    delay(100);
  }
  else {
    Serial.println("off");
    digitalWrite(led, LOW);
    delay(100);
  }
  delay(100);
}
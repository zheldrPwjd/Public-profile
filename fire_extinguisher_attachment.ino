#include <SoftwareSerial.h>
#define BT_RX 2
#define BT_TX 3

int flame = 7;
int state = 0;
int speaker = 8;

String myString = "";

SoftwareSerial HM10(BT_RX, BT_TX);

void setup() {
  pinMode(flame, INPUT);
  Serial.begin(9600);
  HM10.begin(9600);
}

void loop() {
  state = digitalRead(flame);
  if(!state) {
    HM10.write('2'); //소화기 부착물에서 화재 감지기로 화재가 감지됨을 전송함
    for(int i = 0; i < 50; i++) {
      tone(speaker, 988, 250);
      delay(300);
      noTone(speaker);
    }
    delay(100);
  }
  delay(100);
}
#include <SoftwareSerial.h>
#include <dht11.h>
#define DHT11PIN 8
dht11 DHT11;
int pres = A4;
int light = A5;

void setup() {
    pinMode(pres, INPUT);
    pinMode(light, INPUT);
    Serial.begin(9600);
}

void loop() {
    DHT11.read(DHT11PIN);
    Serial.print("TEMP = ");
    Serial.print(DHT11.temperature);
    Serial.print(";");
    Serial.print("HUM = ");
    Serial.print(DHT11.humidity);
    Serial.print(";");
    Serial.print("PRES = ");
    Serial.print(analogRead(pres));
    Serial.print(";");
    Serial.print("LIGHT = ");
    Serial.println(analogRead(light));
    delay(500);
}

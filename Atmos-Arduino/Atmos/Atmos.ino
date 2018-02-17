#include <SoftwareSerial.h>
#include <dht11.h>
#define DHT11PIN 8
dht11 DHT11;
int water = A2;
int light = A5;

void setup() {
    pinMode(water, INPUT);
    pinMode(light, INPUT);
    Serial.begin(9600);
}

void loop() {
    DHT11.read(DHT11PIN);
    Serial.print("TEMP = ");
    Serial.print(DHT11.temperature);
    Serial.println("°C");
    Serial.print("HUM = ");
    Serial.println(DHT11.humidity);
    Serial.print("WATER = ");
    Serial.println(analogRead(water));
    Serial.print("LIGHT = ");
    Serial.println(analogRead(light));
    Serial.println()
    delay(500);
}

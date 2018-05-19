#include <SoftwareSerial.h>
#include <dht11.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>
#include <Adafruit_TSL2561_U.h>


#define DHT11PIN 8
#define BMP_SCK 13
#define BMP_MISO 12
#define BMP_MOSI 11
#define BMP_CS 10
#define OK_LED 7

dht11 DHT11;
Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, 12345);
Adafruit_BMP280 bme(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);
int pres = A4;
int light = A5;

void configureSensor(void)
{
  tsl.enableAutoRange(true);
  tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);
}

void setup() {
    pinMode(OK_LED, OUTPUT);
    Serial.begin(9600);
    if (!tsl.begin()){
      Serial.print("Ooops, no TSL2561 detected ... Check your wiring or I2C ADDR!");
      while (1);
    }
    if (!bme.begin()) {
      Serial.println("Could not find a valid BMP280 sensor, check wiring!");
      while (1);
    }
    configureSensor();
    digitalWrite(OK_LED, HIGH);
    //Serial.println("OK");
}

void loop() {
    DHT11.read(DHT11PIN);
    sensors_event_t event;
    tsl.getEvent(&event);
    Serial.print("TEMP = ");
    Serial.print(DHT11.temperature * 100);
    Serial.print(";");
    Serial.print("HUM = ");
    Serial.print(DHT11.humidity * 100);
    Serial.print(";");
    Serial.print("PRES = ");
    Serial.print(bme.readPressure()); // It's already *100
    Serial.print(";");
    Serial.print("LIGHT = ");
    Serial.println(event.light * 100);
    delay(500);
}

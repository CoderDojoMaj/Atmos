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

dht11 DHT11;
Adafruit_TSL2561_Unified tsl = Adafruit_TSL2561_Unified(TSL2561_ADDR_FLOAT, 12345);
Adafruit_BMP280 bme(BMP_CS, BMP_MOSI, BMP_MISO,  BMP_SCK);
int pres = A4;
int light = A5;

void configureSensor(void)
{
  /* You can also manually set the gain or enable auto-gain support */
  // tsl.setGain(TSL2561_GAIN_1X);      /* No gain ... use in bright light to avoid sensor saturation */
  // tsl.setGain(TSL2561_GAIN_16X);     /* 16x gain ... use in low light to boost sensitivity */
  tsl.enableAutoRange(true);            /* Auto-gain ... switches automatically between 1x and 16x */

  /* Changing the integration time gives you better sensor resolution (402ms = 16-bit data) */
  tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_13MS);      /* fast but low resolution */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_101MS);  /* medium resolution and speed   */
  // tsl.setIntegrationTime(TSL2561_INTEGRATIONTIME_402MS);  /* 16-bit data but slowest conversions */

  /* Update these values depending on what you've set above! */
  Serial.println("------------------------------------");
  Serial.print  ("Gain:         "); Serial.println("Auto");
  Serial.print  ("Timing:       "); Serial.println("13 ms");
  Serial.println("------------------------------------");
}

void setup() {
    Serial.begin(9600);
    if (!tsl.begin()){
      /* There was a problem detecting the ADXL345 ... check your connections */
      Serial.print("Ooops, no TSL2561 detected ... Check your wiring or I2C ADDR!");
      while (1);
    }
    if (!bme.begin()) {  
      Serial.println("Could not find a valid BMP280 sensor, check wiring!");
      while (1);
    }
    configureSensor();
}

void loop() {
    DHT11.read(DHT11PIN);
    sensors_event_t event;
    tsl.getEvent(&event);
    Serial.print("TEMP = ");
    Serial.print(DHT11.temperature);
    Serial.print(";");
    Serial.print("HUM = ");
    Serial.print(DHT11.humidity);
    Serial.print(";");
    Serial.print("PRES = ");
    Serial.print(bme.readPressure()/100);
    Serial.print(";");
    Serial.print("LIGHT = ");
    Serial.println(event.light);
    delay(500);
}


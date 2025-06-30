#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHTesp.h>
#include <WiFi.h>
#include <HTTPClient.h>

// OLED configuration
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_ADDRESS 0x3C
TwoWire myWire = TwoWire(0);
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &myWire, -1);

// Sensor pins
const int DHT_SENSOR_PIN = 21;
const int GAS_SENSOR_PIN = 19;

// WiFi configuration
const char *ssid = "Dennis";
const char *password = "875462319";

// Django server URL
const char *serverUrl = "https://7fb257d5c410-1468329044895344350.ngrok-free.app/api/sensor-readings/";

// Sensor instances
DHTesp dht;

// Sensor values
float temperature = 0.0;
float humidity = 0.0;
int gasValue = 0;

void setupDisplay();
void readDHTSensor();
void readGasSensor();
void updateDisplay();
void connectToWiFi();
void sendDataToServer();

void setup() {
  Serial.begin(115200);
  delay(1000);

  connectToWiFi();

  dht.setup(DHT_SENSOR_PIN, DHTesp::DHT11);
  myWire.begin(23, 22);

  setupDisplay();
}

void loop() {
  readDHTSensor();
  readGasSensor();
  updateDisplay();
  sendDataToServer();
  delay(5000);
}

void setupDisplay() {
  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    while (true)
      ;
  }

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
}

void readDHTSensor() {
  TempAndHumidity data = dht.getTempAndHumidity();
  temperature = data.temperature;
  humidity = data.humidity;
}

void readGasSensor() {
  gasValue = analogRead(GAS_SENSOR_PIN);
}

void updateDisplay() {
  display.clearDisplay();
  display.setCursor(0, 0);

  display.print("T: ");
  display.print(temperature, 1);
  display.print((char)247);
  display.println("C");

  display.print("H: ");
  display.print(humidity, 1);
  display.println("%");

  display.print("G: ");
  display.print(gasValue);
  display.println("ppm");

  display.print("WiFi: ");
  display.println(WiFi.status() == WL_CONNECTED ? "OK" : "X");

  display.display();
}

void connectToWiFi() {
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("Connected!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void sendDataToServer() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{";
    jsonData += "\"temperature\": " + String(temperature, 1) + ",";
    jsonData += "\"humidity\": " + String(humidity, 1) + ",";
    jsonData += "\"gas_value\": " + String(gasValue);
    jsonData += "}";

    int httpResponseCode = http.POST(jsonData);

    if (httpResponseCode > 0) {
      Serial.printf("POST OK: ");
      Serial.println(httpResponseCode);
    } else {
      Serial.printf("POST failed, error: ");
      Serial.println(http.errorToString(httpResponseCode).c_str());
    }
    http.end();
  } else {
    Serial.println("WiFi not connected");
  }
}

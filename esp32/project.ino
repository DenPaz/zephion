#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <DHTesp.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

// Configuration
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_ADDRESS 0x3C
#define DHT_PIN 21
#define GAS_PIN 19
#define SDA_PIN 23
#define SCL_PIN 22

// BLE UUIDs
#define SERVICE_UUID "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

// WiFi credentials
const char *ssid = "Dennis";
const char *password = "875462319";
const char *serverUrl = "https://7fb257d5c410-1468329044895344350.ngrok-free.app/api/sensor-readings/";

// Global State
BLECharacteristic *pCharacteristic;
bool bleActive = false;
TwoWire myWire = TwoWire(0);
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &myWire, -1);
DHTesp dht;
float temperature = 0.0;
float humidity = 0.0;
int gasValue = 0;

// Function Prototypes
void initDisplay();
void initWiFi();
void initBLE();
void stopBLE();
void readSensors();
void updateDisplay();
void sendData();

// Setup
void setup() {
  Serial.begin(115200);
  delay(1000);
  myWire.begin(SDA_PIN, SCL_PIN);
  initDisplay();
  dht.setup(DHT_PIN, DHTesp::DHT11);
  initWiFi();
  if (WiFi.status() != WL_CONNECTED) {
    initBLE();
  }
}

// Loop
void loop() {
  bool wifiConnected = WiFi.status() == WL_CONNECTED;
  readSensors();
  updateDisplay();
  if (wifiConnected && bleActive) {
    Serial.println("WiFi restored. Stopping BLE...");
    stopBLE();
    delay(200);
  }
  if (!wifiConnected && !bleActive) {
    Serial.println("WiFi lost. Starting BLE...");
    initBLE();
    delay(200);
  }
  sendData();
  delay(5000);
}

// Initialization
void initDisplay() {
  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDRESS)) {
    Serial.println("SSD1306 failed");
    while (true)
      ;
  }
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
}

void initWiFi() {
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  for (int attempts = 0; attempts < 20 && WiFi.status() != WL_CONNECTED; attempts++) {
    delay(500);
    Serial.print(".");
  }
  if (WiFi.status() == WL_CONNECTED) {
    Serial.println(" Connected!");
    Serial.print("IP: ");
    Serial.println(WiFi.localIP());
  } else {
    Serial.println(" Failed to connect.");
  }
}

void initBLE() {
  BLEDevice::init("ESP32SensorBLE");
  BLEServer *server = BLEDevice::createServer();
  BLEService *service = server->createService(SERVICE_UUID);
  pCharacteristic = service->createCharacteristic(
    CHARACTERISTIC_UUID,
    BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY);
  pCharacteristic->addDescriptor(new BLE2902());
  service->start();
  BLEAdvertising *advertising = BLEDevice::getAdvertising();
  advertising->addServiceUUID(SERVICE_UUID);
  advertising->start();
  bleActive = true;
  Serial.println("BLE advertising started");
}

void stopBLE() {
  BLEDevice::deinit(true);
  bleActive = false;
  Serial.println("BLE stopped");
}

// Sensor Handling
void readSensors() {
  TempAndHumidity data = dht.getTempAndHumidity();
  if (!isnan(data.temperature))
    temperature = data.temperature;
  if (!isnan(data.humidity))
    humidity = data.humidity;
  gasValue = analogRead(GAS_PIN);
}

void updateDisplay() {
  display.clearDisplay();
  display.setCursor(0, 0);
  display.printf("T: %.1f%cC\n", temperature, (char)247);
  display.printf("H: %.1f%%\n", humidity);
  display.printf("G: %dppm\n", gasValue);
  display.printf("Mode: %s\n", WiFi.status() == WL_CONNECTED ? "WiFi" : "BLE");
  display.display();
}

void sendData() {
  String jsonData = "{";
  jsonData += "\"temperature\": " + String(temperature, 1) + ",";
  jsonData += "\"humidity\": " + String(humidity, 1) + ",";
  jsonData += "\"gas_value\": " + String(gasValue);
  jsonData += "}";

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");
    int code = http.POST(jsonData);
    if (code > 0) {
      Serial.printf("POST OK: %d\n", code);
    } else {
      Serial.printf("POST failed: %s\n", http.errorToString(code).c_str());
    }
    http.end();
  } else {
    Serial.println("WiFi not connected. Sending via BLE...");
    if (pCharacteristic) {
      pCharacteristic->setValue(jsonData.c_str());
      pCharacteristic->notify();
    }
  }
}

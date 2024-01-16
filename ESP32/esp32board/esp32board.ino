#include <SPI.h>
#include <MFRC522.h>
#include <WiFi.h>
#include <HTTPClient.h>

#define RST_PIN    22   // Define the RST_PIN for the MFRC522 module
#define SS_PIN     21   // Define the SS_PIN for the MFRC522 module

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create an MFRC522 instance.

const char* ssid = "rohan";
const char* password = "rohan1234";
const char* serverUrl = "http://192.168.210.45:8000/SData/data1/";  // Replace with the IP of your ESP32

void setup() {
  Serial.begin(115200);  // Initialize serial communication
  SPI.begin();           // Initialize SPI bus
  mfrc522.PCD_Init();    // Initialize the MFRC522 reader

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // Look for new cards
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    // Show UID on serial monitor
    Serial.print("Card UID: ");
    String cardUID = "";
    for (byte i = 0; i < mfrc522.uid.size; i++) {
      cardUID += (mfrc522.uid.uidByte[i] < 0x10 ? "0" : "");
      cardUID += String(mfrc522.uid.uidByte[i], HEX);
    }
    Serial.println(cardUID);

    // Send card UID to the local server using a GET request
    sendRFIDData(cardUID);

    delay(1000);  // Delay to prevent reading the same card repeatedly
  }
}

void sendRFIDData(String cardUID) {
  HTTPClient http;
 for (char& c : cardUID) {
        c = std::toupper(c);
    }
  String url = serverUrl + cardUID;
  Serial.println(url);
  http.begin(url); 
  int httpCode = http.GET();
  Serial.println(httpCode);
  if (httpCode > 0) {
    String payload = http.getString();
    Serial.println("Server response: " + payload);
  } else {
    Serial.println("HTTP GET failed");
  }

  http.end();
}

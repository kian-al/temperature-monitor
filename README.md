📡 ESP32 Smart Temperature & Humidity Alert System

A smart IoT monitoring project built with ESP32, DHT22, MicroPython, and Wokwi.
This system continuously reads temperature & humidity and triggers:

🔴 Red LED alert when temperature is critical

🔊 Continuous buzzer beeps in danger

🔘 Physical button detection

🧪 Fully compatible with Wokwi simulator

🚀 Features
✅ Sensor Monitoring

Reads temperature and humidity using DHT22

Prints live results via serial monitor

🔴 Critical Temperature Detection

Critical zone rules:

Temp > 35°C

Temp < 0°C

If critical:

Red LED activates

Buzzer plays fast continuous alarm

🛑 Error Handling

If any sensor error occurs:

Red LED blinks 3 times

Error message is printed

🔘 Physical Button Support

Button connected on pin 0

Detects presses and prints message

📦 Project Files
File	Description
main.py	Main MicroPython code
wokwi.toml	Wokwi project config
diagram.json	ESP32 wiring diagram
.gitignore	Ignore heavy files
LICENSE	MIT License
🧰 Hardware Components

ESP32 DevKit V1

DHT22 temperature & humidity sensor

RED LED

Buzzer

Push button

Jumper wires

🛠️ Wiring (Wokwi Diagram Included)

Pins used:

Component	Pin
DHT22	GPIO 14
Red LED	GPIO 5
Buzzer (PWM)	GPIO 21
Button	GPIO 0

Diagram is already included in the repo (diagram.json).

import time
from machine import Pin, PWM
import dht

# DHT22 sensor
sensor = dht.DHT22(Pin(14))

# Only RED LED
led_red = Pin(5, Pin.OUT)

# Buzzer
buzzer = PWM(Pin(21))
buzzer.freq(2000)

# Button
button = Pin(0, Pin.IN, Pin.PULL_UP)

def continuous_alarm():
    """Play continuous fast beeping"""
    for i in range(5):  # 5 fast beeps
        buzzer.duty(600)
        time.sleep(0.1)   # Very short beep
        buzzer.duty(0)
        time.sleep(0.1)   # Very short pause



# Main loop
while True:
    try:
        # Button check
        if not button.value():
            print("🔘 Button pressed!")
            time.sleep(0.2)
        
        # Read sensor
        sensor.measure()
        temp = sensor.temperature()
        humidity = sensor.humidity()
        
        print(f"🌡️ {temp:.1f}°C | 💧 {humidity:.1f}%", end="")
        
        # Check if temperature needs RED LED and continuous alarm
        needs_alarm = (temp > 35 or temp < 0)
        
        if needs_alarm:
            led_red.on()
            print(" → 🔴 CRITICAL!")
            # Continuous fast beeping when in critical zone
            continuous_alarm()
        else:
            led_red.off()
            print(" → ✅ Normal")
        
        time.sleep(1)  # Shorter delay for more responsive alarm
        
    except Exception as e:
        print(f"❌ Error: {e}")
        # Blink red LED on error
        for _ in range(3):
            led_red.on()
            time.sleep(0.2)
            led_red.off()
            time.sleep(0.2)
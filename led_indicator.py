import time

class LedIndicator:
    def __init__(self):
        self.led_color = "Grey"

    def finished(self):
        print("Blinking green LED...")
        self.led_color = "Green"
        time.sleep(2)
        print("Drink ready!")
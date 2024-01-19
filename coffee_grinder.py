import time

class CoffeeGrinder:
    def __init__(self):
        self.beans = ["Arabica", "Robusta", "Liberica"]

    def grind_beans(self, beans_type):
        print(f"Grinding {beans_type} beans")
        time.sleep(1)
        print("Grinding sound...")
        print(f"{beans_type} beans grounded!")
import time

class CoffeeBoiler:
    def __init__(self):
        self.water_temp = 20

    def heat_water(self):
        print("Heating water...")
        for _ in range(3):
            time.sleep(1)
            self.water_temp += 20
            print(f"Water temperature: {self.water_temp}C")

    def brew_coffee(self):
        print("Brewing coffee...")
        time.sleep(2)
        print("Coffee ready!")

    def combine(self, ingredient):
        print(f"Combining coffee with {ingredient}")
        time.sleep(2)
        print("Drink ready!")
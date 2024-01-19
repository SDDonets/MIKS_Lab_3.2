import time

class MilkFrother:
    def __init__(self):
        self.milk = "Whole Milk"

    def froth_milk(self):
        print(f"Frothing {self.milk}...")
        time.sleep(2)
        print(self.milk + " frothed!")
        return f"{self.milk} Frothed"
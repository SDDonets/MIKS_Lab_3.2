class CupDispenser:
    def __init__(self):
        self.cups = [
            {"size": "small"},
            {"size": "medium"},
            {"size": "large"}
        ]

    def dispense_cup(self):
        chosen_cup = self.cups.pop()
        print(f"Dispensing {chosen_cup['size']} cup")
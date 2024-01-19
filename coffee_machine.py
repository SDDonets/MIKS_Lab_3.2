from cup_dispenser import CupDispenser
from coffee_grinder import CoffeeGrinder
from coffee_boiler import CoffeeBoiler
from milk_frother import MilkFrother
from led_indicator import LedIndicator

class CoffeeMachine:
    def __init__(self):
        self.cup_dispenser = CupDispenser()
        self.coffee_grinder = CoffeeGrinder()
        self.coffee_boiler = CoffeeBoiler()
        self.milk_frother = MilkFrother()
        self.indicator = LedIndicator()

    def make_espresso(self):
        self.cup_dispenser.dispense_cup()
        self.coffee_grinder.grind_beans()
        self.coffee_boiler.heat_water()
        self.coffee_boiler.brew_coffee()
        self.indicator.finished()

    def make_cappuccino(self):
        self.make_espresso()
        self.milk_frother.froth_milk()
        self.coffee_boiler.combine()
        self.indicator.finished()
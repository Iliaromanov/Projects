from typing import Dict

class Person:
    all_ppl = {}

    def __init__(self, name: str):
        self.name = name
        self.economic_class = "lower class"
        self.net_worth = 0
        Person.all_ppl[self.name] = f"{self.economic_class}, Net Worth: ${self.net_worth}"

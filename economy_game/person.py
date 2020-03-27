from typing import Dict


class Person:
    all_ppl = {}

    def __init__(self, name: str):
        self.name = name
        self.economic_class = "lower class"
        self.net_worth = 0
        Person.all_ppl[self.name] = f"{self.economic_class}, Net Worth: ${self.net_worth}"
        
    def earn_money(self, amount: float) -> None:
        self.net_worth += amount
        Person.all_ppl[self.name] = f"{self.economic_class}, Net Worth: ${self.net_worth}"

    def calc_economic_class(self) -> str:
        if self.net_worth <= 70000:
            self.economic_class = "lower class"
        elif self.net_worth <= 300000:
            self.economic_class = "middle class"
        elif self.net_worth >= 300000 and self.net_worth <= 2000000:
            self.economic_class = "upper middle class"
        elif self.net_worth >= 2000000:
            self.economic_class = "upper class"

        Person.all_ppl[self.name] = f"{self.economic_class}, Net Worth: ${self.net_worth}"

        return self.economic_class

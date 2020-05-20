class Character:
    def __init__(self, name: str, character_class: str):
        self.name = name
        self.character_class = character_class
        self.level = 1
        self.xp = 0

    def __str__(self) -> str:
        return f"{self.name}, Level {self.level} {self.character_class}"

    def use_item(self, item) -> str:
        return f"{self.name} uses {item.item_name}."


class Item:
    def __init__(self, item_name: str, item_level: int):
        self.item_name = item_name
        self.item_level = item_level

    def vendor_price(self) -> int:
        price = self.item_level * 13
        return price

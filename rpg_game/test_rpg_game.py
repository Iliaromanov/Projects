from rpg_game import Character, Item


def test__str__():
    a = Character("Bob", "warrior")
    assert str(a) == "Bob, Level 1 warrior"

    b = Character("Bartholamule", "farmer")
    assert str(b) == "Bartholamule, Level 1 farmer"


def test_use_item():
    a = Character("Bob", "warrior")
    sword = Item("sword", 5)
    assert a.use_item(sword) == "Bob uses sword."

    spear = Item("spear", 1)
    assert a.use_item(spear) == "Bob uses spear."


def test_vendor_price():
    sword = Item("sword", 5)
    assert sword.vendor_price() == 65

    spear = Item("spear", 1)
    assert spear.vendor_price() == 13

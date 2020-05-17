from person import Person

def test__str__():
    bob = Person("bob")
    assert str(bob) == "bob, lower class, net worth: $0"

    barnard = Person("barnard")
    assert str(barnard) == "barnard, lower class, net worth: $0"


def test_earn_money():
    bob = Person("bob")
    bob.earn_money(1000)
    assert bob.net_worth == 1000

    barnard = Person("barnard")
    barnard.earn_money(1)
    assert barnard.net_worth == 1


def test_calc_economic_class():
    barnard = Person("barnard")
    barnard.net_worth = 71000
    barnard.calc_economic_class()
    assert barnard.economic_class == "middle class"

    bartholamule = Person("Bartholamule")
    bartholamule.earn_money(2000000)
    bartholamule.calc_economic_class()
    assert bartholamule.economic_class == "upper class"

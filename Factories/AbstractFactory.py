from abc import ABC
from enum import Enum, auto
from typing import List


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious.")


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in  Tea bag, boil water"
              f" pour {amount} ml and enjoy")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind coffee beans , boil water"
              f" pour {amount} ml and enjoy")
        return Coffee()


def make_drink(drink_name: str):
    if drink_name.lower() == "coffee":
        return CoffeeFactory().prepare(50)
    elif drink_name.lower() == "tea":
        return TeaFactory().prepare(50)
    else:
        return None


class HotDrinkMachine:

    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories: List[HotDrinkFactory()]
    factories = []
    initialised = False

    def __init__(self):
        """ initialised factories which is available drink factories. """
        if not self.initialised:
            self.initialised = True
            for available_drink in self.AvailableDrink:
                drink_name = available_drink.name[0] + available_drink.name[1:].lower()
                drink_factory_name = drink_name+"Factory"
                drink_factory_instance = eval(drink_factory_name)()
                self.factories.append((drink_name,drink_factory_instance))

    def make_drink(self):
        # 1 . print available drink then take option from the customer .
        # 2. ask about an amount than make it.
        for available_drink in self.factories:
            print(available_drink[0])
        chosen_drink_index = int(input(f"Please pick drink (0-{len(self.factories)-1} ) : "))
        selected_amount = int(input(f"Specify amount: "))
        return self.factories[chosen_drink_index][1].prepare(amount=selected_amount)


if __name__ == '__main__':
    # entry = input("What kind of drink would u like? ")
    # drink = make_drink(entry)
    # drink.consume()
    hdm = HotDrinkMachine()
    hdm.make_drink()
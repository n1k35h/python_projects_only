class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
        "water": 3000,
        "milk": 3000,
        "coffee": 1000,
        "chocolate powder": 1000,
        "tea": 1000,
        "cup": 1000

        }

    def report(self):
        """Prints a report of all resources."""
        print(f"\nWater: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Chocolate powder: {self.resources['chocolate powder']}g")
        print(f"Tea: {self.resources['tea']}g")
        print(f"Cups: {self.resources['cup']} cups")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\nSorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"\nHere is your {order.name} ☕️. Enjoy!")

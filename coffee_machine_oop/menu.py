class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, chocolate_powder, tea, cup, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "chocolate powder": chocolate_powder,
            "tea": tea,
            "cup": cup
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, chocolate_powder=0, tea=0, cup=1, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, chocolate_powder=0, tea=0, cup=1, cost=1.5),
            MenuItem(name="coffee", water=250, milk=0, coffee=24, chocolate_powder=0, tea=0, cup=1, cost=2),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, chocolate_powder=0, tea=0, cup=1, cost=3),
            MenuItem(name="tea", water=200, milk=100, coffee=0, chocolate_powder=0, tea=10, cup=1, cost=1.5),
            MenuItem(name="hot chocolate", water=0, milk=200, coffee=0, chocolate_powder=20, tea=0, cup=1, cost=2.5),
            MenuItem(name="hot water", water=300, milk=0, coffee=0, chocolate_powder=0, tea=0, cup=1, cost=0.5),
            MenuItem(name="hot milk", water=0, milk=300, coffee=0, chocolate_powder=0, tea=0, cup=1, cost=1),

        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

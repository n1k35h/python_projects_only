class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "pounds": 1.00,
        "fifty pences": 0.50,
        "twenty pences": 0.20,
        "ten pences": 0.10,
        "five pences": 0.05
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"\nMoney: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.\n")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"\nHere is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("\nSorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

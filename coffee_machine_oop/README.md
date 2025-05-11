# Coffee Machine Simulation

This project is a simulation of a coffee machine built using **Object-Oriented Programming (OOP)** principles. It allows users to interact with the machine by selecting drinks, checking the machine's status, and turning it off. The program is modular and demonstrates the use of encapsulation and abstraction through its design.

---

## Features

- **Drink Selection**: Users can choose from a menu of drinks.
- **Resource Management**: The machine checks if there are enough resources to make the selected drink.
- **Payment Processing**: Handles monetary transactions for drink purchases.
- **Status Reports**: Displays the current status of resources and money.
- **Turn Off Functionality**: Allows the user to turn off the machine.

---

## Classes and Their Roles

1. **`Menu`**:
   - Manages the menu items.
   - Provides methods to retrieve the list of drinks and find specific drinks.

2. **`CoffeeMaker`**:
   - Handles the resources required to make coffee.
   - Provides reports on the current status of resources.
   - Makes the selected drink if resources are sufficient.

3. **`MoneyMachine`**:
   - Manages monetary transactions.
   - Processes payments and provides reports on the current balance.

---

## How It Works

1. The program initializes objects for the `Menu`, `CoffeeMaker`, and `MoneyMachine` classes.
2. A `while` loop keeps the machine running until the user turns it off.
3. Users can:
   - Enter **`off`** to turn off the machine.
   - Enter **`report`** to view the current status of resources and money.
   - Select a drink from the menu.
4. If a drink is selected:
   - The program checks if there are enough resources to make the drink.
   - If sufficient, it processes the payment and makes the coffee.

---

## Usage

1. Run the `main.py` script.
2. Follow the prompts to interact with the coffee machine:
   - Enter **`off`** to turn off the machine.
   - Enter **`report`** to view the current status.
   - Enter the name of a drink (e.g., `latte`, `espresso`) to order it.
3. The machine will handle the rest, including checking resources, processing payments, and making the coffee.

---

## Example Interaction

```plaintext
What would you like to drink? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 4
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $1.0 in change.
Here is your latte ☕. Enjoy!
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

'''
This script simulates the functionality of a coffee machine using object-oriented programming (OOP). 
It interacts with three main classes: `Menu`, `CoffeeMaker`, and `MoneyMachine`, which are imported 
from their respective modules. The program allows users to select drinks, check the machine's status, 
and turn the machine off.

Classes and their roles:
- `Menu`: Manages the menu items and provides methods to retrieve and find drinks.
- `CoffeeMaker`: Handles the resources required to make coffee and provides reports on resource status.
- `MoneyMachine`: Manages transactions of the money inserted and provides reports on the current balance.

Program Flow:
1. The program initialises objects for `Menu`, `CoffeeMaker`, and `MoneyMachine`.
2. A `while` loop runs as long as the machine is "on".
3. Users can:
   - Enter "off" to turn off the machine.
   - Enter "report" to view the current status of resources and money.
   - Select a drink from the menu.
4. If a drink is selected:
   - The program checks if resources are sufficient.
   - If sufficient, it processes the payment and makes the coffee.

This script demonstrates the use of OOP principles such as encapsulation and modularity, making it 
easy to extend or modify the coffee machine's functionality.
'''


m_m = MoneyMachine() # m_m is an object of MoneyMachine class
c_m = CoffeeMaker() # c_m is an object of CoffeeMaker class
menu = Menu() # menu is an object of Menu class

is_on = True # is_on is a boolean variable to check if the machine is on

while is_on: # while loop to check if the machine is on
    option = menu.get_items() # get_items() method returns the list of items in the menu
    choice = input(f"\nWhat would you like to drink? ({option}): ") # input() function to take input from the user
    if choice == "off": # if the user enters off, the machine will be turned off
        is_on = False # is_on is set to False
    elif choice == "report": # if the user enters report, the machine will print the report of the current status
        c_m.report() 
        m_m.report()
    else:
        drink = menu.find_drink(choice) # find_drink() method returns the drink object from the menu
        # print(drink) # print the drink object
        # print(c_m.is_resource_sufficient(drink)) # print the resource status of the drink
        if c_m.is_resource_sufficient(drink) and m_m.make_payment(drink.cost): # if the resources are sufficient and the payment is successful 
                c_m.make_coffee(drink) # make_coffee() method makes the coffee
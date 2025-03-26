from t_c_menu import MENU

profit = 0
resources = {
    "water": 3000,
    "milk": 3000,
    "cocoa": 1000,
    "coffee": 1000,
    "chocolate powder": 1000,
    "tea": 1000,
    "cup": 1000
}

def is_resource_sufficient(order_ingredients):
    """ Returns True when order can be made, False if ingredients are insufficient. """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """ Returns the total calculated from coins inserted. """
    print("Please insert coins.")
    total = int(input("How many pounds?: ")) * 1.00
    total += int(input("How many fifty pences?: ")) * 0.50
    total += int(input("How many twenty pences?: ")) * 0.20
    total += int(input("How many ten pences?: ")) * 0.10
    total += int(input("How many five pences?: ")) * 0.05
    return total

def is_transaction_successful(money_received, drink_cost):
    """ Return True when the payment is accepted, False if money is insufficient. """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is £{change} in change.")
        global profit # to access the global variable
        profit += drink_cost
        return True
    else:
        print(" Sorry that's not enough money. Money refunded. ")
        return False

def make_coffee(drink_name, order_ingredients):
    """ Deduct the required ingredients from the resources. """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        resources["cup"] -= 1
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True # to keep the machine running

while is_on: 
    print("\nWelcome to the Tea & Coffee machine!")
    print(f"""\nHere is the Menu of your choice: \nEspresso: £1.5\nLatte: £2.50\nCoffee: £2.00\nCappuccino: £3.00\nTea: £1.00\nHot Chocolate: £2.50\nHot Milk: £0.50\nHot Water: £0.50 """)
    choice = input(f"\nWhat would you like to drink? ").lower()
    if choice.lower() == "off":
        is_on = False # to turn off the machine
        break
    elif choice.lower() == "report": # to check the resources
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Cocoa: {resources['cocoa']}g")
        print(f"Chocolate Powder: {resources['chocolate powder']}g")
        print(f"Tea: {resources['tea']}g")
        print(f"Cup: {resources['cup']}")
        print(f"\nMoney: £{profit}\n")
    else:
        drink = MENU[choice] # get the drink from the MENU
        if is_resource_sufficient(drink["ingredients"]): # check if resources are sufficient
            payment = process_coins() # get the payment
            if is_transaction_successful(payment, drink["cost"]): # check if payment is successful
                make_coffee(choice, drink["ingredients"]) # make the coffee                
    
    ret = input("\nDo you want to order again? yes(y) / no(n): ").lower()
    if ret.lower() == "n":
        is_on = False # to turn off the machine
        break
    else:
        continue


print("\nThank you for using the tea/ coffee machine!") # end of the program



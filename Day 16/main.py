from art import logo
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()


def coffee():
    print(logo)
    item = None
    choice = input("\nWhat would you like? " + menu.get_items() + ": ")
    if choice == 'off':
        print("\nPower off!")
        return False
    elif choice == "report":
        coffeeMachine.report()
        moneyMachine.report()
    else:
        item = menu.find_drink(choice)
    if item is None:
        return True
    else:
        if coffeeMachine.is_resource_sufficient(item):
            if moneyMachine.make_payment(item.cost):
                coffeeMachine.make_coffee(item)
        else:
            if input("Refilled resources? (y/n): ") == 'y':
                coffeeMachine.refill_resources()
    return True


power = True
while power:
    power = coffee()

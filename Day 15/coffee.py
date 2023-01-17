import art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}


def take_coins():
    print("Please feed coins!")
    quarters = int(input("Enter number of Quarters: "))
    dimes = int(input("Enter number of Dimes: "))
    nickel = int(input("Enter number of Nickels: "))
    penny = int(input("Enter number of Pennies: "))
    return quarters, dimes, nickel, penny


def refill_resources():
    resources['water'] = 1000
    resources['milk'] = 1000
    resources['coffee'] = 500


def report():
    for i in resources:
        if i == 'money':
            print("{}: ${}".format(i, resources[i]))
        print("{}: {}".format(i, resources[i]))


def check_amount(item, a, b, c, d):
    total = (a * 25 + b * 10 + c * 5 + d * 1) / 100
    if total >= MENU[item]['cost']:
        return total - MENU[item]['cost'], True
    else:
        return 0, False


def check_resources(item):
    w = True
    m = True
    c = True
    if 'water' in MENU[item]['ingredients']:
        if resources['water'] >= MENU[item]['ingredients']['water']:
            resources['water'] = resources['water'] - MENU[item]['ingredients']['water']
            w = True
        else:
            print("\nNot enough Water.")
            w = False
    if 'milk' in MENU[item]['ingredients']:
        if resources['milk'] >= MENU[item]['ingredients']['milk']:
            resources['milk'] = resources['milk'] - MENU[item]['ingredients']['milk']
            m = True
        else:
            print("\nNot enough Milk.")
            m = False
    if 'coffee' in MENU[item]['ingredients']:
        if resources['coffee'] >= MENU[item]['ingredients']['coffee']:
            resources['coffee'] = resources['coffee'] - MENU[item]['ingredients']['coffee']
            c = True
        else:
            print("\nNot enough Coffee.")
            c = False
    return w and m and c


def coffee(x):
    print(art.logo)
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        print("\nPower off!")
        return False
    if choice == "report":
        report()
    elif choice not in MENU:
        print("\nInvalid choice!")
    else:
        if check_resources(choice):
            quarters, dimes, nickel, penny = take_coins()
            balance, amount = check_amount(choice, quarters, dimes, nickel, penny)
            if amount:
                print("\nHere is your {} ☕. Enjoy!".format(choice))
                resources["money"] = resources["money"] + MENU[choice]['cost']
                if balance > 0:
                    print("Here is your ${} change.".format(balance))
            else:
                print("\nSorry, that's not enough money. {} is ${}.".format(choice, MENU[choice]['cost']))
                print("Money you have given is refunded. Please collect it.")
        else:
            refilled = False
            while not refilled:
                if input("\nRefilled resources? (If yes, type 'y'): ") == 'y':
                    refilled = True
                    refill_resources()
                    print("Refilled!")
    return True


power = True
resources["money"] = 0
while power:
    power = coffee(power)

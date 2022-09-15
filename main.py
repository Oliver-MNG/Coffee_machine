from art import logo

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def monkey_business(menu, order, resources):
    resources['water'] -= menu[order]['ingredients']['water']
    resources['coffee'] -= menu[order]['ingredients']['coffee']
    if order == 'latte' or order == 'cappuccino':
        resources['milk'] -= menu[order]['ingredients']['milk']
    print("Please insert coins.")
    a = int(input("how many quarters?: "))
    b = int(input("how many dimes?: "))
    c = int(input("how many nickles?: "))
    d = int(input("how many pennies?: "))
    money = a * 0.25 + b * 0.1 + c * 0.05 + d * 0.01
    order_cost = menu[order]['cost']
    change = "{:.2f}".format(float(money - order_cost))
    if money >= order_cost:
        print(f"Here is ${change} in change.")
        print(f"Here is your {order}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


balance = 0
on = True
while on:
    print(logo)
    order = input("What would you like? espresso/latte/cappuccino : ")
    if order == 'espresso':
        if MENU[order]['ingredients']['water'] <= resources['water'] and MENU[order]['ingredients']['coffee'] <= resources['coffee']:
            monkey_business(MENU, order, resources)
            balance += MENU[order]['cost']
        else:
            print("Sorry there is not enough resources.")
    elif order == 'latte':
        if MENU[order]['ingredients']['water'] <= resources['water'] and MENU[order]['ingredients']['coffee'] <= resources['coffee'] and MENU[order]['ingredients']['coffee']:
            monkey_business(MENU, order, resources)
            balance += MENU[order]['cost']
        else:
            print("Sorry there is not enough resources.")
    elif order == 'cappuccino':
        if MENU[order]['ingredients']['water'] <= resources['water'] and MENU[order]['ingredients']['coffee'] <= resources['coffee'] and MENU[order]['ingredients']['coffee']:
            monkey_business(MENU, order, resources)
            balance += MENU[order]['cost']
        else:
            print("Sorry there is not enough resources.")
    elif order == 'report':
        print(f"Water: {resources['water']},\nMilk: {resources['milk']},\nCoffee: {resources['coffee']},\nProfit: {balance}")
    else:
        on = False





















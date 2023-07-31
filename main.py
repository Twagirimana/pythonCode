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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_resources(order_ingredients):
    for n in order_ingredients:
        if order_ingredients[n] >= resources[n]:
            print(f"sorry there is not enough {n}")
            return False
    return True

def pay_coin():
    print("input coin")
    total = int(input("how many quarters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickels?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total

def transaction(money_received, price):
    if money_received >= price:
        change = round(money_received - price, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += price
        return True
    else:
        print("sorry that is not enough money. money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    for n in order_ingredients:
        resources[n] -= order_ingredients[n]
    print(f"Here is your {drink_name}!")


On = True
while On:
    choice = input("what would you like?(espresso/latte/cappuccino):")
    if choice == "off":
        On = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = pay_coin()
            if transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])











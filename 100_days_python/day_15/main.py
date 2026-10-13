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
money = 0
cofee_machine=True
def money_calculation(cost):
    '''Returns the total calculated from coins inserted''' 
    print("Please insert coins")
    quarts = int(input(f"How many quarters?:  "))
    dimes = int(input(f"How many dimes?:  "))
    nickles = int(input(f"How many nickles?:  "))
    pennies = int(input(f"How many pennies?:  "))
    total = (0.25*quarts) + (0.1 * dimes) + (0.05*nickles) + (0.01*pennies)
    print(total)

    if cost>total:
        return -1
    elif cost<total:
        return total-cost
    else:
        return 0

def make_cofee(ingrediants, cost):
    resources["water"] -= ingrediants['water']
    resources["milk"] -= ingrediants.get('milk',0)
    resources["coffee"] -= ingrediants['coffee']
    global money
    money = cost


def check_resources(ingredients):
    for item in ingredients:
        if (resources[item]<ingradients.get(item, 0)):
            return "Sorry, there is not enough {item}."

    return None;


while cofee_machine :
    user_data = input("What would you like? (espresso/latte/cappuccino):  ").lower()
    if user_data in MENU:
        ingradients= MENU[user_data]['ingredients']
        cost = MENU[user_data]['cost']
        error = check_resources(ingradients)
        if error:
            print(error)
        else:
            price_check = money_calculation(cost)
            if price_check>=0:
                make_cofee(ingradients, cost)
                print(f"Here is ${price_check:.2f} in change")
                print(f"Here is your {user_data}. Enjoy!.")
            elif price_check ==-1:
                print(f"​Sorry that's not enough money. Money refunded.")

    elif user_data == 'report':
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${money}")
    elif user_data == 'off':
        cofee_machine=False
    else:
        print("You have choose wrong option")
        cofee_machine = False

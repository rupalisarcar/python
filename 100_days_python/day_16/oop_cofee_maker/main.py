from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

cofee_machine_start = True

while cofee_machine_start:
    get_item = menu.get_items()
    cofee_type = input(f"What would you like? ({get_item}):  ").lower()
    if cofee_type == "report":
        coffee_maker.report()
        money_machine.report()
    elif cofee_type=='off':
        cofee_machine_start=False
    else :
        item = menu.find_drink(order_name = cofee_type)
        if coffee_maker.is_resource_sufficient(item) and money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)


    # 

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    option = input(f"What would you like? ({menu.get_items()}): ")
    if option == "off":
        break

    if option == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(option)

        if drink and coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)

    print()

from typing import Dict
from textwrap import dedent

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


def show_menu() -> None:
    print(" MENU ".center(35, "*"))
    for coffee, data in MENU.items():
        print(f"{coffee.capitalize()} ".ljust(30, "-"), f"${data['cost']}")


def report(data: Dict[str, float]) -> None:
    print(dedent("""
        Water: {water}ml
        Milk: {milk}ml
        Coffee: {coffee}g
        Money: ${money}
    """).format(**data), end="")


def request_payment() -> float:
    coins, total = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}, 0
    print("Please insert coins.")
    for coin, value in coins.items():
        while True:
            try:
                total += float(input(f"How many {coin} (${value:.2f})? ")) * value
            except ValueError:
                print("Error: You did not enter a value.")
            else:
                break

    return total


def sufficient_money(drink: str, amount: float) -> bool:
    return amount >= MENU[drink]["cost"]


def have_enough_resources(drink: str, resources: Dict[str, float]) -> bool:
    for ingredient, total_available in MENU[drink]["ingredients"].items():
        if resources[ingredient] < total_available:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def make_coffee(drink: str, resources: Dict[str, float]) -> None:
    for ingredient, total_available in MENU[drink]["ingredients"].items():
        resources[ingredient] -= total_available

    print(f"Here is your {drink}. Enjoy!")


def check_change(drink: str, money: float):
    change = abs(MENU[drink]["cost"] - money)
    print(f"Here is ${change:.2f} in change.")


def main():
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
    }
    money = 0

    while True:
        show_menu()
        option = input(f"\nWhat would you like? ").lower()

        if option == "off":
            break

        if option in MENU.keys():
            if have_enough_resources(option, resources):
                payment_amount = request_payment()
                print()

                if sufficient_money(option, payment_amount):
                    money += MENU[option]["cost"]
                    check_change(option, payment_amount)
                    make_coffee(option, resources)
                else:
                    print("Sorry that's not enough money. Money refunded.")

        elif option == "report":
            report({**resources, "money": money})
        else:
            print("Error: Invalid option. Choose a drink from the menu.")

        print()


if __name__ == "__main__":
    main()

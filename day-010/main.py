import art
from typing import Dict, Callable


def add(n1: float, n2: float) -> float:
    return n1 + n2


def subtract(n1: float, n2: float) -> float:
    return n1 - n2


def multiply(n1: float, n2: float) -> float:
    return n1 * n2


def divide(n1: float, n2: float) -> float:
    return n1 / n2


def ask_value(msg) -> float:
    try:
        value = float(input(msg).strip())
    except ValueError:
        raise ValueError("You did not enter a number")

    return value


def ask_operation(operations: Dict[str, Callable[[float, float], float]]) -> str:
    operation = input(f"Pick an operation ({'|'.join(operations.keys())}): ")

    if operation in operations.keys():
        return operation

    raise ValueError("Invalid operation")


def clear_console() -> None:
    print("\033[H\033[J", end="")


def format_error(content) -> str:
    return "{red_color}Error: {msg}.{reset}".format(red_color="\033[1;31m", msg=content, reset="\033[m")


def calculator(operations: Dict[str, Callable[[float, float], float]]):
    clear_console()
    print(art.LOGO)

    result = None

    while True:
        print()

        try:
            num1 = ask_value("First number: ") if result is None else result
            operation_symbol = ask_operation(operations)
            num2 = ask_value("Next number: ")

            result = operations[operation_symbol](num1, num2)
        except Exception as error:
            print(format_error(error))
        else:

            print(f"\n{num1} {operation_symbol} {num2} = {result}\n")

            option = None
            while option not in ("U", "N", "E"):
                option = input(f"Type 'U' to calculation with {result:.2f}, " 
                               "'N' to start new calculation or 'E' to exit: ").upper()
            if option == "E":
                return

            if option == "N":
                calculator(operations)
                return


if __name__ == "__main__":
    calculator({
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    })

    print("\nGoodbye!")

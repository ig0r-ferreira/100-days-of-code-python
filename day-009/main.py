import art


def ask_name() -> str:
    name = input("What is your name? ").upper()
    
    if not name.replace(" ", "").isalpha():
        raise ValueError("You did not enter a name.")
        
    return name.strip()


def ask_bid_value() -> float:
    try:
        value = float(input("What is your bid? $").strip())
    except ValueError:
        raise ValueError("You did not enter a value.")

    if value <= 0:
        raise ValueError("The value must be greater than zero.")

    return value


def clear_console() -> None:
    print("\033[H\033[J", end="")


def format_error(content) -> str:
    return "{red_color}Error: {msg}{reset}".format(red_color="\033[1;31m", msg=content, reset="\033[m")    


def get_inputs() -> list:
    args = []
    
    for entry_request in [ask_name, ask_bid_value]:
        while True:
            try:
                args.append(entry_request())
            except Exception as error:
                print(format_error(error))
            else:
                break
    
    return args


if __name__ == "__main__":
    bids_per_person = {}
    
    while True:
        print(f"{art.LOGO}\nBlind auction\n")

        name, bid_value = get_inputs()
        bids_per_person[name] = bid_value

        print()

        should_continue = None
        while should_continue not in ("Y", "N"):
            should_continue = input("Are there other bidders? (Y/N)? ").upper()

        if should_continue == "N":
            break

        clear_console()
    
    winner = sorted(bids_per_person, key=bids_per_person.get, reverse=True)[0]
    print(f"The winner is {winner} with a bid of ${bids_per_person[winner]:.2f}.")
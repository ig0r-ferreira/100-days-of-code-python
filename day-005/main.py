# Password Generator Project
import random
from string import ascii_letters, digits


def print_error(error):
    print(f"\033[1;31mError: {error}\033[m")


def request_value(msg):
    while True:
        try:
            num = int(input(msg))
        except ValueError:
            print_error("You did not enter a number.")
        else:
            if num > 0: return num
            print_error("The minimum value is 1.")


def generate_password(num_letters, num_symbols, num_digits):
    allowed_symbols = ("!", "#", "$", "%", "&", "(", ")", "*", "+")
    
    randomchars = lambda charset, number: random.sample(charset, k=number)

    if not 32 >= (num_letters + num_symbols + num_digits) >= 8:
        raise ValueError("Password must be 8 to 32 characters long.")
    
    chars = randomchars(ascii_letters, num_letters) + \
            randomchars(allowed_symbols, num_symbols) + \
            randomchars(digits, num_digits)
    
    random.shuffle(chars)
    password = "".join(chars)
    
    return password


if __name__ == "__main__":    
    print("Welcome to the Password Generator!\n")
    while True:
        num_letters = request_value("How many letters would you like in your password? ")
        num_symbols = request_value("How many symbols would you like? ")
        num_digits = request_value("How many numbers would you like? ")
        
        try:
            password = generate_password(num_letters, num_symbols, num_digits)
        except ValueError as error:
            print_error(error)
            confirm_msg = "Do you want to try again"
        else:
            print(f"\nHere is your password: {password}")
            confirm_msg = "Want to generate another"

        print()
        
        continue_ = None
        while continue_ not in ("Y", "N"):
            continue_ = input(f"{confirm_msg} (Y/N)? ").upper()
        
        print()

        if continue_ == "N":
            break

    print("Thanks for using the password generator. Until next time.")
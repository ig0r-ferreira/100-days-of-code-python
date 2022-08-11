from random import randint
import art


MIN_VALUE, MAX_VALUE = 1, 100
DIFFICULTY = {
   "easy": 10,
   "hard": 5 
}

TITLE_SCREEN = f"""
{art.LOGO}
Welcome to the Number Guessing Game!
I'm thinking of a number between {MIN_VALUE} and {MAX_VALUE}.
"""


def set_difficulty() -> str:
    chosen_mode = None
    while chosen_mode not in DIFFICULTY.keys():
        chosen_mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    return chosen_mode


def ask_for_guess(number_list:'list[int]') -> int:
    try:
        number = int(input("Make a guess: "))
    except ValueError:
        raise ValueError("You didn't enter a number.")
    
    if not (MAX_VALUE >= number >= MIN_VALUE):
        raise ValueError("The number is outside the defined range.")
    
    if number in number_list:
        raise ValueError("You already guessed that number. Try another.")
    
    return number


def clear_console() -> None:
    print("\033[H\033[J", end="")


def format_error(content:str) -> str:
    return "{red_color}Error: {msg}{reset}".format(red_color="\033[1;31m", msg=content, reset="\033[m")


def play_game():
    print(TITLE_SCREEN)

    secret_number = randint(MIN_VALUE, MAX_VALUE)
    mode = set_difficulty()

    guess_list = []
    for attempt in range(DIFFICULTY[mode], 0, -1):
        while True:
            print(f"\nYou have {attempt} attempts remaining to guess the number.")
            try:
                number_guess = ask_for_guess(guess_list)
            except Exception as error:
                print(format_error(error))
            else:
                guess_list.append(number_guess)
                break
        
        if number_guess == secret_number:
            print("\nYou guessed right. Very well!")
            break
        
        print("Too", "high." if number_guess > secret_number else "low.")
    else:
        print(f"\nYour chances are over, you lost. The answer is {secret_number}.")


if __name__ == "__main__":
    while True:
        play_game()
        
        print()
        
        play_again = None
        while play_again not in ("y", "n"):
            play_again = input("Want to play again (y/n)? ").lower()

        if play_again == "n":
            break
        
        clear_console()

    print("\nUntil next time!")        

import random
import os


def request_option():
    while True:
        choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n=> ").strip()

        if choice in ('0', '1', '2'):
            return int(choice)
        
        print("{red}Error: Invalid number. Try again!{reset}".format(**font_colors))


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [
    {
        'figure': ROCK,
        'weakness': 1
    },
    {
        'figure': PAPER,
        'weakness': 2
    },
    {
        'figure': SCISSORS,
        'weakness': 0
    }
]

font_colors = {
    'red': '\033[1;31m',
    'green': '\033[1;32m',
    'yellow': '\033[1;33m',
    'reset': '\033[m'
}

if __name__ == "__main__":
    print("Welcome to the Rock, Paper, Scissors game", end="\n\n")
    
    while True:
        user_choice = request_option()
        print(f"\nYou chose:\n{options[user_choice]['figure']}")

        computer_choice = random.randrange(0, len(options))
        print(f"Computer chose:\n{options[computer_choice]['figure']}")

        if user_choice == computer_choice:
            result = "{yellow}It's a draw!"
        elif user_choice == options[computer_choice]['weakness']:
            result = "{green}You win!"
        else:
            result = "{red}You lose!"

        result += "{reset}"
        print(result.format(**font_colors), end="\n\n")

        continue_game = None
        while continue_game not in ('Y', 'N'):
            continue_game = input("Do you want to play again? [Y/N]: ").strip().upper()

        if continue_game == 'N':
            print("\n\nGame Over!")
            break

        clear()

import random
from hangman_words import WORD_LIST
from hangman_art import STAGES, LOGO


def random_word(word_list:'list[str]') -> str:
    return random.choice(word_list)


def clear_console() -> None:
    print("\033[H\033[J", end="")


def hangman() -> None:

    def show_title() -> None:
        print(f"{LOGO}\n\nThe word has {word_length} letters.\n\n")


    secret_word = random_word(WORD_LIST).upper()
    word_length = len(secret_word)
    display, guessed_letters = ["_"] * word_length, []
    hits, lives = 0, 6

    show_title()
    
    while hits < word_length and lives > 0:
        guess = input("Guess a letter: ").strip().upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print(f"'{guess}' is not a letter. Try again!")
            continue

        if guess in guessed_letters:
            print("You have already used that letter. Try another!")
            continue
        
        clear_console()
        show_title()

        guessed_letters.append(guess)
        occurs_in_word = 0

        for pos in range(word_length):
            if secret_word[pos] == guess:
                display[pos] = guess
                occurs_in_word += 1
        
        if not occurs_in_word:
            lives -= 1
            print(f"The letter '{guess}', is not in the word. You lost one life, {lives} left.")
        else:
            hits += occurs_in_word
            print("Very good! You guessed a letter.")

        print(STAGES[lives])
        print(*display, end='\n\n')


    if lives:
        print("You barely survived, congratulations.")
    else:
        print(f"You died.\nThe word is: {secret_word}.")  
  

if __name__ == "__main__":
    hangman()
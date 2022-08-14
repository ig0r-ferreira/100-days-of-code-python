import art


def caesar_cipher(cipher_direction: str, start_text: str, shift_amount: int) -> str:
    # noinspection PyPep8Naming
    final_text, TOTAL_LETTERS, INT_A, INT_Z_PLUS_ONE = "", 26, 97, 123
    
    shift_amount %= TOTAL_LETTERS 
    # Changes the signal according to the direction
    shift_amount *= (-1) ** (cipher_direction == "decode")

    for char in start_text:
        int_char = ord(char)
        
        # Encodes only unaccented alphabetic characters
        if INT_Z_PLUS_ONE > int_char >= INT_A:
            int_char += shift_amount
            
            if INT_Z_PLUS_ONE > int_char >= INT_A:
                pass
            elif int_char >= INT_Z_PLUS_ONE:
                int_char = INT_A + int_char % INT_Z_PLUS_ONE
            else:
                int_char = INT_Z_PLUS_ONE - INT_A % int_char

            final_text += chr(int_char)
        else:
            final_text += char
            
    return final_text


def ask_direction() -> str:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    
    if direction not in ("encode", "decode"):
        raise ValueError("Invalid option. Choose between 'encode' or 'decode' only.")

    return direction


def ask_message() -> str:
    msg = input("Type your message: ").lower()
    
    if not msg:     
        raise ValueError("The message is empty.")
    
    return msg


def ask_shift() -> int:
    try:
        shift = int(input("Type the shift number: "))
    except ValueError:
        raise ValueError("You didn't enter a number.")
    
    if shift < 1: 
        raise ValueError("The number must be greater than zero.")

    return shift


def clear_console() -> None:
    print("\033[H\033[J", end="")


def format_error(content):
    return "{red_color}Error: {msg}{reset}".format(red_color="\033[1;31m", msg=content, reset="\033[m")


if __name__ == "__main__":    
    while True:
        print(art.LOGO)

        args = []
        for funct in [ask_direction, ask_message, ask_shift]:
            while True:
                try:
                    args.append(funct())
                except Exception as error:
                    print(format_error(error))
                else:
                    break
            
        result = caesar_cipher(*args)
        print(f"{args[0].capitalize()}d text: {result}\n")
        
        continue_ = None
        while continue_ not in ("Y", "N"):        
            continue_ = input("Do you want to continue (Y/N)? ").upper()

        if continue_ == "N": 
            break

        clear_console()
    
    print("\nGoodbye!")

import pandas


def main() -> None:
    df_nato_alphab = pandas.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {key: value for _, key, value in df_nato_alphab.itertuples()}

    while True:
        word = input("Enter a word [type 0 to exit]: ").strip().upper()
        if word == "0":
            break

        if word == "":
            print("No words have been entered.")
        elif len(word) < 2:
            print("You have entered a character. Please enter a word.")
        elif not word.isalpha():
            print("Sorry, only letters of the alphabet please.")
        else:
            nato_words = ", ".join(map(phonetic_dict.get, word))
            print(nato_words)


if __name__ == "__main__":
    main()

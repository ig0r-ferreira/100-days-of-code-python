import pandas


def main() -> None:
    df_nato_alphab = pandas.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {key: value for _, key, value in df_nato_alphab.itertuples()}

    while True:
        word = input("Enter a word [type 0 to exit]: ").strip().upper()
        if word == "0":
            break
        if len(word) < 2 or not word.isalpha():
            print("Error: You didn't enter a word.")
        else:
            nato_word = ", ".join(map(phonetic_dict.get, word))
            print(nato_word)


if __name__ == "__main__":
    main()

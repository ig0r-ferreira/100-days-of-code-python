from typing import List


def read_lines_from(path: str) -> List[str]:
    with open(path) as file:
        content = [line.rstrip() for line in file]

    return content


def write_file(path: str, content: str) -> None:
    with open(path, "w") as file:
        file.write(content)


def main() -> None:
    names = read_lines_from(r".\Input\Names\invited_names.txt")
    letter_template = "\n".join(read_lines_from(r".\Input\Letters\starting_letter.txt"))

    for name in names:
        write_file(fr".\Output\ReadyToSend\letter_for_{name}.txt", letter_template.replace("[name]", name))


if __name__ == "__main__":
    main()

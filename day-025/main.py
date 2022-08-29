import turtle
import csv
from typing import List, Dict, Tuple, Any
from functools import partial

Coord = Tuple[float, float]


def load_brazil_states() -> Dict[str, Coord]:
    with open("states_data.csv", encoding="utf-8") as file:
        file.readline()
        reader = csv.DictReader(file, fieldnames=("state", "x", "y"))
        return {row["state"]: (row["x"], row["y"]) for row in reader}


def save_unguessed_states(missing_states: List[List[str]]) -> None:
    with open("states_to_learn.csv", mode="w", encoding="utf-8", newline="\n") as file:
        writer = csv.writer(file)
        writer.writerow(["state"])
        writer.writerows(missing_states)


def game_over() -> None:
    turtle.home()
    turtle.write("GAME OVER", align="center", font=("Arial", 24, "bold"))


def ask_for_state(data_states: Dict[str, Any], window_name: str = "Guess a state", guessed_states=None) -> None:
    answer_state = turtle.textinput(title=window_name, prompt="Enter the name of a state: ")
    answer_state = answer_state is not None and answer_state.strip().title()

    if not answer_state or data_states.get(answer_state) is None:
        guessed_states = guessed_states or {}
        missing_states = [[state] for state in data_states.keys() if state not in guessed_states]

        save_unguessed_states(missing_states)
        game_over()
        return

    x, y = map(float, data_states[answer_state])
    turtle.goto(x, y)
    turtle.write(answer_state, align="center", font=("Arial", 10, "normal"))

    if guessed_states is None:
        guessed_states = []

    guessed_states.append(answer_state)
    new_window_name = f"{len(guessed_states)}/{len(data_states)} States Correct"

    if len(guessed_states) < 26:
        turtle.ontimer(partial(ask_for_state, data_states, new_window_name, guessed_states), 100)
    else:
        game_over()


def main() -> None:
    window = turtle.Screen()
    window.title("Brazil states")
    window.setup(width=680, height=568)
    window.bgpic("brazil_map.png")

    turtle.penup()
    turtle.hideturtle()

    states = load_brazil_states()
    ask_for_state(data_states=states)
    window.mainloop()


if __name__ == "__main__":
    main()

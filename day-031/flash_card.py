import tkinter as tk
import pandas as pd
import random


class FlashCardApp(tk.Tk):
    BG_COLOR = "#B1DDC6"
    CARD_FRONT_FONT = "#000000"
    CARD_BACK_FONT = "#d21034"
    CARD_TITLE_FONT = ("Arial", 40, "italic")
    CARD_WORD_FONT = ("Arial", 60, "bold")
    PROGRESS_FILE_PATH = "data/words_to_learn.csv"
    ENGLISH_WORDS_FILE_PATH = "data/english_words.csv"
    WRONG_IMG_PATH = "img/wrong.png"
    RIGHT_IMG_PATH = "img/right.png"
    CARD_FRONT_IMG_PATH = "img/card_front.png"
    CARD_BACK_IMG_PATH = "img/card_back.png"

    def __init__(self) -> None:
        super().__init__()
        self.title("Flash Card")
        self.config(bg=self.BG_COLOR, padx=50, pady=80)
        self.resizable(False, False)

        self.card_front_img: tk.PhotoImage | None = None
        self.card_back_img: tk.PhotoImage | None = None
        self.card_canvas: tk.Canvas | None = None
        self.check_img: tk.PhotoImage | None = None
        self.known_button: tk.Button | None = None
        self.cross_img: tk.PhotoImage | None = None
        self.unknown_button: tk.Button | None = None
        self.english_dict: list[dict[str, str]] | None = None
        self.card_bg_img_id: int | None = None
        self.card_title_id: int | None = None
        self.card_word_id: int | None = None
        self.flip_timer: str | None = None
        self.current_card: dict[str, str] | None = None

        self.create_widgets()
        self.load_english_dict()
        self.next_card()

    def create_widgets(self) -> None:
        self.card_front_img = tk.PhotoImage(file=self.CARD_FRONT_IMG_PATH)
        self.card_back_img = tk.PhotoImage(file=self.CARD_BACK_IMG_PATH)
        self.card_canvas = tk.Canvas(
            width=self.card_front_img.width(), height=self.card_front_img.height(), highlightthickness=0,
            bg=self.BG_COLOR
        )

        x_pos, y_pos = self.card_front_img.width() / 2, self.card_front_img.height() / 2
        self.card_bg_img_id = self.card_canvas.create_image(x_pos, y_pos, image=self.card_front_img)
        self.card_title_id = self.card_canvas.create_text(x_pos - 10, y_pos - 100, font=self.CARD_TITLE_FONT)
        self.card_word_id = self.card_canvas.create_text(x_pos - 10, y_pos, font=self.CARD_WORD_FONT)
        self.card_canvas.grid(row=0, column=0, columnspan=2)

        self.cross_img = tk.PhotoImage(file=self.WRONG_IMG_PATH)
        self.unknown_button = tk.Button(
            image=self.cross_img, highlightthickness=0, command=lambda button_id="unknown": self.next_card(button_id)
        )
        self.unknown_button.grid(row=1, column=0)

        self.check_img = tk.PhotoImage(file=self.RIGHT_IMG_PATH)
        self.known_button = tk.Button(
            image=self.check_img, highlightthickness=0, command=lambda button_id="known": self.next_card(button_id)
        )
        self.known_button.grid(row=1, column=1)

    def load_english_dict(self) -> None:
        try:
            data = pd.read_csv(self.PROGRESS_FILE_PATH)
        except FileNotFoundError:
            data = pd.read_csv(self.ENGLISH_WORDS_FILE_PATH)

        self.english_dict = data.to_dict(orient="records")

    def next_card(self, id_button: str = None) -> None:
        if self.flip_timer:
            self.after_cancel(self.flip_timer)

        if id_button == "known":
            self.save_progress()

        self.current_card = random.choice(self.english_dict)
        self.card_canvas.itemconfig(self.card_bg_img_id, image=self.card_front_img)
        self.card_canvas.itemconfig(self.card_title_id, text="English", fill=self.CARD_FRONT_FONT)
        self.card_canvas.itemconfig(self.card_word_id, text=self.current_card.get("en"), fill=self.CARD_FRONT_FONT)

        self.flip_timer = self.after(3000, func=lambda card=self.current_card: self.flip_card(self.current_card))

    def flip_card(self, card: dict[str, str]) -> None:
        self.card_canvas.itemconfig(self.card_bg_img_id, image=self.card_back_img)
        self.card_canvas.itemconfig(self.card_title_id, text="Brazilian portuguese", fill=self.CARD_BACK_FONT)
        self.card_canvas.itemconfig(self.card_word_id, text=card.get("pt-br"), fill=self.CARD_BACK_FONT)

    def save_progress(self) -> None:
        self.english_dict.remove(self.current_card)
        pd.DataFrame(self.english_dict).to_csv(self.PROGRESS_FILE_PATH, index=False)

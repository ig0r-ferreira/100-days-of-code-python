import tkinter as tk
import tkinter.ttk as tkk
from tkinter import font


class PasswordManager(tk.Tk):
    WHITE_COLOR: str = "white"
    RED_COLOR: str = "#A10035"
    FONT_CONFIG: dict = {
        "family": "Verdana",
        "size": 11
    }

    def __init__(self) -> None:
        super().__init__()
        self.title("Password Manager")
        self.bg_img = None
        self.img_canvas = None
        self.website_label = None
        self.website_input = None
        self.username_label = None
        self.username_input = None
        self.password_input = None
        self.password_label = None
        self.generate_password_button = None
        self.add_password_button = None

        tkk.Style().configure('pad.TEntry', padding=(5, 4, 0, 4))
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.config(**self.FONT_CONFIG)
        self.option_add("*Font", self.defaultFont)
        self.config(pady=80, padx=60)
        self.create_widgets()

    def create_widgets(self) -> None:
        self.bg_img = tk.PhotoImage(file="logo.png")
        self.img_canvas = tk.Canvas(width=self.bg_img.width(), height=self.bg_img.height(), highlightthickness=0)
        x_pos, y_pos = self.bg_img.width() / 2, self.bg_img.height() / 2
        self.img_canvas.create_image(x_pos, y_pos, image=self.bg_img)

        self.website_label = tk.Label(text="Website")
        self.website_input = tkk.Entry(width=46, style="pad.TEntry")
        self.website_input.focus()

        self.username_label = tk.Label(text="Email/Username")
        self.username_input = tkk.Entry(width=46, style="pad.TEntry")

        self.password_label = tk.Label(text="Password")
        self.password_input = tkk.Entry(width=28, style="pad.TEntry")

        self.generate_password_button = tk.Button(text="Generate Password")
        self.add_password_button = tk.Button(text="Add", bg=self.RED_COLOR, fg=self.WHITE_COLOR)

        self.img_canvas.grid(row=0, column=1, pady=(0, 30))
        self.website_label.grid(row=1, column=0, padx=5, sticky="w")
        self.website_input.grid(row=1, column=1, columnspan=2, sticky="ew", pady=5)
        self.username_label.grid(row=2, column=0, padx=5, sticky="w")
        self.username_input.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
        self.password_label.grid(row=3, column=0, padx=5, sticky="w")
        self.password_input.grid(row=3, column=1, sticky="we", pady=5, padx=(0, 10))
        self.generate_password_button.grid(row=3, column=2, sticky="e")
        self.add_password_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=5)

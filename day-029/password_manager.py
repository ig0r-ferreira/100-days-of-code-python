import tkinter as tk
from tkinter import font, ttk, messagebox
import json
import random
from string import ascii_letters, digits


def get_credentials(key=None) -> dict[str, dict[str, str]] | None:
    try:
        with open(file="data.json", mode="r", encoding="utf-8") as data_file:
            data = json.load(data_file)
            return key is None and data or data.get(key)
    except FileNotFoundError:
        return None


class PasswordManager(tk.Tk):
    WHITE_COLOR: str = "#FFFFFF"
    RED_COLOR: str = "#A10035"
    FONT_CONFIG: dict = {
        "family": "Verdana",
        "size": 11
    }

    def __init__(self) -> None:
        super().__init__()
        self.title("Password Manager")
        self.config(pady=80, padx=60)
        self.resizable(False, False)

        # Add padding in Entries
        ttk.Style().configure('pad.TEntry', padding=(5, 4, 0, 4))

        # Set default font
        default_font = font.nametofont("TkDefaultFont")
        default_font.config(**self.FONT_CONFIG)
        self.option_add("*Font", default_font)

        self.bg_img: tk.PhotoImage | None = None
        self.img_canvas: tk.Canvas | None = None
        self.website_label: tk.Label | None = None
        self.username_label: tk.Label | None = None
        self.password_label: tk.Label | None = None
        self.website_entry: ttk.Entry | None = None
        self.username_entry: ttk.Entry | None = None
        self.password_entry: ttk.Entry | None = None
        self.search_credentials_button = None
        self.generate_password_button: tk.Button | None = None
        self.add_password_button: tk.Button | None = None

        self.create_widgets()

    def create_widgets(self) -> None:
        self.bg_img = tk.PhotoImage(file="img/logo.png")
        self.img_canvas = tk.Canvas(width=self.bg_img.width(), height=self.bg_img.height(), highlightthickness=0)
        x_pos, y_pos = self.bg_img.width() / 2, self.bg_img.height() / 2
        self.img_canvas.create_image(x_pos, y_pos, image=self.bg_img)

        self.website_label = tk.Label(text="Website")
        self.website_entry = ttk.Entry(width=28, style="pad.TEntry")
        self.website_entry.focus()
        self.search_credentials_button = tk.Button(
            text="Search", command=self.search_credential
        )

        self.username_label = tk.Label(text="Email/Username")
        self.username_entry = ttk.Entry(width=46, style="pad.TEntry")

        self.password_label = tk.Label(text="Password")
        self.password_entry = ttk.Entry(width=28, style="pad.TEntry")

        self.generate_password_button = tk.Button(
            text="Generate Password", command=self.generate_password
        )
        self.add_password_button = tk.Button(
            text="Add", bg=self.RED_COLOR, fg=self.WHITE_COLOR, command=self.save_password
        )

        self.img_canvas.grid(row=0, column=1, pady=(0, 30))
        self.website_label.grid(row=1, column=0, padx=5, sticky="w")
        self.website_entry.grid(row=1, column=1, sticky="we", pady=5, padx=(0, 10))
        self.search_credentials_button.grid(row=1, column=2, sticky="we")
        self.username_label.grid(row=2, column=0, padx=5, sticky="w")
        self.username_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=5)
        self.password_label.grid(row=3, column=0, padx=5, sticky="w")
        self.password_entry.grid(row=3, column=1, sticky="we", pady=5, padx=(0, 10))
        self.generate_password_button.grid(row=3, column=2, sticky="we")
        self.add_password_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=5)

    def save_password(self) -> None:

        user_inputs = self.get_user_inputs()
        website = user_inputs.pop("website").title()
        credential = get_credentials(website)

        if not credential and not self.has_empty_fields() and self.confirm_save():
            new_credential = {
                website: {
                    **user_inputs
                }
            }

            all_credentials = get_credentials() or {}
            all_credentials.update(new_credential)

            with open(file="data.json", mode="w", encoding="utf-8") as data_file:
                json.dump(all_credentials, data_file, indent=4)

            self.clear_fields()

        elif credential:
            messagebox.showinfo(title=website, message="Credential already registered.")

    def clear_fields(self) -> None:
        self.website_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def has_empty_fields(self) -> bool:
        has_empty_fields = "" in self.get_user_inputs().values()
        if has_empty_fields:
            messagebox.showwarning(title="Blank fields", message="Please don't leave any fields empty!")

        return has_empty_fields

    def confirm_save(self) -> bool:
        user_inputs = self.get_user_inputs()
        confirm_msg = "These are details entered:\n\n" \
                      "Username: {username}\n" \
                      "Password: {password}\n\n" \
                      "It's ok to save?".format(**user_inputs)

        return bool(messagebox.askyesnocancel(title=user_inputs["website"], message=confirm_msg))

    def get_user_inputs(self) -> dict[str, str]:
        return {
            "website": self.website_entry.get().strip(),
            "username": self.username_entry.get().strip(),
            "password": self.password_entry.get().strip()
        }

    def generate_password(self) -> None:
        num_letters = random.randint(8, 10)
        num_symbols = random.randint(2, 4)
        num_digits = random.randint(2, 4)

        allowed_symbols = ("#", "$", "%", "&", "*", "@")

        if not 32 >= (num_letters + num_symbols + num_digits) >= 8:
            raise ValueError("Password must be 8 to 32 characters long.")

        chars = random.sample(ascii_letters, k=num_letters) + \
            random.sample(allowed_symbols, k=num_symbols) + \
            random.sample(digits, k=num_digits)

        random.shuffle(chars)
        password = "".join(chars)

        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(tk.END, password)

    def search_credential(self) -> None:
        website = self.get_user_inputs()["website"].title()
        if not website:
            messagebox.showwarning(title="Empty website field", message="Insert a website first!")
            return

        msg = "Username: {username}\n"\
              "Password: {password}\n\n"

        credential = get_credentials(website)

        if credential:
            messagebox.showinfo(title=website, message=msg.format(**credential))
        else:
            messagebox.showinfo(title="Info", message="Credential not found.")

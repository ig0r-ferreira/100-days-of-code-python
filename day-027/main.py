import tkinter as tk
import re

GENERAL_FONT = ("Verdana", 14)
IN_OUT_FONT = ("Verdana", 32)
IN_OUT_WIDTH = 12
RANGE_LIMITS = {
    "from_": 1,
    "to": 1_000_000_000
}


def validate_input(user_input):
    if re.match(r"^\d+(?:.\d+)?$", user_input):
        minval = int(window.nametowidget(miles_input).config('from')[4])
        maxval = int(window.nametowidget(miles_input).config('to')[4])

        return maxval >= float(user_input) >= minval

    return False


def convert_miles_to_km():
    km_output.config(state=tk.NORMAL)
    km_output.delete(0, tk.END)

    miles = float(miles_input.get().strip())
    km = round(miles * 1.609, 3)
    km_output.insert(tk.END, str(km))

    km_output.config(state="readonly")


window = tk.Tk()
window.title("Convert Miles to Kilometers")
window.minsize(width=400, height=100)
window.config(padx=50, pady=40)

miles_input = tk.Spinbox(width=IN_OUT_WIDTH, font=IN_OUT_FONT, justify=tk.CENTER, **RANGE_LIMITS)
miles_input.focus()
miles_input.grid(row=0, column=0, pady=10)

miles_label = tk.Label(text="Miles", font=GENERAL_FONT)
miles_label.grid(row=1, column=0)

to_label = tk.Label(text="=", font=GENERAL_FONT)
to_label.grid(row=0, column=1, padx=10)

km_label = tk.Label(text="Kilometers", font=GENERAL_FONT)
km_label.grid(row=1, column=2)

km_output = tk.Spinbox(width=IN_OUT_WIDTH, font=IN_OUT_FONT, justify=tk.CENTER, state="readonly",
                       readonlybackground="white")
km_output.grid(row=0, column=2, pady=10)

range_validation = window.register(validate_input)
miles_input.config(validate="key", validatecommand=(range_validation, '%P'), command=convert_miles_to_km)
convert_miles_to_km()

window.mainloop()

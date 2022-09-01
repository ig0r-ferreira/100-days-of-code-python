import tkinter as tk
import pyglet
from datetime import datetime, timedelta
from functools import partial


pyglet.font.add_file("font/Orbitron-Bold.ttf")


class PomodoroApp(tk.Tk):
    WHITE = "#ffffff"
    TEAL = "#B9FFF8"
    WINDOW_TITLE = "Pomodoro"
    FONT_TIMER_CONFIG = ("Orbitron", 44)
    FONT_BUTTON = ("Orbitron", 12)
    FONT_LABEL = ("Orbitron", 16)
    WORKING_TIME = "25:00"
    SHORT_BREAK_TIME = "05:00"
    LONG_BREAK_TIME = "20:00"
    END_TIME = "00:00"

    def __init__(self):
        super().__init__()
        self.reset_button = None
        self.start_stop_button = None
        self.button_frame = None
        self.title_label = None
        self.timer_text = None
        self.canvas = None
        self.bg_img = None
        self.config_window()
        self.draw_figure_and_timer()
        self.create_title()
        self.create_buttons()
        self.running_count = False
        self.steps = 0
        self.reset_timer(self.WORKING_TIME)

    def config_window(self):
        self.title(self.WINDOW_TITLE)
        self.resizable(False, False)
        self.config(padx=100, pady=50, bg=self.TEAL)

    def draw_figure_and_timer(self):
        self.bg_img = tk.PhotoImage(file="img/tomato.png")
        self.canvas = tk.Canvas(width=self.bg_img.width(), height=self.bg_img.height(), bg=self.TEAL,
                                highlightthickness=0)
        x_pos, y_pos = self.bg_img.width() / 2, self.bg_img.height() / 2
        self.canvas.create_image(x_pos, y_pos, image=self.bg_img)
        self.timer_text = self.canvas.create_text(x_pos, y_pos, fill=self.WHITE, font=self.FONT_TIMER_CONFIG)
        self.canvas.pack()

    def create_title(self):
        x_pos, y_pos = self.bg_img.width() / 2, (self.bg_img.height() / 2) - 60
        self.title_label = self.canvas.create_text(x_pos, y_pos, fill=self.WHITE, font=self.FONT_LABEL)

    def reset_timer(self, start_time, block="WORKING", reset_steps=False):
        self.steps = 1 if reset_steps else self.steps
        self.running_count = False
        self.canvas.itemconfig(self.title_label, text=block.upper())
        self.canvas.itemconfig(self.timer_text, text=start_time)
        self.start_stop_button.config(text="START")

    def next_block(self):
        self.steps += 1

        if self.steps % 8 == 0:
            block_name = "LONG BREAK"
            start_time = self.LONG_BREAK_TIME
        elif self.steps % 2 == 0:
            block_name = "BREAK"
            start_time = self.SHORT_BREAK_TIME
        else:
            block_name = "WORKING"
            start_time = self.WORKING_TIME

        self.reset_timer(start_time, block_name)
        if self.steps <= 8:
            self.start_stop_timer()
        else:
            self.steps = 1

    def count_down(self):
        time_format = "%M:%S"
        current_time = datetime.strptime(self.canvas.itemcget(self.timer_text, "text"), time_format)

        if self.running_count and current_time > datetime.strptime(self.END_TIME, time_format):
            new_time = (current_time - timedelta(seconds=1)).strftime(time_format)
            self.canvas.itemconfig(self.timer_text, text=new_time)
            self.after(1000, self.count_down)

        elif self.running_count:
            self.next_block()

    def start_stop_timer(self):
        state = self.start_stop_button["text"]
        if state in ("START", "RESUME"):
            self.running_count = True
            self.start_stop_button.config(text="STOP")
            self.count_down()
        else:
            self.running_count = False
            self.start_stop_button.config(text="RESUME")

    def create_buttons(self):
        x_pos, y_pos = self.bg_img.width() / 2, (self.bg_img.height() / 2) + 70
        self.button_frame = tk.Frame()
        self.button_frame.pack()
        button_config = {
            "master": self.button_frame,
            "width": 8,
            "bg": self.TEAL,
            "font": self.FONT_BUTTON,
        }

        self.start_stop_button = tk.Button(**button_config, command=self.start_stop_timer)

        reset_function = partial(self.reset_timer, self.WORKING_TIME, reset_steps=True)
        self.reset_button = tk.Button(**button_config, text="RESET", command=reset_function)

        self.start_stop_button.grid(row=0, column=0)
        self.reset_button.grid(row=0, column=1)
        self.canvas.create_window(x_pos, y_pos, window=self.button_frame)

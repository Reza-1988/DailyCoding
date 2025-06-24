import tkinter as tk
import math
import emoji


# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# TIMER RESET
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmark_label.config(text="")

# TIMER MECHANISM
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    elif reps % 2 == 1:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# COUNTDOWN MECHANISM
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text="%d:%02d" %(count_min, count_sec)) # this methode get the canvas text and pass the new text
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) # this methode count down every 1 second
    else:
        start_timer()
        # add emoji every 2 reps
        global reps
        working_session = math.floor(reps // 2)
        checkmark_label.config(text=emoji.emojize(":tomato:") * working_session)
        # text = ""
        # for _ in range(working_session):
        #     text += "1"
        #     checkmark_label.config(text=text)

# UI SETUP
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# read image and make canvas with text
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

# labels
title_label = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35), bg=YELLOW)
title_label.grid(row=0, column=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

checkmark_label = tk.Label(text="" ,fg=GREEN,bg=YELLOW,font=(FONT_NAME, 10))
checkmark_label.grid(row=2, column=1)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()

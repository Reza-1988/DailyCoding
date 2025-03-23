import tkinter as tk
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

data = pd.read_csv("./data/french_words.csv")
# with orient argument we can change our dict to key:columns and values:row
words_to_learn = data.to_dict(orient="records")
current_card = {}

def front_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(canvas_background, image=canvas_front_img)
    canvas.itemconfig(canvas_front_word, text=current_card["French"], font=(FONT_NAME, 35, "italic"), fill="Black" )
    canvas.itemconfig(canvas_title, text="French", font=(FONT_NAME, 35, "bold"), fill="Black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_background, image=canvas_back_img)
    canvas.itemconfig(canvas_title, text="English", font=(FONT_NAME, 35, "italic"), fill="white")
    canvas.itemconfig(canvas_front_word, text=current_card["English"], font=(FONT_NAME, 35, "bold"), fill="white")






# UI SETUP
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# read image and make canvas with text
canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_front_img = tk.PhotoImage(file="./images/card_front.png")
canvas_back_img = tk.PhotoImage(file="./images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=canvas_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 35, "italic"), fill="Black")
canvas_front_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 35, "bold"), fill="Black")

wrong_image = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=front_card)
wrong_button.grid(row=1, column=0)

right_img = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(image=right_img, highlightthickness=0, command=front_card)
right_button.grid(row=1, column=1)

front_card()



window.mainloop()
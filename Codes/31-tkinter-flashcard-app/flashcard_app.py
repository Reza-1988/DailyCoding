import tkinter as tk
import random
import pandas as pd

# Define constants for UI styling
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

# Initialize global variables
current_card = {}
to_learn = {}

# READ FILE
# Attempt to load the words to learn from a CSV file
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    # with orient argument we can change our dict to key:columns and values:row
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# CARD FUNCTIONALITY
def front_card():
    """Display the front of the card (French word) and schedule a flip after 3 seconds."""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_background, image=canvas_front_img)
    canvas.itemconfig(canvas_front_word, text=current_card["French"], font=(FONT_NAME, 35, "italic"), fill="Black" )
    canvas.itemconfig(canvas_title, text="French", font=(FONT_NAME, 35, "bold"), fill="Black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    """Flip the card to show the English translation."""
    canvas.itemconfig(canvas_background, image=canvas_back_img)
    canvas.itemconfig(canvas_title, text="English", font=(FONT_NAME, 35, "italic"), fill="white")
    canvas.itemconfig(canvas_front_word, text=current_card["English"], font=(FONT_NAME, 35, "bold"), fill="white")

def known_card():
    """Remove the current card from the to_learn list and save the updated list."""
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn).to_csv("./data/words_to_learn.csv", index=False)
    front_card()

# UI SETUP
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Set up a timer to flip the card after 3 seconds
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
right_button = tk.Button(image=right_img, highlightthickness=0, command=known_card)
right_button.grid(row=1, column=1)

# Display the first card
front_card()

window.mainloop()
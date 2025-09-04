from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/mandarin_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_background_front)
    canvas.itemconfig(card_hanzi, text=current_card["Hanzi"])
    canvas.itemconfig(card_pinyin, text=current_card["Pinyin"])
    canvas.itemconfig(card_meaning, text="")
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_background_back)
    canvas.itemconfig(card_hanzi, text="")
    canvas.itemconfig(card_pinyin, text="")
    canvas.itemconfig(card_meaning, text=current_card["Meaning"])


def is_known():
    to_learn.remove(current_card)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_background_front = PhotoImage(file="images/card_front.png")
card_background_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_background_front)
card_hanzi = canvas.create_text(400, 150, font=("Aeriel", 40, "normal"))
card_pinyin = canvas.create_text(400, 200, font=("Aeriel", 60, "italic"), anchor="n")
card_meaning = canvas.create_text(
    400, 200, font=("Aeriel", 18, "italic"), width=400, anchor="n"
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.config(highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, command=is_known)
known_button.config(highlightthickness=0)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

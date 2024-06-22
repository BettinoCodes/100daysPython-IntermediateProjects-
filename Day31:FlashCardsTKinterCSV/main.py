from tkinter import *
from data.data_dictionary import italian_dict
import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()

try:
    data_cards = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    italian_dict = italian_dict
else:
    italian_dict = data_cards.to_dict(orient='records')

def flip_card():
    canvas.itemconfig(canv_img, image=back_img)
    canvas.itemconfig(canv_title, text="ENGLISH")
    canvas.itemconfig(canv_word, text=f"{current_card["ENGLISH"]}")
    canvas.after(3000, revert_canvas)


window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

current_card = {}

back_img = PhotoImage(file="images/card_back.png")


def revert_canvas():
    global front_img
    canvas.itemconfig(canv_img, image=front_img)
    canvas.itemconfig(canv_title, text="ITALIAN")
    canvas.itemconfig(canv_word, text=f"{current_card["ITALIAN"]}")


def flip_it():
    canvas.after(0, flip_card)

def next_card():
    global current_card
    current_card = random.choice(italian_dict)
    canvas.itemconfig(canv_title, text="ITALIAN")
    canvas.itemconfig(canv_word, text=current_card["ITALIAN"])


def add_to_wrong():
    italian_dict.remove(current_card)
    print(len(italian_dict))
    data = pandas.DataFrame(italian_dict)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
canv_img = canvas.create_image(400, 263, image=front_img)
canv_title = canvas.create_text(400, 150, text=f"Title", font=("arial", 26, "italic"))
canv_word = canvas.create_text(400, 263, text=f"WORD", font=("arial", 40, "bold"), width=700)
canvas.grid(column=1, row=0, columnspan=2)


photo1 = PhotoImage(file="images/right.png")
canvas_right = Button(image=photo1, highlightthickness=0, command=next_card)
canvas_right.grid(column=0, row=2, columnspan=2 )


photo = PhotoImage(file="images/wrong.png")
canvas_wrong = Button(image=photo, command=add_to_wrong)
canvas_wrong.grid(column=2, row=2, columnspan=2 )

flip_button = Button(text="FLIP", width=5, height=2, bg=BACKGROUND_COLOR, highlightthickness=0, font=("arial", 18, "bold"), command=flip_it)
flip_button.grid(column=1, row=2, columnspan=2)



next_card()

window.mainloop()


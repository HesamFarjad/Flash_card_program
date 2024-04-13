import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# data = pandas.read_csv("./data/french_words.csv")
# to_learn = data.to_dict(orient="records")



def known_word():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_bg_for_front, image=img_front)

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_bg_for_front, image=img_back)



# ----------------------------------- UI -------------------------------
window = Tk()
window.title("Flash Card")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

img_back = PhotoImage(file="./images/card_back.png")

img_front = PhotoImage(file="./images/card_front.png")
card_bg_for_front = canvas.create_image(400, 263, image=img_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

wrong_btn_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=wrong_btn_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
button_wrong.grid(row=1, column=0)

correct_btn_img = PhotoImage(file="./images/right.png")
button_correct = Button(image=correct_btn_img, highlightbackground=BACKGROUND_COLOR, command=known_word)
button_correct.grid(row=1, column=1)

next_card()
window.mainloop()

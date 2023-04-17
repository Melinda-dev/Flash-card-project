from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
# if haven't words to learn, then use french_words to create a dic.
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    # data type is list
    to_learn = original_data.to_dict("records")
    print(to_learn)


else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background,image=card_front_image)
    window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_know():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    #"index=False": the DataFrame index will not be included in the CSV file.
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B1DDC6")

window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_image)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,260,text="word",font=("Ariel", 60, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


#Button

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_know)
known_button.grid(row=1, column=0)

next_card()

window.mainloop()

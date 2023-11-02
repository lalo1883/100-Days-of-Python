import random

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd


words = pd.read_csv('FlashCards - Hoja 1.csv')
random_index = {}
def select_new_choice():
    global random_index, flip_timer
    window.after_cancel(flip_timer)
    random_index = random.choice(words.index)
    random_word = words.at[random_index, 'English']
    canvas.itemconfig(text_title, text=f'English', fill='black')
    canvas.itemconfig(text_word, text=f'{random_word}', fill='black')
    canvas.itemconfig(card_background, image=card_image)
    flip_timer = window.after(3000, func=filp_card)


    # print(f'Traduction: {traduction}')

def filp_card():
    traduction = words.at[random_index, 'Español']
    canvas.itemconfig(text_word, text=f'{traduction}', fill='white')
    canvas.itemconfig(text_title, text=f'Español', fill='white')
    canvas.itemconfig(card_background, image=card_back_image)

window = Tk()
window.title("Card Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=filp_card)


canvas = Canvas(width=800, height=526)
card_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')
card_background = canvas.create_image(400,263,image=card_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

text_title= canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
text_word = canvas.create_text(400, 263, text='Word', font=('Arial', 60, 'bold'))

canvas.grid(row=0,column=0, columnspan=2)



cross_image = PhotoImage(file='images/wrong.png')
unkown_button = Button(image=cross_image, highlightthickness=0, command=select_new_choice)
unkown_button.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
known_button = Button(image=right_image, highlightthickness=0, command=select_new_choice)
known_button.grid(row=1, column=1)


window.mainloop()
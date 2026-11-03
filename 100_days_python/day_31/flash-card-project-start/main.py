BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random 

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
random_word={}
word_list={}
csv_file_path = "D:/python/100_days_python/day_31/flash-card-project-start/data/french_words.csv"
new_csv_file_path = "D:/python/100_days_python/day_31/flash-card-project-start/data/words_to_learn.csv"

try:
    data= pandas.read_csv(new_csv_file_path)
except FileNotFoundError:
    original_data= pandas.read_csv(csv_file_path)
    word_list = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")

def next_card():   
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(word_list)
    french_word = random_word['French']
    canvas.itemconfig(card_image, image = card_font)
    canvas.itemconfig(card_title, text="French",  fill="black")
    canvas.itemconfig(card_word, text=french_word,  fill="black")
    flip_timer = window.after(3000,flip_card)

def remove_data():
    word_list.remove(random_word)
    data =  pandas.DataFrame(word_list)
    print("remove = data", data)
    data.to_csv(new_csv_file_path,index=False)
    next_card()

    

def flip_card():
    canvas.itemconfig(card_image, image = card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")       

flip_timer = window.after(3000,flip_card)

canvas = Canvas(width=800, height=526)
card_font = PhotoImage(file="D:/python/100_days_python/day_31/flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="D:/python/100_days_python/day_31/flash-card-project-start/images/card_back.png")
card_image = canvas.create_image(400,263, image=card_font)
card_title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="D:/python/100_days_python/day_31/flash-card-project-start/images/right.png")
right_btn = Button(image=right_image, highlightthickness=0, command=remove_data)
right_btn.grid(row=1, column=0)

wrong_image = PhotoImage(file="D:/python/100_days_python/day_31/flash-card-project-start/images/wrong.png")
wrong_btn = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=1)


next_card()

window.mainloop()
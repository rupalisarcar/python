from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width = 500, height=300)

my_label = Label(text="New Text", font=("arial",40, "bold"))
my_label.pack() 

def button_clicked():
    print("Clicked the btn")
    my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())

button = Button()
button.config(text="Click me", command=button_clicked)
button.pack()


input = Entry(width=20)
show_data = input.get()
input.pack()
window.mainloop()
from tkinter import *

window = Tk()
window.title("Grid layout")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

first_label = Label(text="Label", font=("Courier",25,"bold"))
first_label.config(padx=50, pady=50)
first_label.grid(column=0, row=0)

button = Button()
button.config(text="New button")
button.grid(column=2, row=0)


button2 = Button()
button2.config(text="Button")
button2.grid(column=1, row=1)

last_input = Entry(width=30)

last_input.grid(column=3, row=2)

window.mainloop()
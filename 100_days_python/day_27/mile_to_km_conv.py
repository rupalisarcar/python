from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=100)

first_input = Entry()
first_input.config(width=10)
first_input.grid(column=1, row=0)

label1 = Label()
label1.config(text="Miles")
label1.grid(column=2, row=0)

label2 = Label()
label2.config(text="is equal to")
label2.grid(column=0, row=1)



km_dis = Label()
km_dis.config(text="0")
km_dis.grid(column=1, row=1)


km_label = Label()
km_label.config(text="Km")
km_label.grid(column=2, row=1)

def calculate_km():
    distance = float(first_input.get())*1.60
    km_dis.config(f"{distance}")

button = Button()
button.config(text="Calculate", command=calculate_km)
button.grid(column=1, row=2)

window.mainloop()
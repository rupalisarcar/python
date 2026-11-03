from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','@','#','$','%','&','*','(',')','+','_']

    ne_letter = random.randint(8,10)
    ne_number = random.randint(2,4)
    ne_symbol = random.randint(2,4)

    
    pass_letters=[random.choice(letters) for _ in range(ne_letter)]
    pass_numbers=[random.choice(numbers) for _ in range(ne_number)]
    pass_symbols = [random.choice(symbols) for _ in range(ne_symbol)]

    random_password = pass_letters+pass_numbers+pass_symbols
    random.shuffle(random_password)
    new_password = ''.join(random_password)

    pass_entry.insert(0,new_password)
    pyperclip.copy(new_password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    if len(website)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave Website field empty")
    else:
        try:
            with open("./day_29/data.json","r") as file_read:
                data = json.load(file_read)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
           
        else:
            if website in data:
                email = data[website]['email']
                password = data[website]['password']
                messagebox.showinfo(title=website, message=f"Email : {email}\nPassword : {password}")     
            else:
                messagebox.showinfo(title="Error", message=f"No details for the {website} exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    password = pass_entry.get()
    email = email_entry.get()
    if len(password)==0 or len(website)==0 or len(email)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered : \nEmail : {email}\nPassword : {password}\nIs it okay to save?")    
        if is_ok:
            # newEntry = f"Website : {website} | Email/username : {email} | Password : {password}\n"
            new_data = {
                website:{
                    "email":email,
                    "password":password
                }
            }
            try:
                with open("./day_29/data.json","r") as file_read:
                    data = json.load(file_read)
                    
            except FileNotFoundError:         
                with open("./day_29/data.json","w") as file_write:
                    json.dump(new_data,file_write, indent=3)    
            else:      
                data.update(new_data)  
                with open("./day_29/data.json","w") as file_write:
                    json.dump(data,file_write, indent=3) 
            finally:                                  
                    website_entry.delete(0,"end")
                    pass_entry.delete(0,"end")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

pass_image = PhotoImage(file="D:/python/100_days_python/day_29/password-manager-start/logo.png")
canvas.create_image(100,100, image = pass_image)
canvas.grid(row=0, column=1)

# ---------------- Website ----------------
website_level = Label(text="Website : ")
website_level.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()

search_btn = Button()
search_btn.config(text="Search", command = find_password, width=13)
search_btn.grid(row=1, column=2)

# ---------------- Email ----------------
email_level = Label(text="Email/Username : ")
email_level.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"rupalisarkar12@gmail.com")

# ---------------- Password ----------------
pass_level = Label(text="Password : ")
pass_level.grid(row=3, column=0)

pass_entry = Entry(width=21)
pass_entry.grid(row=3,column=1)

pass_btn = Button()
pass_btn.config(text="Generate Password", command=create_password)
pass_btn.grid(row=3, column=2)
# ---------------- button ----------------

add_btn = Button()
add_btn.config(text="Add", width=36, command=save)
add_btn.grid(row=4,column=1, columnspan=2)
window.mainloop()
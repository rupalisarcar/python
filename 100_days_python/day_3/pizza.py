print("Welcome to Python Pizza Deliveries!")
price = 0;
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("What you want extra cheese? Y or N: ")

if size=='S' or size=='s':
    price=15
elif size=='M' or size == 'm':
    price=20
elif size == 'L' or size=='l':
    price=25
else:
    print("You typed the wrong inputs")

if pepperoni=='Y':
    if size=='S' or size =='s':
        price+=2
    else:
        price+=3

if extra_cheese == 'Y':
    price+=1

print(f"Your final bill is Rs.{price}.")
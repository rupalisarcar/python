import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['1','2','3','4','5','6','7','8','9','0']

symbols = ['!','@','#','$','%','&','*','(',')','+','_']

print("Welcome to the Password Generator")
ne_letter = int(input("How many letters would you like in your password?\n"))
ne_number = int(input("How many numbers would you like?\n"))
ne_symbol = int(input("How many symbols would you like?\n"))

#easy password
new_password = ''
for l in range(0,ne_letter):
    new_password+=random.choice(letters)
for sym in range(0,ne_symbol):
    new_password+=random.choice(symbols)
for num in range(0,ne_number):
    new_password+=random.choice(numbers)   

print(new_password) 

# Hard Password 1st option
passwordLength = len(new_password)
strong_password=''
for password in range(0,passwordLength):
    strong_password+=random.choice(new_password)

print(strong_password)   

# Hard Password 2nd option

new_password_2 = []
for l in range(0,ne_letter):
    new_password_2.append(random.choice(letters))
for sym in range(0,ne_symbol):
    new_password_2.append(random.choice(symbols))
for num in range(0,ne_number):
    new_password_2.append(random.choice(numbers)) 

print(f"New password {new_password_2}") 
random.shuffle(new_password_2) 
strong_password2 = ''
for char in new_password_2:
    strong_password2 +=char    


print(f"Random password {new_password_2}") 
print(f"Random password is {strong_password2}") 

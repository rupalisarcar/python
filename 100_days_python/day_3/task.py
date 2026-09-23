print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
question_1 = input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\" \n").lower()

if question_1=="left" :
    question_2= input('You\'ve come to lake. There is an island in the middle of the lake.\n\tType "wait" to wait for a boat. Type "swim" to swim across.').lower()

    if question_2=="wait":
        question_3 = input("You arrived at the island unharmed. There is house with 3 doors. One Red, one yellow, one blue. Which color do you choose?").lower()

        if question_3 =='yellow':
            print("You've found the treasue. You Win")
        elif question_3 == "red":
            print("It's room full of fire. Game over")
        elif question_3 == "blue":
            print("You enter a room of beasts. Game over")
        else:
            print("You choose a door doesn't exist. Game Over")
    else:
        print("You got attacked by an angry trout. Game Over")
elif question_1 == "right":
    print("you fell into a hole. Game over.")
else:
    print("You have enterd wrong option")
import random

rock = '''
        ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'
 '''

paper = ''' 
              / \\ | | /\\
               \\ \\| |/ /
                \\ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
                |     |
'''

scissors = ''' 
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \\  `(.-')
   > ._>-'
  / \\/

'''

arr = [rock, paper, scissors]

user_choose = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors\n"))
print(arr[user_choose])
computer_choice = random.randint(0,2)
print("Computer Choose\n",arr[computer_choice])

if user_choose>=3 or user_choose<0:
    print("You typed a invalid number")
if user_choose==computer_choice:
    print("It's a draw")
elif (user_choose==0 and computer_choice==2) or (user_choose==2 and computer_choice==1) or (user_choose==1 and computer_choice==0):
    print("You win")
else : 
    print("You loose")
from random import choice
from game_data import data

all_data = data.copy()
def random_choice():
    '''Return random data from game_ data'''
    print(len(all_data))
    selected = choice(all_data)
    all_data.remove(selected)
    return selected



compare_A = random_choice()
compare_B = random_choice()

score = 0
right_ans = True

while right_ans:
    print(f"Compare A - {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
    print(f"Compare B - {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")

    compare = input("Who has more followers? Type 'A' or 'B' :   ").upper()

    if compare_A['follower_count'] > compare_B['follower_count'] and compare=='A':
        compare_B = random_choice()
        right_ans = True
        score+=1
    elif compare_A['follower_count'] < compare_B['follower_count'] and compare=='B':
        compare_A = compare_B
        compare_B = random_choice()
        right_ans = True
        score+=1
    else : 
        print(f"Sorry, that's wrong.Final score : {score}")
        right_ans = False



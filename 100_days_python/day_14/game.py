from random import choice
from game_data import data
import art

# Display Art

# Generate a random account for game data
all_data = data.copy()
def random_choice():
    '''Return random data from game_ data'''
    selected = choice(all_data)
    all_data.remove(selected)
    return selected
# format the account data into a printable format
def formated_data(account):
    name =account['name']
    description =account['description']
    country =account['country']
    return (f"{name}, a {description}, from {country}")

def check_ans(compare_A_count, compare_B_count, guess):
    if compare_A_count>compare_B_count:
        return guess == 'A'
    else:
        return guess=='B'

# Ask user for a guess
def higher_lower():
    
    compare_B = random_choice()
    score = 0
    right_ans = True

    while right_ans:
        compare_A = compare_B
        compare_B= random_choice()
        print(f"Compare A - {formated_data(compare_A)}")
        print(art.vs)
        print(f"Against B - {formated_data(compare_B)}")
        
        compare = input("Who has more followers? Type 'A' or 'B' :   ").upper()

        print("\n"*20)
        print(art.logo)
        guess_ans= check_ans(compare_A['follower_count'], compare_B['follower_count'],compare)

        if guess_ans == True:
            score+=1
            print(f"You're right! Current score: {score}.")
        else :             
            print(f"Sorry, that's wrong.Final score : {score}")
            right_ans = False

print(art.logo)
higher_lower()



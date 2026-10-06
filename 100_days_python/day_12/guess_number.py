import random
from art import logo

def guessing_number_fun(attempt, guess_number):
    print("attempt number", attempt)
    while attempt>0:
        print(f"You have {attempt} attempts remaining to guess the number.")  
        # let the user guess a number
        user_choose = int(input("Make a guess:  "))
        if guess_number>user_choose and attempt>1:
            print("Too low.\nGuess again.")
        elif guess_number<user_choose and attempt>1:
            print("Too high.\nGuess again.")
        elif guess_number==user_choose:
            return (f"You got it. The answer was {guess_number}")
        else:
            return "You've run out of guesses. Refresh the page to run again"
        attempt-=1

# Choosing a random number between 1 and 100
guess_number = random.randint(1,100)

# function to set difficulty
def guessing_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between between 1 and 100.")
    difficult_level = input("Choose a difficulty. Type 'easy' or 'hard' :  ").lower()
    attempt_number = 0
    if difficult_level == 'easy':
        attempt_number = 10
        print(guessing_number_fun(attempt_number,guess_number))
    elif difficult_level == 'hard':
        attempt_number = 5
        print(guessing_number_fun(attempt_number,guess_number))
    else:
        print("You choose wrong option")
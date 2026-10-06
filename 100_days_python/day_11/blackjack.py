import random
import art

def deal_card():
    ''' Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculation(card):
    ''' Take a list of the cards and return the score calculated from the cards'''
    if 11 in card and 10 in card and len(card)==2: 
        result = 0
    else:
        result = sum(card)
        if result>21 and 11 in card:
            card.remove(11)
            card.append(1)
        
    return result

def compare(com_score, user_score):
    if user_score==com_score:
        return "Draw 🙃"
    
    elif com_score==0:
        return "Lose, opponent has Blackjack 😱"
        
    elif user_score==0:
        return "Win with a Blackjack 😎"
    
    elif com_score>21:
        return "Opponent went over. You win 😁"

    elif user_score>21:
        return "You went over. You lose 😭"

    elif user_score>com_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def start_play():
    my_cards = []
    computer_cards = []
    print(art.logo)
    for i in range(2):
        my_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    game_over = False
    while not game_over:
        my_score = calculation(my_cards)
        computer_score = calculation(computer_cards)
        print(f"Your cards: {my_cards}, current score: {my_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if my_score == 0 or computer_score ==0 or my_score>21:    
            game_over = True
        else:
            play_again = input(f"Type 'y' to get another card, type 'n' to pass:  ").lower()
            if play_again == 'y':
                my_cards.append(deal_card())
            else:
                game_over = True
    
    while computer_score<17:
        computer_cards.append(deal_card())
        computer_score = calculation(computer_cards)

    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(computer_score,my_score))


        
                





            
            

while input(f"Do you want to you want to play a game of Blackjack? Type 'y' or 'n':  ").lower() =='y':
    print("\n"*20)    
    start_play()
                



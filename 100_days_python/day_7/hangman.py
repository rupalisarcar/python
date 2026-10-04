import random
import hangman_words
import hangman_art

word_list=hangman_words.word_list
stages = hangman_art.stages

#print logo
print(hangman_art.logo)
choose_word = random.choice(word_list)

placeholder=""
for space in range(len(choose_word)):
    placeholder+='_'

print(placeholder)
game_over = False
choosed_char=[]
guesed_char = []
lives = 6

while not game_over:
    print(f"****************************{lives} LIVES LEFT****************************")

    display = ""
  
    letter = input("Guess a letter: ").lower()
    
    if letter in choosed_char:
        print(f"You've already guessed {letter}")

    for char in choose_word:
        if char==letter:
            display+=letter
            choosed_char.append(letter)
        elif char in choosed_char:
            display+=char    
        else:
            display+='_'  
            

    print(display)

    if letter not in choose_word:
        if letter not in guesed_char:
            guesed_char.append(letter)    
            lives-=1     
            print(f"You guessed {letter}, that's not in the word. You lose a life.")
        else:
            print(f"You've already guessed {letter}")
        if lives==0:
            game_over = True
            print(f"It was {choose_word}! You loose")
            
    print(stages[lives])    

    if "_" not in display:
       game_over = True
       print("You win")
    
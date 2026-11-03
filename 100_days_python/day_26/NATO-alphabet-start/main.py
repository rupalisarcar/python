import pandas
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path,"nato_phonetic_alphabet.csv")


alphabet_data_frame = pandas.read_csv(file_path)


#Loop through rows of a data framefor (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

#TODO 1. Create a dictionary in this format:

# {"A": "Alfa", "B": "Bravo"}

# Keyword Method with iterrows()
phonetic_dict ={row.letter:row.code for (index,row) in alphabet_data_frame.iterrows()}




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
right_word=True
while right_word:
    user_input = list(input("Enter a word : ").upper())
    try:
        new_nato_word = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:    
        print(new_nato_word)
        right_word=False
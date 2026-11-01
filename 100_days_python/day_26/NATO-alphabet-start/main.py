import pandas
import os

dir_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir_path,"nato_phonetic_alphabet.csv")


alphabet_data_frame = pandas.read_csv(file_path)
print(alphabet_data_frame)

#Loop through rows of a data framefor (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

#TODO 1. Create a dictionary in this format:

# {"A": "Alfa", "B": "Bravo"}

# Keyword Method with iterrows()
phonetic_dict ={row.letter:row.code for (index,row) in alphabet_data_frame.iterrows()}
print(phonetic_dict)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = list(input("Enter a word : ").upper())
new_nato_word = [phonetic_dict[letter] for letter in user_input]
print(new_nato_word)

import os
script_dir = os.path.dirname(os.path.abspath(__file__))

new_name_file_path = os.path.join(script_dir, "Input","Names","invited_names.txt")

with open(new_name_file_path,"r") as name_file:
    names_file = name_file.readlines()

letter_file_path = os.path.join(script_dir, "Input","Letters","starting_letter.txt")
with open(letter_file_path,"r") as letter_file:
    letter = letter_file.read()

    print(names_file)
    for name in names_file:
        new_name = name.strip()
        new_letter = letter.replace("[name]", new_name)

        new_letter_file_path = os.path.join(script_dir, "Output","ReadyToSend",f"letter_for_{new_name}.docx")
        with open(new_letter_file_path,"w") as new_letter_file:
            new_letter_file.write(new_letter)



    
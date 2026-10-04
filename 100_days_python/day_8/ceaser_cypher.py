from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(user_text, shift_amount, encode_or_decode):
        # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
        #  by the shift amount and print the decrypted text.
        original_text = ''
        for char in user_text:
            if char not in alphabet:
                original_text+=char
            else:
                if encode_or_decode == 'encode':
                    shifted_index = alphabet.index(char)+shift_amount
                else:
                    shifted_index = alphabet.index(char)-shift_amount
                shifted_index %= len(alphabet)
                original_text += alphabet[shifted_index]

        print(f"Here is the {encode_or_decode}d result: {original_text}")

play = True
while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction=='encode' or direction=='decode':
        caesar(text,shift,direction)
        restart_again = input(f"Type 'yes' if you want to go again. Otherwise, type 'no'\n")
        if restart_again != 'yes':
            play=False
            print("Good bye")
    else:
        print("You entered wrong direction")

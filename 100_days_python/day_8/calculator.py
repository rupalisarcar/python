def calculate_love_score(name1, name2):
    names= (name1 + name2).upper()

    true_total = 0
    love_total = 0

    true_total = names.count('T')+names.count('R')+names.count('U')+names.count('E')
    love_total = names.count('L')+names.count('O')+names.count('V')+names.count('E')
   
    print(true_total)
    print(love_total)
    print(f"{true_total}{love_total}")   

calculate_love_score("Kanye West", "Kim Kardashian")
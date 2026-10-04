from art import logo
print(logo)
print("Welcome to the secret auction program")
auction_dic = {}
play = True
while play:
    bider_name = input("What is your name? : ")
    bid_price = int(input("what's your bid? Rs."))
    auction_dic[bider_name] = bid_price

    continue_auc = input("Are there any other bidders? Type 'yes' or 'no'.\n") 
    if continue_auc == 'yes':
        print('\n'*100)
    elif continue_auc == "no":
        play=False
        print(auction_dic)
        maxPrice = 0
        name=''
        for key in auction_dic:
            if auction_dic[key]>maxPrice:
                maxPrice = auction_dic[key]
                name=key
        print("\n"*50)
        print(f"The winner is {name} with a bid of Rs.{maxPrice}")
    else:
        print("You typed wrongly")
        play=False
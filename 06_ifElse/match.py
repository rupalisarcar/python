a = int(input("Enter a number : "))

match a:
    case 200:
        print("You entered 200")    
    case 400:
        print("You entered 400")
    case 404:
        print("Enter error page")
    case 450:
        print("You entered 450")
    case _:
        print("You entered wrong number")

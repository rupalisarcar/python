import art

def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    if n1>n2:
        return n1-n2
    else:
        return n2-n1
def multiply(n1, n2):
    return n1*n2
def division(n1, n2):
    return n1/n2

print(art.logo)

oprations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : division
}

def calculator():
    first_number = float(input(f"What is the first number? : "))
    operation_again='y'
    while operation_again=='y':
        for symbol in oprations:
            print(symbol)
        operator = input(f"Pick an operation: ")
        sec_number = float(input(f"What's the next number? : "))

        result = oprations[operator](first_number, sec_number)
        print(f"{first_number} {operator} {sec_number} = {result}")
    

        operation_again = input(f"Type 'y to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if operation_again =='y':
            first_number= result
        else:
            calculator()

calculator()




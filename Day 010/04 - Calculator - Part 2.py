#calculator 
from art import logo

#add 
def add(n1, n2):
    return n1 + n2 

#subtract 
def subtract(n1, n2):
    return n1 - n2 

#multiply 
def multiply(n1, n2):
    return n1 * n2 

#divide
def divide(n1, n2):
    return n1 / n2 


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))
    num2 = float(input("What's the second number? "))
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation symbol from the line above: ")
    answer = operations[operation_symbol](n1=num1,n2=num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    keep_going = True 

    while keep_going:
        user_continue = input(f"Would you like to continue with {answer}, or type 'n' to start a new calculation.: ")
        if str(user_continue).lower() == "n":
            keep_going = False
            calculator()
        else:
            num1 = answer
            operation_symbol = input("Pick an operation symbol from the line above: ")
            num2 = float(input("What is the next number? "))
            answer = operations[operation_symbol](n1=num1,n2=num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

calculator()
#Calculator

def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2):
    return n1 - n2 

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
    return n1 / n2 

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

global keep_calculating 
global num1 
global num2 
global operations_string
global answer 

keep_calculating = True 

num1 = 0 

num2 = 0 

operations_string = ""
for operator in operations:
    operations_string += f"{operator} "
operations_string = operations_string.rstrip()

answer = 0

def start_calculating():
    global num1
    global num2 
    global answer 
    global keep_calculating 
    global operations_symbol

    num1 = int(input("What's the first number? "))

    operations_symbol = input(f"Choose an operation [{operations_string}]: ")

    num2 = int(input("What's the second number? "))

    answer = operations[operations_symbol](n1=num1,n2=num2)
    num1 = answer 

    print(f"{num1} {operations_symbol} {num2} = {answer}")

    while keep_calculating == True:
        another_calc = input("do you want to continue calculating? y/n ")
        if another_calc == "n":
            print("Goodbye")
            return 
        else:
            operations_symbol = input(f"Choose an operation [{operations_string}]: ")

        num2 = int(input("What's the second number? "))

        answer = operations[operations_symbol](n1=num1,n2=num2)
        num1 = answer 

        print(f"{num1} {operations_symbol} {num2} = {answer}")

start_calculating()
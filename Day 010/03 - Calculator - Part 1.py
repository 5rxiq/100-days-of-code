#calculator 

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

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

for key in operations:
    print(key)

operation_symbol = input("Pick an operation symbol from the line above: ")

answer = operations[operation_symbol](n1=num1,n2=num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
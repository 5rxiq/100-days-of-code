from art import logo
print(logo)

# add function
def add(n1, n2):
    return n1 + n2

# subtract function
def subtract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

answer = ""
keep_running = True

while keep_running is True:
    if answer == "":
        num1 = float(input("What's the first number?: "))
    else:
        num1 = float(answer)

    for symbol in operations:
        print(symbol)

    user_operation = input("Please choose a symbol from the list above: ")

    num2 = float(input("What's the second number?: "))

    answer = operations[user_operation](n1=num1, n2=num2)
    print(f"{num1} {user_operation} {num2} = {answer}")

    cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit. ")

    if cont == "n":
        keep_running = False
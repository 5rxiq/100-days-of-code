# Functions

def my_function():
    result = 3 * 2
    return result


output = my_function()
my_function()
print(output)

# Functions with Outputs


def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
#    print(f"{f_name} {l_name}")
    return f"{f_name} {l_name}"


# format_name("cameron", "adams")
formatted_string = format_name("cameron", "adams")
print(formatted_string)
print(format_name("cameron", "adams"))


# Functions with outputs


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Please try again with valid input."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"Result: {formatted_f_name} {formatted_l_name}"


print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))

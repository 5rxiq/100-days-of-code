#######################################################
#Function with an output
#######################################################
def format_name_one(f_name, l_name):
    formatted_f_name = f_name.title()
    formateed_l_name = l_name.title()
    return f"{formatted_f_name} {formateed_l_name}"

print(format_name_one("cAm", "aDaMs"))

#######################################################
#Return Function
#######################################################
def format_name_two(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any valid inputs"
    formatted_f_name = f_name.title()
    formateed_l_name = l_name.title()
    return f"{formatted_f_name} {formateed_l_name}"

print(format_name_two(input("What is your first name? "), input("What is your last name? ")))

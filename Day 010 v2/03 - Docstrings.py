# When format_name is called, the below comment will be the prompt / documentation. 
def format_name(f_name, l_name):
    """
    Takes a first and last name and formats them into title case. 
    """
    if f_name == "" or l_name == "":
        return "Missing name input"
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"{formatted_fname} {formatted_lname}"

print(format_name(input("what is your first name? "), input("What is your last name? ")))
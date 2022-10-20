# Docstrings are ways to create little bits of documentation as we go along
def format_name(f_name, l_name):
    """Take a first and last name and format
    it to return the title case version of the name."""
    f_name = f_name.title()
    l_name = l_name.title()
#    print(f"{f_name} {l_name}")
    return f"{f_name} {l_name}"

format_name()
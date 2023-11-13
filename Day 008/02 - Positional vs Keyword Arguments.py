# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#simple function
def greet():
    print("Hello")
    print("Good Morning")
    print("Goodbye")
greet()

#function with input 

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Good Morning {name}")
    print(f"Goodbye {name}")
greet_with_name("Cameron")
#name = parameter
#Cameron = argument

#functions with more than one input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"Isn't is a beatiful day in {location}, {name}?")
#this is position arguments
greet_with("cameron","denver")
#this is keyword arguments
greet_with(location="seattle",name="arlo")
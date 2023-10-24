#Instructions
#Write a program that calculates and outputs the number of characters in any name. 
#The automated tests will try out lots of different names as the input. 
#Your code should work for any name.

name_length = len(input("Please enter a name. "))

print("That name is " + str(name_length) + " letters long.")
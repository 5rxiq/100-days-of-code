# dictionaries are made up of keys and values 

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

#Retrieving Items from Dictionary
print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Create an empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
programming_dictionary = {}

#edit an item in a dictionary 
programming_dictionary["Bug"] = "A moth in your computer"

#loop though a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
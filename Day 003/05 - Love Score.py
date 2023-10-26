#Instructions
#💪 This is a difficult challenge! 💪

#You are going to write a program that tests the compatibility between two people.

#To work out the love score between two people:

#    Take both people's names and check for the number of times the letters in the word TRUE occurs.
#    Then check for the number of times the letters in the word LOVE occurs.
#    Then combine these numbers to make a 2 digit number.

#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is *x*, you go together like coke and mentos."
#For Love Scores between 40 and 50, the message should be:
#"Your score is *y*, you are alright together."
#Otherwise, the message will just be their score. e.g.:
#"Your score is *z*."

#e.g.
#name1 = "Angela Yu"
#name2 = "Jack Bauer"

#T occurs 0 times
#R occurs 1 time
#U occurs 2 times
#E occurs 2 times
#Total = 5

#L occurs 1 time
#O occurs 0 times
#V occurs 0 times
#E occurs 2 times
#Total = 3

#Love Score = 53

#Print: "Your score is 53."
#These functions will help you:

#lower() count()
#Example Input 1

#Kanye West
#Kim Kardashian

#Example Output 1

#The Love Calculator is calculating your score...
#Your score is 42, you are alright together.

#Example Input 2

#Brad Pitt
#Jennifer Aniston

#Example Output 2

#The Love Calculator is calculating your score...
#Your score is 73.

#Hint

#You can check your values against mine using this table:
#Name 1 	Name 2 	Score
#Brad Pitt 	Jennifer Aniston 	73
#Prince William 	Kate Middleton 	67
#Ashton Kutcher 	Mila Kunis 	63
#Angela Yu 	Jack Bauer 	53
#David Beckham 	Victoria Beckham 	45
#Mario 	Princess Peach 	43
#Kanye West 	Kim Kardashian 	42

print("The Love Calculator is calculating your score...")
name1 = input("What is name 1? ") # What is your name?
name2 = input("What is name 2? ") # What is their name?
names = name1 + name2
names = names.lower()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

t = names.count("t")  
r = names.count("r") 
u = names.count("u")
e = names.count("e")
l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")

true = t + r + u + e 
love = l + o + v + e 
final_score = str(true) + str(love) 
final_score = int(final_score)

print("The Love Calculator is calculating your score...")

if final_score < 10 or final_score > 90:
    print(f"You score is {final_score}, you go together like coke and mentos.")

elif final_score >= 40 and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")

else:
    print(f"Your score is {final_score}.")

#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is *x*, you go together like coke and mentos."
#For Love Scores between 40 and 50, the message should be:
#"Your score is *y*, you are alright together."
#Otherwise, the message will just be their score. e.g.:
#"Your score is *z*."
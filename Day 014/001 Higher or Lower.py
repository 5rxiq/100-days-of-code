import game_data 
import art
import random
import os


first_compare = random.randint(0,49)
name1 = game_data.data[first_compare]['name']
follower_count1 = game_data.data[first_compare]['follower_count']
description1 = game_data.data[first_compare]['description']
country1 = game_data.data[first_compare]['country']

score = 0
keep_playing = True

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def gameplay():
    global first_compare
    global name1 
    global follower_count1
    global description1
    global country1
    global score
    global keep_playing
    
    while keep_playing is True: 
        second_compare = random.randint(0,49)

        name2 = game_data.data[second_compare]['name']
        follower_count2 = game_data.data[second_compare]['follower_count']
        description2 = game_data.data[second_compare]['description']
        country2 = game_data.data[second_compare]['country']

        correct_answer = ""
        if follower_count1 > follower_count2:
            correct_answer = 'A'
        else:
            correct_answer = 'B'

        print(art.logo)
        print(f"Compare A: {name1}, a {description1}. from {country1}.")
        print(art.vs)
        print(f"Against B: {name2}, a {description2}. from {country2}.")
        choice = input(f"\nYour current score is: {score} \nWho has more followers? Type 'A' or 'B': ").upper()
        print(f"")

        if choice.upper() == correct_answer.upper():
            name1 = name2
            follower_count1 = follower_count2
            description1 = description2
            country1 = country2
            score += 1
            clear()
        else:
            keep_playing = False
            clear()
            print(f"Game Over. Your score was {score}.")
gameplay()
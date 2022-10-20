# Write your code below this line 👇
def prime_checker(number):
    tracker = []
    for num in range(2, number):
        if number % num == 0:
            tracker.append(num)
    if(len(tracker)) == 0:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")




# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
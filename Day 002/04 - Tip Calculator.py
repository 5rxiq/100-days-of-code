#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print('Welcome to the tip calculator!')
bill_total = float(input('What was the total of your bill? $'))
tip_pct = int(input('What percent tip would you like to give? 10, 12, or 15? '))
multiplier = 1 + float(tip_pct / 100)
split_cnt = int(input('How many people are splitting the bill? ')) 
split_amt = round((bill_total * multiplier) / split_cnt,2)
split_amt = "{:.2f}".format(split_amt)

print('\n' + f'Each person should pay: ${split_amt}')


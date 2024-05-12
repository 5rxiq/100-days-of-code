def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
      else:
        print("Not leap year")
    else:
      print("Leap year")
  else:
    print("Not leap year")
  
# TODO: Add more code here 👇
def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

  leap_year_result = is_leap(year)

  if leap_year_result == "Leap year":
    month_days[1] = 29

  return month_days[month-1]


#print(is_leap(2024))
#print(days_in_month(2024,2))
  


  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: ")) # Enter a year
month = int(input("Enter a month number: ")) # Enter a month
days = days_in_month(year, month)
print(days)

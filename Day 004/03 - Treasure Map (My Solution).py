line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
#print(f"{line1}\n{line2}\n{line3}")

#x_axis = ["A","B","C"]
#y_axis = ["1","2","3"]

x_axis = position[:1]

if x_axis.lower() == "a":
    x_axis = 0
elif x_axis.lower() == "b":
    x_axis = 1
else:
    x_axis = 2

y_axis = position[-1:]
y_axis = int(y_axis) -1
print(x_axis)
print(y_axis)

map[int(y_axis)][int(x_axis)] = "X"
print(f"{line1}\n{line2}\n{line3}")

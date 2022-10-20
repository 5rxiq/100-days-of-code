student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
    if 100 >= student_scores[score] >= 91:
        student_grades[score] = "Outstanding"
    elif 90 >= student_scores[score] >= 81:
        student_grades[score] = "Exceeds Expectations"
    elif 80 >= student_scores[score] >= 71:
        student_grades[score] = "Acceptable"
    elif student_scores[score] <= 70:
        student_grades[score] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
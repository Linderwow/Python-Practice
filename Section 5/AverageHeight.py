# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height += height
print(str(total_height) + " is a total height")

# ------------------------------------
number_of_students = 0
for students in student_heights:
    number_of_students += 1
print(str(number_of_students) + " students")
average_height = round(total_height / number_of_students)
print(str(average_height) + " is an average height")

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)

# PEMDAS
# () parentheses
# ** exponents
# *  multiplication
# /  division
# +  addition
# -  subtraction

print(3 * (3 + 3) / 3 - 3)
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person
# both weigh the same amount, the short person is usually more overweight.
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
BMI = int(weight) / float(height) ** 2
print(round(BMI), 2)  # round to 2 decimal places

# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
bill = float(input("What is the total bill? "))
how_many_people = int(input("How many people are splitting the bill "))
what_is_the_tip_percentage = int(input("What is the tip percentage? 10, 12, 15 "))
total_bill=what_is_the_tip_percentage/100*bill+bill
actualBillAfterSplitting = (what_is_the_tip_percentage/100*bill+bill)/how_many_people
print(str(actualBillAfterSplitting) + "$ each has to pay")
print(str(total_bill) + "$ is a total bill")

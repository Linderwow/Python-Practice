cars = ["mercedes", "audi", "pegeot", "citroen", "mazda", "tesla", "lucid"]
for number in range(0, len(cars)):
    print(cars[number])
# ------------------------------------------
total = 0
for numbers in range(1, 101):
    if numbers % 2 == 0:
        total += numbers
print(f"{total} is a total of all even numbers")
# -----------------------or-------------------
total2 = 0
for numbers in range(1, 101, 2):
    total2 += numbers
print(f"{total2} is a total of all even numbers")

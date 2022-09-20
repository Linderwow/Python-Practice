import random

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

states_of_america = ["Delaware", "Virginia", "Washington", "New York", "Idaho"]
print(f"{states_of_america}")
print(states_of_america[0] + " is the first state in the list")
print(states_of_america[1] + " is the second state in the list")

states_of_america[1] = "Transylvania"  # will replace item under INDEX 1

states_of_america.extend(["India", "France"])  # will extend our list and add these 2 items
print(states_of_america)

# π¨ Don't change the code below π
row1 = ["ποΈ", "ποΈ", "π€―οΈ"]
row2 = ["π«οΈ", "π₯ΊοΈ", "π€«οΈ"]
row3 = ["π·οΈ", "π€οΈ", "π€€οΈ"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# π¨ Don't change the code above π

# Write your code below this row π
horizontal_position = int(position[0])  # 2
vertical_position = int(position[1])  # 3
map[vertical_position - 1][horizontal_position - 1] = "X"

# Write your code above this row π

# π¨ Don't change the code below π
print(f"{row1}\n{row2}\n{row3}")

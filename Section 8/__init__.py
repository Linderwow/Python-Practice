import random
import math
import paint_Calc
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))

coverage = random.randint(3,6)
paint_calc(height=test_h,widtht=test_w,cover=coverage)

def paint_calc(height, weight, cover):
    pass


area = height * width
num_of_cans = math.ceil(area / cover)
print(f"You'll need{num_of_cans}")

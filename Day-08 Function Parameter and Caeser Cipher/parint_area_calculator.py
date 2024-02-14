import math

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5 #one can can cover 5 square meters of a wall



def paint_calc(height,width,cover):
    no_of_cans = (height * width) / cover
    return no_of_cans



result = paint_calc(height=test_h,width=test_w,cover=coverage)
print(round(result))
print(math.ceil(result))
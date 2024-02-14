#bug 1
def my_function():
    for i in range(1,20):
        if i == 20:
            print("You got it")
        
my_function()

#bug 2 

from random import randint
dice_img = ["1","2","3","4","5","6"]
# dice_nums = randint(1,6)
dice_nums = randint(0,5)
print(dice_nums)
print(dice_img[dice_nums])




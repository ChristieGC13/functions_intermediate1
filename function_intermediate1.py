
import random 

def randInt(min = 0, max = 100):
    if (min > max):
        print("Max must be greater than min")
        return
    if (max < 0 or min < 0 ):
        print("Must be positive numbers")
        return
    num = round(random.random() * (max - min) + min)
    return num

print(randInt(min = -100, max = 100))
# should print a random integer between 0 to 100
# print(randInt(max=50))
# should print a random integer between 0 to 50
# print(randInt(min=50))
# should print a random integer between 50 to 100
# print(randInt(min=50, max=500))
# # should print a random integer between 50 and 500

# Bonus: Account for any edge cases(eg. min > max, max < 0)

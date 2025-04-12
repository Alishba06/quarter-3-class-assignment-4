
# Built-in Modules

# math
# random
# os



# math

# import math

# print(math.sqrt(16))   # Output: 4.0


# random

# import random

# print(random.randint(1,100))  # Random number between 1 and 100


# os

# import os

# print(os.getcwd())  # Current working directory



# sys 

# import sys

# print(sys.version) # Python version





# function in python 


# def greet(name):
#     print(f"Hello,{name}!")

# greet("AlishbaBoss")
# greet("Aliza")
# greet("Maila")





# Global Function


# def say_hello():               # Ye say_hello() ek global function hai.
#     print("hello world")



# Utility Function 


# def is_even(n):
#     return n % 2 == 0

# print(is_even(4))   # True




# Immutable (unchangeable) objects

# Jaise: int, float, str, tuple


def change_number(x):
    x = x + 10
    print("Inside:", x)


num = 5
change_number(num)
print("Outside:", num)



# Mutable (changeable) objects

# Jaise: list, dict, set


# def add_item(my_list):
#     my_list.append(4)
#     print("Inside:", my_list)


# numbers = [1,2,3]
# add_item(numbers)
# print("Outside:", numbers)




# Function Arguments 

def greet(name):
    print(f"Hello, {name}") # ya function ka parameter hai

greet("Alishba") # yahan argumenthai




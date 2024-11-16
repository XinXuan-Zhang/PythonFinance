# -*- coding: utf-8 -*-
"""7functions_Alex.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18feZ5ueN9gmkXjsqw27-FHmtrm4J_ZBo
"""

# 7functions.py

# 7.1 Functions

# 7.1.1 Create a function named function1 that prints this string "Hello World"
# TODO: Write your code below
def function1():
    print("Hello World")
function1()





# 7.1.2 Execute the functon function1
# TODO: Write your code below

function1()






# 7.1.3 Create a function named function2 that takes in one integer parameter number1. The function adds 5 to the input number1, and prints the result
# TODO: Write your code below
def function2(number1):
    result = number1 + 5
    print(result)
function2(10)





# 7.1.4 Create a function named compare_numbers() with two arguments. If the first argument is greater than the second, print "first number is greater".
# If the second number is greater than the first, print "first number is smaller". Is the numbers are equal, print "equal numbers"
# TODO: Write your code below
def compare_numbers(num1, num2):
    if num1 > num2:
        print("first number is greater")
    elif num1 < num2:
        print("first number is smaller")
    else:
        print("equal numbers")
compare_numbers(10, 5)
compare_numbers(3, 7)
compare_numbers(8, 8)






# 7.2 Create a lambda function that takes one parameter (a) and returns it.
# TODO: Write your code below
return_value = lambda a: a
print(return_value(10))  # Expected output: 10





### 7.3 Python built-in functions : https://www.w3schools.com/python/python_ref_functions.asp

nums = [11,33,14,2,58,65,34]

# 7.3.1 Using Python's built in sum() function, print the sum of the numbers in the list nums
# TODO: Write your code below
nums = [11, 33, 14, 2, 58, 65, 34]
print(sum(nums))





# 7.3.2 Using Python's built in min() function, print the minimum of the numbers in the list nums
# TODO: Write your code below
nums = [11, 33, 14, 2, 58, 65, 34]
print(min(nums))





# 7.3.3 Using Python's built in abs() function, print the absolute value of -6.
# TODO: Write your code below
print(abs(-6))




# 7.3.4 Using Python's built in round() function, round the number 4.67888 to two decomal places.
# TODO: Write your code below
rounded_value = round(4.67888, 2)
print(rounded_value)





# 7.4 Python Modules
# HINT: https://www.w3schools.com/python/python_modules.asp
# HINT: https://realpython.com/python-modules-packages/
# HINT: https://docs.python.org/3/tutorial/modules.html


# 7.4.1 Create a python module mod.
# In mod.py, create a function psum(number1, number2) that takes two arguments and prints the sum of them. Assume the input arguments to be numbers.
# In mod.py, create a function pmultiply(number1, number2) that takes two arguments and prints the product of them. Assume the input arguments to be numbers.

def psum(number1, number2):
    result = number1 + number2
    print(result)

def pmultiply(number1, number2):
    result = number1 * number2
    print(result)


# 7.4.2 Create python file main.py and import the module mod.
# In main.py run the psum() and pmultiply() functions from the module mod using any two numbers.

import mod
mod.psum(10, 5)
mod.pmultiply(10, 5)


# 7.4.3 In main.py, also import Python's built in module platform. Then list the functions and variables in the platform module using the dir() function.
import mod

import platform
print(dir(platform))
mod.psum(10, 5)
mod.pmultiply(10, 5)
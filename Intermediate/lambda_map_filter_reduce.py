# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can take any number of arguments but can only have one expression.

# squared = lambda num: num * num without auto formatting
def squared(num):
    return num * num
# lambda num : num * num
print(squared(5))  # Output: 25 

def addTwo(num): lambda num: num + 2        
print(addTwo(3))  # Output: 5 

lambda a, b : a + b  # without auto formatting
sum_total = lambda a, b: a + b
print(sum_total(10, 5))  # Output: 15

# ================================================================

def funcbuilder(x):
    return lambda num : num + x

addTen = funcbuilder(10)
addTwenty = funcbuilder(20)

print(addTen(7))    # Output: 17. 7 = the 'num' parameter and 10 = the 'x' parameter
print(addTwenty(7)) # Output: 27. 7 = the 'num' parameter and 20 = the 'x' parameter

# ===========================Higher Order Functions===============================

# Higher order functions are functions that can take other functions as arguments or return functions as results.


numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num: num * num, numbers) # map applies the lambda function to each item in the numbers list

print(list(squared_nums))  # Output: [9, 49, 144, 324, 400, 441] if you want it to output a list, you must use the list constructor eg list(squared_nums))
# If you just print squared_nums, it will show a map object like <map object at 0x7f9b8c0d1d60> MAP is very handy

# ==================================Filter function===================================================

lambda num : num % 2 != 0 # % = modulus operator, it gives the remainder of a division operation

odd_nums = filter(lambda num: num % 2 != 0, numbers) # filter applies the lambda function to each item in the numbers list and only keeps those for which the function returns True
print(list(odd_nums))  # Output: [3, 7, 21] if you want it to output a list, you must use the list constructor eg list(odd_nums))

even_nums = filter(lambda num: num % 2 == 0, numbers) # filter applies the lambda function to each item in the numbers list and only keeps those for which the function returns True
print(list(even_nums))  # Output: [12, 18, 20] if you want it to output a list, you must use the list constructor eg list(even_nums))

# ==================================Reduce function===================================================

from functools import reduce
# reduce applies the lambda function cumulatively to the items in the numbers list, from left to right, so as to reduce the list to a single value

lambda acc, curr: acc + curr # acc = accumulator, curr = current value

numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers) # 1+2+3+4+5+1 = 16
print(total)  # Output: 16

print(sum(numbers)) # Output: 16, this is a built-in function that does the same thing as the reduce function above

total_from_50 = reduce(lambda acc, curr: acc + curr, numbers, 50) # 50+1+2+3+4+5+1 = 66
print(total_from_50)  # Output: 66, this is a built-in function that does the same thing as the reduce function above
print(sum(numbers, 50)) # Output: 66, this is a built-in function that does the same thing as the reduce function above

lambda acc, curr: acc + len(curr)
words = ["hello", "world", "python", "is", "awesome"]
character_count = reduce(lambda acc, curr: acc + len(curr), words,0)
print(character_count)  # Output: 21, this is a built-in function that does the same thing as the reduce function above
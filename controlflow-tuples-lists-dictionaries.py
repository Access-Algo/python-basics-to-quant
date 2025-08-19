# ================ User Input Rock Paper Scissors Game ===============
# import sys
# import random
# from enum import Enum

# class RPS(Enum):
#     ROCK = 1
#     PAPER = 2
#     SCISSORS = 3


# print(" ")
# playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper or \n3 for Scissors:\n")
# player = int(playerchoice)

# if player < 1 or player > 3: 
#     sys.exit("Invalid choice, enter 1/2/3") 

# computerchoice = random.choice("123")
# computer = int(computerchoice)

# print("")
# print("You chose: " + str(RPS(player)).replace("RPS." , "") + ".")
# print("Python chose: " + str(RPS(computer)).replace("RPS." , "") + ".")
# print("")

# if player == 1 and computer == 3: 
#     print("You win")
# elif player == 2 and computer == 1: 
#     print("you win")
# elif player == 3 and computer == 2: 
#     print("you win")
# elif player == computer:
#     print("It's a draw!")
# else:
#     print ("Python WINS!")

#=================== Lists and Tuples ===================

users= ["Alice", "Bob", "Dave"]

data = [ 'Dave', 42 , True, 3.14, "Hello" ]

empty_list = [] 

print("Dave" in users)  # True
print("Dave" in data)  # True
print("Dave" in empty_list)
print(users[0])  # Alice
print(users[-2])  # Bob

print(users.index("Bob"))
print(users[0:2])  # ['Alice', 'Bob']
print(users[1:])  # ['Bob', 'Dave']
print(users[-3:-1])  # ['Bob', 'Dave']  

print(len(data)) # 5    

users.append("Eve")
print(users)  # ['Alice', 'Bob', 'Dave', 'Eve']

users += ["Frank"]
print(users)  # ['Alice', 'Bob', 'Dave', 'Eve', 'Frank']

users.extend(["Grace", "Heidi"])
print(users)  # ['Alice', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']

# users.extend(data)
# print(users)  # ['Alice', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi', 'Dave', 42, True, 3.14, 'Hello']

users.insert(0, "Zoe")
print(users)  # ['Zoe', 'Alice', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']
users[2:2] = ["Charlie", "Bobert"]
print(users)  # ['Zoe', 'Alice', 'Charlie', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']    
users[1:3] = ["Alicia", "Bobby"] #this is called a SLICE
print(users)  # ['Zoe', 'Alicia', 'Bobby', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']

users.remove("Zoe")
print(users)  # ['Alicia', 'Bobby', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']
print(users.pop()) 
print(users)  # ['Alicia', 'Bobby', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace']

del users[0]
print(users)  # ['Bobby', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace']   

data.clear()
print(data)  # []

users.sort()
print(users)  # ['Bob', 'Bobby', 'Dave', 'Eve', 'Frank', 'Grace']

users[1:2] = ["dave"]   
users.sort()
print(users)  # ['Bob', 'dave', 'Dave', 'Eve', 'Frank', 'Grace']


users.sort(key=str.lower)
print(users)

nums = [5, 2, 9, 1, 5, 6]   
nums.reverse() 
print(nums)  # [6, 5, 1, 9, 2, 5]

# nums.sort(reverse=True)
# print(nums)  # [9, 6, 5, 5, 2, 1]

print(sorted(nums, reverse=True))
print(nums)  # [6, 5, 1, 9, 2, 5] (original list remains unchanged)    

#copying lists
numscopy = nums.copy()
mynums = list(nums)  # another way to copy a list
mycopy = nums[:]        
print(numscopy)  # [6, 5, 1, 9, 2, 5]
print(mynums)  # [6, 5, 1, 9, 2, 5]
print(mycopy)  # [6, 5, 1, 9, 2, 5]
print(nums)  # [6, 5, 1, 9, 2, 5]

print(type(numscopy))  # <class 'list'> 

my_list = list([1, 2, 3])
print(my_list)  # [1, 2, 3]

#===========================tuples
my_tuple = tuple([1, 2, 3])
another_tuple = (4, 5, 6, 7, 2, 2)   

print(my_tuple)  # (1, 2, 3)
print(another_tuple)  # (4, 5, 6)
print(type(my_tuple))  # <class 'tuple'>
print(type(another_tuple))  # <class 'tuple'>

newlist = list(my_tuple)
newlist.append(10)
newtuple = tuple(newlist)
print(newtuple)  # (1, 2, 3, 10) #packing the tuple

#unpacking the tuple
a, b, c, *d = another_tuple 
print(a)  # 4
print(b)  # 5
print(c)  # 6
print(d)  # [7, 2, 2] * = collecting the rest

print(another_tuple.count(2))  # 2 (counts how many times 2 appears in the tuple)
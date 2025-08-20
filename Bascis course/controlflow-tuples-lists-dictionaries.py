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

# users= ["Alice", "Bob", "Dave"]

# data = [ 'Dave', 42 , True, 3.14, "Hello" ]

# empty_list = [] 

# print("Dave" in users)  # True
# print("Dave" in data)  # True
# print("Dave" in empty_list)
# print(users[0])  # Alice
# print(users[-2])  # Bob

# print(users.index("Bob"))
# print(users[0:2])  # ['Alice', 'Bob']
# print(users[1:])  # ['Bob', 'Dave']
# print(users[-3:-1])  # ['Bob', 'Dave']  

# print(len(data)) # 5    

# users.append("Eve")
# print(users)  # ['Alice', 'Bob', 'Dave', 'Eve']

# users += ["Frank"]
# print(users)  # ['Alice', 'Bob', 'Dave', 'Eve', 'Frank']

# users.extend(["Grace", "Heidi"])
# print(users)  # ['Alice', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']

# # users.extend(data)
# # print(users)  # ['Alice', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi', 'Dave', 42, True, 3.14, 'Hello']

# users.insert(0, "Zoe")
# print(users)  # ['Zoe', 'Alice', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']
# users[2:2] = ["Charlie", "Bobert"]
# print(users)  # ['Zoe', 'Alice', 'Charlie', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']    
# users[1:3] = ["Alicia", "Bobby"] #this is called a SLICE
# print(users)  # ['Zoe', 'Alicia', 'Bobby', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']

# users.remove("Zoe")
# print(users)  # ['Alicia', 'Bobby', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace', 'Heidi']
# print(users.pop()) 
# print(users)  # ['Alicia', 'Bobby', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace']

# del users[0]
# print(users)  # ['Bobby', 'Bob', 'Dave', 'Eve', 'Frank', 'Grace']   

# data.clear()
# print(data)  # []

# users.sort()
# print(users)  # ['Bob', 'Bobby', 'Dave', 'Eve', 'Frank', 'Grace']

# users[1:2] = ["dave"]   
# users.sort()
# print(users)  # ['Bob', 'dave', 'Dave', 'Eve', 'Frank', 'Grace']


# users.sort(key=str.lower)
# print(users)

# nums = [5, 2, 9, 1, 5, 6]   
# nums.reverse() 
# print(nums)  # [6, 5, 1, 9, 2, 5]

# # nums.sort(reverse=True)
# # print(nums)  # [9, 6, 5, 5, 2, 1]

# print(sorted(nums, reverse=True))
# print(nums)  # [6, 5, 1, 9, 2, 5] (original list remains unchanged)    

# #copying lists
# numscopy = nums.copy()
# mynums = list(nums)  # another way to copy a list
# mycopy = nums[:]        
# print(numscopy)  # [6, 5, 1, 9, 2, 5]
# print(mynums)  # [6, 5, 1, 9, 2, 5]
# print(mycopy)  # [6, 5, 1, 9, 2, 5]
# print(nums)  # [6, 5, 1, 9, 2, 5]

# print(type(numscopy))  # <class 'list'> 

# my_list = list([1, 2, 3])
# print(my_list)  # [1, 2, 3]

# #===========================tuples===========================
# my_tuple = tuple([1, 2, 3])
# another_tuple = (4, 5, 6, 7, 2, 2)   

# print(my_tuple)  # (1, 2, 3)
# print(another_tuple)  # (4, 5, 6)
# print(type(my_tuple))  # <class 'tuple'>
# print(type(another_tuple))  # <class 'tuple'>

# newlist = list(my_tuple)
# newlist.append(10)
# newtuple = tuple(newlist)
# print(newtuple)  # (1, 2, 3, 10) #packing the tuple

# #unpacking the tuple
# a, b, c, *d = another_tuple 
# print(a)  # 4
# print(b)  # 5
# print(c)  # 6
# print(d)  # [7, 2, 2] * = collecting the rest

# print(another_tuple.count(2))  # 2 (counts how many times 2 appears in the tuple)


#============================dictionaries & sets===========================

band = {
    "vocals": "Plant",
    "guitar": "Page",
    "bass": "Jones",
    "drums": "Bonham"
}

band2 = dict(vocals="Plant", guitar="Page", bass="Jones", drums="Bonham")

print(band)
print(band2)
print(type(band))  # <class 'dict'>
print(len(band))  # 4 (number of key-value pairs)

# Access Items
print(band["vocals"])  # Plant
print(band.get("guitar"))  # Page   

#list all keys
print(band.keys())  # dict_keys(['vocals', 'guitar', 'bass', 'drums'])
#list all values
print(band.values())  # dict_values(['Plant', 'Page', 'Jones', 'Bonham'])

#list of key/value pairs as tuples
print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page'), ('bass', 'Jones'), ('drums', 'Bonham')])

#varify if key exists
print("vocals" in band)  # True
print("keyboard" in band)  # False
print("triangle" in band)  # False

#change values
band["vocals"] = "Freddie"
band.update({"bass": "Brian"})

print(band)  # {'vocals': 'Freddie', 'guitar': 'Page', 'bass': 'Brian', 'drums': 'Bonham'}

#remove items
print(band.pop("bass"))
print(band)  # {'vocals': 'Freddie', 'guitar': 'Page', 'drums': 'Bonham'}

band["drums"] = "Roger" 
print(band)  # {'vocals': 'Freddie', 'guitar': 'Page', 'drums': 'Roger'}
print(band.popitem())  # ('drums', 'Roger' )
print(band)  # {'vocals': 'Freddie', 'guitar': 'Page'}

#delete and clear
band["drums"] = "Bonham"
del band["drums"]   
print(band)  # {'vocals': 'Freddie', 'guitar': 'Page'}

band2.clear()
print(band2)  # {}
del band2

#copy dictionaries

# band2 = band #creates only a reference not a copy dont do this
# print("Bad Copy!")
# print(band2)  # {'vocals': 'Freddie', 'guitar': 'Page'}
# print(band)

# band2["drums"] = "Dave"
# print(band) #shows it changes both dictionaries, dont copy this way, you want a fresh copy

band2 = band.copy()  # creates a copy
band2["drums"] = "Dave"
print("good copy")
print(band)
print(band2)  # {'vocals': 'Freddie', 'guitar': 'Page', 'drums': 'Dave'}

#another way, constructor function
band3 = dict(band)  # creates a copy
print("good copy")
print(band3)

#nested dictionaries 

member1 = {
    "Name" : "Plant",
    "Instrument" : "Vocals"
}

member2 = {
    "Name" : "Page",
    "Instrument" : "Guitar"
}


band = {
    "member1": member1,
    "member2": member2,
}

print(band)
print(band["member1"]["Name"])  # Plant going down levels in the dictionary to find the data

#sets

nums = {1, 2, 3, 4, 5}
nums2 = set ((1,2,3,4))
print(nums)  # {1, 2, 3, 4, 5}
print(nums2)  # {1, 2, 3, 4}
print(type(nums))  # <class 'set'>
print(len(nums))  # 5 (number of unique items   )

#no duplicates allowed!
nums3 = {1, 2, 3, 4, 5, 5, 5}
print(nums3)  # {1, 2, 3, 4, 5} (duplicates are removed)

#a True value is a dupe of 1, False is a dupe of 0

nums = {1, True, 2, False, 3, 4, 0}
print(nums)  # {0, 1, 2, 3, 4} (True is treated as 1 and False as 0)

#check if a value is in a set
print(2 in nums)  # True
print(5 in nums)  # False
#but you  cannot refer to an element in a set with an index position or a key

#add a new element to a set
nums.add(6)
print(nums)  # {0, 1, 2, 3, 4, 6}

#add elements from one set to another

morenums = {7, 8, 9}
nums.update(morenums)
print(nums)  # {0, 1, 2, 3, 4, 6, 7, 8, 9}

#you can use update with lists, tuples and dictionaries too

#merge two sets to make a new set
one = {1,2,3}
two = {5,6,7}
mynewset = one.union(two)
print(mynewset)  # {1, 2, 3, 5, 6, 7}

#keep the duplicates only
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)  # {2, 3}

#Keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)  # {1}

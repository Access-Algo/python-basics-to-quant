# ======================Functions====================

# def hello():
#     print("Hello, World!")

# hello() #must all be lowercase or with_these_underscore_things

# # def sum_of(num1, num2):
# #     print(num1 + num2)

# # sum_of(5, 10) # this will print 15
# # sum_of(20, 30) # this will print 50
# # sum_of(100, 200) # this will print 300
# # sum_of("1", "2") # this will print 12 (string concatenation)

# def sum_of(num1=0, num2=0):
#     if (type(num1) != int or type(num2) != int):
#         return "Invalid input, input integers only"
#     return num1 + num2

# total = sum_of(2,2) # this will return 4
# print(total) # prints 4

# def multiple_items(*args):
#     print(args) # prints a tuple of all arguments passed
#     print(type(args)) # prints <class 'tuple'>

# multiple_items(1, 2, 3, 4, 5) # prints (1, 2, 3, 4, 5)

# def multiple_named_items(**kwargs):
#     print(kwargs) # prints a dictionary of all named arguments passed
#     print(type(kwargs)) # prints <class 'dict'>

# multiple_named_items(name="Alice", age=30, city="New York") 



#============================Recursion============================

# def add_onee(num):

#     if (num >=9):
#         return num + 1
    
#     total = num + 1
#     print(total)

#     return add_onee(total)

# add_onee(0) # this will print 1, 2, 3, ..., 10 and return 11

# for i in range(10):
#     i + 1
#     print(i + 1)



# #===============while loops further================

# value = True
# count = 4
# while value:
#     count += 1
#     print(count)
#     if count == 5:  # Change this condition to control the number of iterations
#         break
#     else: 
#         value = False  # This will stop the loop after one iteration
#         continue  # This will skip the rest of the loop and start the next iteration




import sys
import random
from enum import Enum


def rock_paper_scissors():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3


    print(" ")
    playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper or \n3 for Scissors:\n")
    player = int(playerchoice)
    if playerchoice not in ["1", "2", "3"]:
        print
        sys.exit("Invalid choice, enter 1/2/3")
        return rock_paper_scissors()


    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("")
    print("You chose: " + str(RPS(player)).replace("RPS." , "") + ".")
    print("Python chose: " + str(RPS(computer)).replace("RPS." , "") + ".")
    print("")

    if player == 1 and computer == 3: 
        print("You win")
    elif player == 2 and computer == 1: 
        print("you win")
    elif player == 3 and computer == 2: 
        print("you win")
    elif player == computer:
        print("It's a draw!")
    else:
        print ("Python WINS!")

    print("play again?")
    while True:
        playagain = input("\n(yes/no): ")
        if playagain.lower() not in ["yes", "no"]:
            continue
        else:
            break
    if playagain.lower() == "yes":
        return rock_paper_scissors()
    else: print("Thanks for playing!")
    sys.exit("Bye! ")

rock_paper_scissors()  # Uncomment to play the game
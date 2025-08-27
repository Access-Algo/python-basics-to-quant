#================loops=============
#while loops

# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break  # Exit the loop when value is 5 (break value)
#     value += 1  

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue  # Skip the rest of the loop when value is 5
#     print(value)  # This line will be skipped when value is 5
# else:
#     print("Value is now equal to " + str(value))

#================for loops=====================

names = ["Alice", "Bob", "Charlie", "David"]
# for name in names:
#     print("Hello, " + name + "!")

# for x in "mississippi":
#     print(x)

#finding things
# for x in names:
#     if x == "Bob":
    
#         print("Found " + x)

# #skipping things
# for x in names:
#     if x == "Bob":
#         continue
#     print("Found " + x)

#Ranges

# for x in range(4):
#     print(x)
# for x in range(2,4):
#     print(x)

# for x in range(5,101,5):
#     print(x)
# else:
#     print("Finished printing multiples of 5")

# names = ["Alice", "Bob", "Charlie", "David"]
# actions = ["greet", "find", "skip", "print"]

# # for name in names:
# #     for action in actions:
# #         print(name + " will " + action + " now.")

# for action in actions:
#     for name in names:
#         print(name + " will " + action + " now.")


#============rock paper scissors game loop additions

# ================ User Input Rock Paper Scissors Game ===============
import sys
import random
from enum import Enum

def rock_paper_scissors():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playagain = True

    while playagain:


        print(" ")
        playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper or \n3 for Scissors:\n")
        player = int(playerchoice)

        if player < 1 or player > 3: 
            sys.exit("Invalid choice, enter 1/2/3") 

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

        playagain = input("\nDo you want to play again? \n(yes/no): ")
        if playagain.lower() == "no":
            playagain = False
            print("\nThanks for playing!")
        else: 
            print("\nLet's play again!")
            
            
sys.exit("Bye!")

rock_paper_scissors()


import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print(" ")
playerchoice = input("Enter ... \n1 for Rock, \n2 for Paper or \n3 for Scissors:\n")
player = int(playerchoice)

if player < 1 | player > 3: 
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


# #==========================scopes==========================
# from turtle import color


# name = "bob"



# # greeting("smith")

# count = 1

# def examplefunction():
#     color = "blue"

#     global count
#     count = 2

#     print(count)
#     def greeting(surname):
#         print("Hello " + name)
#         nonlocal color
#         color = "red"   
#         print(color)
#         print(surname)
#     greeting("smith")
#     print("This is an example function.")

# examplefunction()



# Rock Paper Scissors optimisation using scope=====================================================

import sys
import random
from enum import Enum

game_round = 0

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
    def decide_winner(player,computer):
        if player == 1 and computer == 3: 
            return "You win"
        elif player == 2 and computer == 1: 
            return "you win"
        elif player == 3 and computer == 2: 
            return "you win"
        elif player == computer:
            return "It's a draw!"
        else:
            return "Python WINS!"
    game_result = decide_winner(player, computer)
    print(game_result)

    global game_round
    game_round += 1
    print("\ngame round " + str(game_round))
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
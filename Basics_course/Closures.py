#====================closures=========================
#Closure is a function having access to the scope of its parents even after the parent function has finished execution.     

# def parent_function(person,coins):
#     #coins = 3

#     def play_game():
#         nonlocal coins 
#         coins -= 1

#         if coins > 1:
#             print("\n" + person + " has " + str(coins) + " coins left. Play again!")

#         elif coins == 1:
#             print("\n" + person + " has " + str(coins) + " coin left. Play again!")
        
#         else:
#             print("\n" + person + " has " + str(coins) + " No coins left. Game Over!")
#     return play_game 

# tommy = parent_function("Tommy",3)
# jenny = parent_function("Jenny",5)

# tommy()
# tommy()
# jenny()
# tommy()
# jenny()
# jenny()


import sys
import random
from enum import Enum

def rps():
    game_round = 0
    player_wins = 0
    python_wins = 0

    def rock_paper_scissors():
        nonlocal player_wins
        nonlocal python_wins

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
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3: 
                player_wins += 1
                return "You win"
            elif player == 2 and computer == 1: 
                player_wins += 1
                return "you win"
            elif player == 3 and computer == 2: 
                player_wins += 1
                return "you win"
            elif player == computer:
                return "It's a draw!"
            else:
                python_wins += 1
                return "Python WINS!"
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_round
        game_round += 1

        print("\nGame round " + str(game_round))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))

        print("play again?")
        while True:
            playagain = input("\n(y for yes/n for no): ")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return rock_paper_scissors()
        else: print("Thanks for playing!")
        sys.exit("Bye! ")
    return rock_paper_scissors()


play = rps()  # Uncomment to play the game

play()
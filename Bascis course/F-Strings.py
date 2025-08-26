# person = "Alice"
# age = 30
# greeting = f"Hello, my name is {person} and I am {age} years old."  #actual fstring
# print(greeting)

# message = "\n%s is %s years old." % (person, age)
# print(message)  

# message2 = "\n{} is {} years old.".format(person, age)
# print(message2)  

# message3 = "\n{1} is {0} years old.".format(age, person)
# print(message3)  

# message4 = "\n{person} is {age} years old.".format(age=age, person=person)
# print(message4)  

# player = {"person": "Alice", "age": "30"}
# message5 = "\n{person} is {age} years old.".format(**player)
# print(message5)  

# # this is actually f-strings

# messagef = f"\n{person} is {age} years old."
# print(messagef)
# messagef = f"\n{person} is {10+20} years old."
# print(messagef)
# messagef = f"\n{person.upper()} is {age} years old."
# print(messagef)
# messagef = f"\n{player['person']} is {player['age']} years old."
# print(messagef)

# # f string formatting options

# num = 10
# print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")  # .2f means 2 decimal places

# for num in range(1, 11):
#     print(f"\n2.25 times {num} is {2.25 * num:.2f}") 

# for num in range(1, 11):
#     print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}")

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
        print(f"You chose: {str(RPS(player)).replace("RPS." , "").title()}.")
        print(f"Python chose: {str(RPS(computer)).replace("RPS." , "").title()}.\n")
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

        print(f"\nGame round {str(game_round)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")

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
# def hello(name,lang):
#     greetings = {"English" : "Hello", "Spanish" : "Hola", "French" : "Bonjour", "German" : "Guten Tag"}
#     msg = f"{greetings[lang]} {name}!"
#     print(msg)

# if __name__ =='__main__':
#     import argparse

#     parser = argparse.ArgumentParser(description="Provides a personal greeting")
#     parser.add_argument("-n", "--name", metavar="--name", required = True, help="Name of the person to greet")
    
#     parser.add_argument("-l", "--lang", metavar="language", required=True, choices=["English", "Spanish", "French", "German"], help="Language of the greeting")

#     args = parser.parse_args()
#     hello(args.name, args.lang)



import sys
import random
from enum import Enum

def rps(name="PlayerOne"):
    game_round = 0
    player_wins = 0
    python_wins = 0

    def rock_paper_scissors():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3


        print(" ")
        playerchoice = input(f"Enter {name}'s choice: \n1 for Rock, \n2 for Paper or \n3 for Scissors:\n")
        player = int(playerchoice)
        if playerchoice not in ["1", "2", "3"]:
            print(f"Invalid choice {name}, please enter 1/2/3")
            return rock_paper_scissors()


        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("")
        print(f"{name}, you chose: {str(RPS(player)).replace("RPS." , "").title()}.")
        print(f"Python chose: {str(RPS(computer)).replace("RPS." , "").title()}.\n")
        print("")
        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3: 
                player_wins += 1
                return f"{name} you win"
            elif player == 2 and computer == 1: 
                player_wins += 1
                return f"{name} you win"
            elif player == 3 and computer == 2: 
                player_wins += 1
                return f"{name} you win"
            elif player == computer:
                return "It's a draw!"
            else:
                python_wins += 1
                return f"Python WINS!, sorry {name}..."
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_round
        game_round += 1

        print(f"\nGame round {game_round}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"play again, {name}?")
        while True:
            playagain = input("\n(y for yes/n for no): ")
            if playagain.lower() not in ["y", "n"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return rock_paper_scissors()
        else: print(f"Thanks for playing, {name}!")
        sys.exit(f"Bye, {name}!")
    return rock_paper_scissors()



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personalised experience")
    parser.add_argument("-n", "--name", metavar="--name", required = True, help="Name of the person playing the game")
    
    args = parser.parse_args()
   

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()   
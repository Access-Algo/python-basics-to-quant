import sys
from CommandLineArguments import rps
from guess_number import guess_number


def play_game(name="Player 1"):
    welome_back = False

    while True:
        if welcome_back == True:
            print(f"\nWelcome back to the Arcade Menu, {name}!\n")

        playerchoice = input(f"\n{name}, please choose a game to play:\n\n1. Rock, Paper, Scissors\n2. Guess the Number\nX Exit\n\n")

        if playerchoice not in ['1', '2', 'X', 'x']:
            print(f"\nInvalid input {name}. Please enter 1, 2, or X.")
            return play_game(name)
        
        welcome_back = True

        if playerchoice == '1':
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == '2':
            guess_the_number = guess_number(name)
            guess_the_number()
        elif playerchoice in ['X', 'x']:
            print(f"\nThanks for playing, {name}! Goodbye!\n")
            sys.exit()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Arcade Game Menu")
    parser.add_argument('--name', type=str, default="Player 1", help='Name of the player')

    args = parser.parse_args("welcome to the arcade")
    
    play_game(args.name)

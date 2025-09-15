import sys
import random

def guess_number(name="Player 1"):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(f"\n{name}, guess what number I'm thinking of (1-3): \n\n")

        if playerchoice not in ['1', '2', '3']:
            print(f"\nInvalid input {name}. Please enter a number between 1 and 3.")
            return play_guess_number()
        
        computerchoice = random.choice("123")

        print(f"\n{name}, you chose {playerchoice}.") 
        print(f"\nI chose {computerchoice}.\n")

        player = int(playerchoice)
        computer = int(computerchoice)

        def determine_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"\n{name}, you win!"
            else:
                return f"\n{name}, I win!"
            
        game_result = determine_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n Game count: {game_count}")
        print(f"\n{name}, your total wins: {player_wins}")
        print(f"\nYour win percentage: {player_wins / game_count * 100:.2f}%")

        print("\nDo you want to play again? (yes/no)")

        while True:
            playagain = input("\n Y for Yes, N for No: \n\n")
            if playagain.lower() not in ["y", "n"]:
                print("\nInvalid input. Please enter Y or N.")
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print(f"\nThanks for playing, {name}! Goodbye!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye, {name}!")
            else:
                return
    return play_guess_number

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Play a number guessing game.")

    parser.add_argument('--name', type=str, default="Player 1", help='Name of the player')
    args = parser.parse_args()

    guess_number_game = guess_number(name=args.name)
    guess_number_game()
    
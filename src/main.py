
from game import Game


def main() -> None:
    
    print_title()
    print_introduction()
    
    play_again = True
    while play_again:
        game = Game()
        print("Do you want to play against:\n"
              "  1. another player\n"
              "  2. against the computer\n")
        opponent = choose_opponent_prompt()
        if opponent == 1: # Another player
            while not game.game_over:
                game.player_turn()
        else: # Computer
            turn_counter = 0
            while not game.game_over:
                if turn_counter % 2 == 0:
                    game.player_turn()
                else:
                    game.computer_turn()
                turn_counter += 1
                
        response = play_again_prompt()
        play_again = response


# Print an ASCII art title for the game.
def print_title() -> None:
    title = r"""
  _______                __                       __           
 /_  __(_)____          / /_____  _____          / /_____  ___ 
  / / / / ___/ ______  / __/ __ `/ ___/ _____   / __/ __ \/ _ \
 / / / / /__  /_____/ / /_/ /_/ / /__  /_____/ / /_/ /_/ /  __/
/_/ /_/\___/          \__/\__,_/\___/          \__/\____/\___/ 
"""
    print(title)


# Print an explanation of rules and how the game is played
def print_introduction() -> None:
    introduction = """
Welcome to play Tic-tac-toe! Here's how to play:

1. This game is played on a 3x3 board, laid out like this:

     1 | 2 | 3
    ----------- 
     4 | 5 | 6        
    -----------                                        
     7 | 8 | 9

   At first all of the squares are empty but the numbers here signify
   the numbers of the squares.
   
2. Two players take turns, one as "X" and the other as "O". Player X goes first.
   On your turn, you can choose a square on the board to place your symbol in.
   That's done by entering the number of the square you want to choose.
   You can't choose a square that's already been taken.

3. You win by placing three of your symbols in a row, column, or diagonal.

4. A game can also end in a tie if all of the squares are taken but no one has won.

"""
    print(introduction)


def choose_opponent_prompt() -> int:
    while True:
        try:
            response = int(input('Write "1" for another player'
                             'or "2" for the computer: ').strip())
            if response in {1, 2}:
                return response
            else:
                raise ValueError
        except ValueError:
            print('Invalid response! Please answer with "1" or "2".')


def play_again_prompt() -> bool:
    while True:
        try:
            response = input("Do you want to play again? (yes/no): ")
            match response.strip().lower():
                case "y" | "yes":   return True
                case "n" | "no":   return False
                case _:     raise ValueError
        except ValueError:
            print('Invalid response! Please answer with "yes" or "no".\n')


if __name__ == "__main__":
    main()

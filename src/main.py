
from game import Game

def main() -> None:
    print("\nWelcome to this tic-tac-toe game!\n"
          "The game works by writing the number (1-9) "
          "of the square you want to choose on your turn.\n\n"
          "The game board can be visualized like this: \n\n"
          "    1 | 2 | 3    \n"
          "   -----------   \n"
          "    4 | 5 | 6    \n"
          "   -----------   \n"
          "    7 | 8 | 9    \n")
    
    play_again = True
    while play_again:
        game = Game()
        print("\nDo you want to play against:\n"
              "    1. another player\n"
              "    2. against the computer\n")
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

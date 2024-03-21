
from ai import AI
from game import Game


def main() -> None:
    print_title()
    print_introduction()

    play_again = True
    while play_again:
        game = Game()
        opponent = choose_opponent_prompt()
        if opponent == 1:
            while not game.game_over:
                player_turn(game)
        else:
            ai = AI("O")
            turn_counter = 0
            while not game.game_over:
                if turn_counter % 2 == 0:
                    player_turn(game)
                else:
                    ai_turn(game, ai)
                turn_counter += 1
    
        response = play_again_prompt()
        play_again = response


def print_title() -> None:
    title = r"""
      _______                __                       __           
     /_  __(_)____          / /_____  _____          / /_____  ___ 
      / / / / ___/ ______  / __/ __ `/ ___/ _____   / __/ __ \/ _ \
     / / / / /__  /_____/ / /_/ /_/ / /__  /_____/ / /_/ /_/ /  __/
    /_/ /_/\___/          \__/\__,_/\___/          \__/\____/\___/ 
    """
    print(title)


def print_introduction() -> None:
    introduction = """
Welcome to play Tic-tac-toe! Here's how to play:

1.  This game is played on a 3x3 board like this:

     1 | 2 | 3
    ----------- 
     4 | 5 | 6        
    -----------                                        
     7 | 8 | 9

    At first all of the squares are empty but the numbers here signify
    the numbers of the squares.
   
2.  Two players take turns, one as "X" and the other as "O". Player X goes
    first. On your turn, you can choose a square on the board to place your
    symbol in. That's done by entering the number of the square. You cannot
    choose a square that has already been taken.

3.  You win by placing three of your symbols in a row, column, or diagonal.

4.  A game can also end in a tie if all of the squares are taken but no one
    has won.
"""
    print(introduction)


def choose_opponent_prompt() -> int:
    print(
        "Do you want to play against:\n"
        "1) another player\n"
        "2) the computer"
    )
    while True:
        try:
            response = int(input().strip())
            if response in {1, 2}:
                return response
            else:
                raise ValueError
        except ValueError:
            print('Invalid response! Please answer with "1" or "2".')


def print_board(game: Game) -> None:
    print("Current board:\n")
    print(" " * 5 + " | ".join(game.board[:3]))
    print(" " * 4 + "-" * 11)
    print(" " * 5 + " | ".join(game.board[3:6]))
    print(" " * 4 + "-" * 11)
    print(" " * 5 + " | ".join(game.board[6:]) + '\n')


def handle_game_over(game: Game) -> None:
    if game.check_winner() is not None:
        game.game_over = True
        print(f"Player {game.other_player} won!\n")
    elif game.is_tie():
        game.game_over = True
        print("It's a tie!\n")


def move_prompt(game: Game) -> int:
    while True:
        try:
            square = int(input("Choose a square: "))
            if (0 < square < 10 and game.board[square - 1] == ' '):
                return square
            else:
                print("Invalid move! Square must exist and be empty.\n")
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.\n")


def player_turn(game: Game) -> None:
    print(f"\nPlayer {game.current_player}'s turn.\n")
    print_board(game)
    handle_game_over(game)
    chosen_square = move_prompt(game)
    game.play(chosen_square)
    game.switch_player()


def ai_turn(game: Game, ai: AI) -> None:
    print(f"\nPlayer {game.current_player}'s turn.\n")
    print_board(game)
    handle_game_over(game)
    chosen_square = ai.find_best_move(game)
    game.play(chosen_square)
    game.switch_player()


def play_again_prompt() -> bool:
    while True:
        try:
            response = input("Do you want to play again? (yes/no): ")
            match response.lower():
                case "y" | "yes":   return True
                case "n" | "no":   return False
                case _:     raise ValueError
        except ValueError:
            print('Invalid response! Please answer with "yes" or "no".\n')


if __name__ == "__main__":
    main()


from ai import AI
from board import Board


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.game_over = False
        self.current_player = 'O'

    def make_move(self, num_of_square: int) -> None:
        self.board.update_square(num_of_square, self.current_player)
        
    def print_board(self) -> None:
        row_1 = self.board[:3]
        row_2 = self.board[3:6]
        row_3 = self.board[6:]
        print("\nCurrent board:\n")
        print("    " + " | ".join(row_1))
        print("   " + "-" * 11)
        print("    " + " | ".join(row_2))
        print("   " + "-" * 11)
        print("    " + " | ".join(row_3))
        print("\n")
    
    def handle_game_over(self) -> None:
        if self.board.check_winner() is not None:
            self.game_over = True
            print(f"Player {self.current_player} won!\n")
        elif self.board.is_tie():
            self.game_over = True
            print("It's a tie!\n")
        
    def switch_player(self) -> None:
        self.current_player = 'X' if self.current_player == 'O' else 'O'
        
    def move_input(self) -> int:
        while True:
            try:
                square = int(input(f"Player {self.current_player}'s turn. "
                                   "Choose a square: "))
                if self.board.is_valid_square(square):
                    return square
                else:
                    print("Invalid move! Square must exist and be empty.\n")
            except ValueError:
                print("Invalid input! Please enter a number 1-9.\n")
    
    def player_turn(self) -> None:
        self.print_board()
        self.handle_game_over()
        self.switch_player()
        if not self.game_over:
            chosen_square = self.move_input()
            self.make_move(chosen_square)
    
    def computer_turn(self) -> None:
        self.print_board()
        self.handle_game_over()
        self.switch_player()
        if not self.game_over:
            ai = AI(self.current_player)
            chosen_square = ai.find_best_move_pruning(self.board)
            self.make_move(chosen_square)

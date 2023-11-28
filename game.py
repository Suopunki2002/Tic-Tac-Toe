
from board import Board


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player = 'O'
        self.game_over = False
    
    def make_move(self, n_of_square:int) -> None:
        self.board.update_square(n_of_square, self.player)
        
    def print_current_board(self) -> None:
        print("\n")
        self.board.print_board()
    
    def handle_game_over(self) -> None:
        if self.board.check_winner() is not None:
            self.game_over = True
            print(f"\nPlayer {self.player} won!\n")
        elif self.board.check_tie():
            self.game_over = True
            print(f"\nIt's a tie!\n")
        
    def switch_player(self) -> None:
        self.player = 'X' if self.player == 'O' else 'O'
        
    def player_input(self) -> int:
        while True:
            try:
                inp = int(input("Choose a square: "))
                if self.board.valid_square(inp):
                    return inp
                else:
                    print("Invalid move! Square must exist and be empty.")
            except ValueError:
                print("Invalid input! Please enter a number 1-9.")
                
    def new_turn(self) -> None:
        self.print_current_board()
        self.handle_game_over()
        if not self.game_over:
            self.switch_player()
            print(f"\nPlayer {self.player}'s turn. "
                "Write the number of the square you want to choose. "
                "The square must be empty and the number 1-9")
            chosen_square = self.player_input()
            self.make_move(chosen_square)

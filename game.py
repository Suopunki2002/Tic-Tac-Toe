
from board import Board


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player = 'O'
        self.game_over = False
        
    def make_move(self, position: int) -> None:
        self.board.update_position(position, self.player)
    
    def winner(self) -> str:
        return self.board.check_winner()

    def tie(self) -> bool:
        return self.board.is_full() and self.winner() is None
    
    def print_current_board(self) -> None:
        print("\n")
        self.board.print_board()
        
    def handle_game_over(self) -> None:
        if self.winner() is not None:
            self.game_over = True
            print(f"\nPlayer {self.player} wins!\n")
        elif self.tie():
            self.game_over = True
            print("\nIt's a tie!\n")
    
    def switch_player(self) -> None:
        self.player = 'X' if self.player == 'O' else 'O'
    
    def player_input(self) -> int:
        while True:
            try:
                move_pos = int(input("Number of the square: "))
                if self.board.is_valid_position(move_pos):
                    return move_pos
                else:
                    print("Invalid move! Square must exist and be empty.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
    def new_turn(self) -> None:
        self.print_current_board()
        self.handle_game_over()
        if not self.game_over:
            self.switch_player()
            print(f"\nPlayer {self.player}'s turn. "
                  "Write the number of the square you want to choose. "
                  "The square must be empty and the number between 1 and 9.")
            move_pos = self.player_input()
            self.make_move(move_pos)

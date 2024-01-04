
class Game:
    
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.other_player = 'O'
        self.game_over = False
    
    def empty_squares(self) -> list[int]:
        return [i + 1 for i, square in enumerate(self.board) if square == ' ']
    
    def is_valid_square(self, num_of_square: int) -> bool:
        if num_of_square < 1 or num_of_square > 9:
            return False
        return self.board[num_of_square - 1] == ' '

    def play_square(self, num_of_square: int) -> None:
        self.board[num_of_square - 1] = self.current_player
    
    def check_winner(self) -> str | None:
        winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for start, mid, end in winning_combinations:
            if self.board[start] == self.board[mid] == self.board[end] != ' ':
                return self.board[start]
        return None
    
    def is_tie(self) -> bool:
        return not self.empty_squares()
        
    def print_board(self) -> None:
        print("Current board:\n")
        print(" " * 5 + " | ".join(self.board[:3]))
        print(" " * 4 + "-" * 11)
        print(" " * 5 + " | ".join(self.board[3:6]))
        print(" " * 4 + "-" * 11)
        print(" " * 5 + " | ".join(self.board[6:]) + '\n')
    
    def handle_game_over(self) -> None:
        if self.check_winner() is not None:
            self.game_over = True
            print(f"Player {self.other_player} won!\n")
        elif self.is_tie():
            self.game_over = True
            print("It's a tie!\n")
        
    def switch_player(self) -> None:
        self.current_player, self.other_player = self.other_player, self.current_player
        
    def move_input(self) -> int:
        while True:
            try:
                square = int(input(f"Player {self.current_player}'s turn. "
                                   "Choose a square: "))
                if self.is_valid_square(square):
                    return square
                else:
                    print("Invalid move! Square must exist and be empty.\n")
            except ValueError:
                print("Invalid input! Please enter a number 1-9.\n")
    
    def player_turn(self) -> None:
        self.print_board()
        self.handle_game_over()
        if not self.game_over:
            chosen_square = self.move_input()
            self.play_square(chosen_square)
            self.switch_player()
    
    def computer_turn(self) -> None:
        self.print_board()
        self.handle_game_over()
        if not self.game_over:
            ai = AI(self.current_player)
            chosen_square = ai.find_best_move(self.board)
            self.play_square(chosen_square)
            self.switch_player()

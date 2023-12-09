
class Board:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
    
    def empty_squares(self) -> list[int]:
        return [i + 1 for i, square in enumerate(self.board) if square == ' ']
    
    def is_valid_square(self, num_of_square: int) -> bool:
        return num_of_square in self.empty_squares()
    
    def update_square(self, num_of_square: int, symbol: str) -> None:
        self.board[num_of_square - 1] = symbol
        
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
        row_1 = self.board[:3]
        row_2 = self.board[3:6]
        row_3 = self.board[6:]
        print("    " + " | ".join(row_1))
        print("   " + "-" * 11)
        print("    " + " | ".join(row_2))
        print("   " + "-" * 11)
        print("    " + " | ".join(row_3))
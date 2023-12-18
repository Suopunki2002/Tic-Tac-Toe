
class Board:
    
    def __init__(self) -> None:
        self.board: list[str] = [' ' for _ in range(9)]
    
    def empty_squares(self) -> list[int]:
        return [i + 1 for i, square in enumerate(self.board) if square == ' ']
    
    def is_valid_square(self, num_of_square: int) -> bool:
        if num_of_square < 1 or num_of_square > 9:
            return False
        return self.board[num_of_square - 1] == ' '
    
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

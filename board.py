class Board:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.empty_squares = [i for i in range(1, 10)]
    
    def valid_square(self, n_of_square: int) -> bool:
        return n_of_square in self.empty_squares
    
    def update_square(self, n_of_square: int, symbol: str) -> None:
        self.board[n_of_square-1] = symbol
        self.empty_squares.remove(n_of_square)
        
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
        
    def check_tie(self) -> bool:
        return not self.empty_squares
    
    def print_board(self) -> None:
        # Change empty squares to the number of the square
        current_board = [
            str(i) if i in self.empty_squares
            else self.board[i-1]
            for i in range(1, 10)
            ]
        print(" | ".join(current_board[:3]))
        print("-" * 9)
        print(" | ".join(current_board[3:6]))
        print("-" * 9)
        print(" | ".join(current_board[6:]))
        
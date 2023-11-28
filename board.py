
class Board:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.empty_squares = [i for i in range(1, 10)]
    
    def valid_square(self, number: int) -> bool:
        return number in self.empty_squares
    
    def update_square(self, number: int, symbol: str) -> None:
        self.board[number-1] = symbol
        self.empty_squares.remove(number)
        
    def check_winner(self) -> str | None:
        # Check rows and columns
        for i in range(3):
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != ' ':
                return self.board[i*3]
            elif self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return self.board[i]
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] != ' ':
            return self.board[2]
        
    def check_tie(self) -> bool:
        return not self.empty_squares
    
    def print_board(self) -> None:
        current_board = []
        # Change to the number of the square if the square is empty
        for i, square in enumerate(self.board):
            match square:
                case ' ':
                    current_board += str(i+1)
                case _:
                    current_board += square
        print(" | ".join(current_board[:3]))
        print("-" * 9)
        print(" | ".join(current_board[3:6]))
        print("-" * 9)
        print(" | ".join(current_board[6:]))
        
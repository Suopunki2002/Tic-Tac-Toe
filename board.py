
class Board:
    def __init__(self) -> None:
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.all_coordinates = [(r, c) for r in range(3) for c in range(3)]
        self.empty_coordinates = self.all_coordinates
    
    def valid_square(self, coordinates: (int, int)) -> bool:
        if coordinates not in self.all_coordinates:
            return False
        return coordinates in self.empty_coordinates
    
    def update_square(self, coordinates: (int, int), symbol: str) -> None:
        row, col = coordinates
        self.board[row][col] = symbol
        self.empty_coordinates.remove(coordinates)
        
    def is_full(self) -> bool:
        return not self.empty_coordinates
        
    def check_winner(self) -> str:
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            # Check columns
            elif self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
    
    def check_tie(self) -> bool:
        return self.is_full() and self.check_winner() is None
    

class Board:
    def __init__(self) -> None:
        self.board = [[' ' for i in range(3)] for j in range(3)]
    
    def is_valid_move(self, row: int, col: int) -> bool:
        if (self.board[row][col] == ' '):
            return True
        else:
            return False
        
    def check_winner(self) -> str:
        for i in range(3):
            # Check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            # Check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None
    
    def is_full(self) -> bool:
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    
    def print_board(self) -> None:
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

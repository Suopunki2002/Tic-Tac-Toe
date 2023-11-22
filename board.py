
class Board:
    def __init__(self) -> None:
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.pos_to_coord = {
            1: (0, 0),
            2: (0, 1),
            3: (0, 2),
            4: (1, 0),
            5: (1, 1),
            6: (1, 2),
            7: (2, 0),
            8: (2, 1),
            9: (2, 2)
        }
        self.coord_to_pos = {
            (0, 0): 1,
            (0, 1): 2,
            (0, 2): 3,            
            (1, 0): 4,
            (1, 1): 5,
            (1, 2): 6,            
            (2, 0): 7,
            (2, 1): 8,
            (2, 2): 9
        }
    
    def is_valid_position(self, position: int) -> bool:
        is_valid_position = position in [1, 2, 3, 4, 5, 6, 7, 8, 9]
        coords = self.pos_to_coord[position]
        row = coords[0]; col = coords[1]
        if is_valid_position and self.board[row][col] == ' ':
            return True
        else:
            return False
        
    def update_position(self, position: int, symbol: str) -> None:
        coords = self.pos_to_coord[position]
        row = coords[0]; col = coords[1]
        self.board[row][col] = symbol
        
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
        for i in range(3):
            row = self.board[i]
            printable = []
            for j in range(3):
                x = row[j]
                if x == ' ':
                    printable += str(self.coord_to_pos[(i, j)])
                else:
                    printable += x 
            print(" | ".join(printable))
            if i != 2:
                print("-" * 9)

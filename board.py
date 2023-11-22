
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
        self.coord_to_pos = {v: k for k, v in self.pos_to_coord.items()}
    
    def is_valid_position(self, position: int) -> bool:
        if position not in self.pos_to_coord:
            return False
        row, col = self.pos_to_coord[position]
        return self.board[row][col] == ' '
        
    def update_position(self, position: int, symbol: str) -> None:
        row, col = self.pos_to_coord[position]
        self.board[row][col] = symbol
        
    def check_winner(self) -> str:
        for i in range(3):
            # Check rows and columns
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' \
            or self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' \
        or self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None
    
    def is_full(self) -> bool:
        return all(cell != ' ' for row in self.board for cell in row)
    
    def print_board(self) -> None:
        for i, row in enumerate(self.board):
            printable = []
            for j, cell in enumerate(row):
                if cell == ' ':
                    printable += str(self.coord_to_pos[(i, j)])
                else:
                    printable += cell
            print(" | ".join(printable))
            if i != 2:
                print("-" * 9)
        
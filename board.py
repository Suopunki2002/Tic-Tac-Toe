
class Board:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.empty_cells = [i for i in range(1, 10)]
    
    def valid_cell(self, number: int) -> bool:
        return number in self.empty_cells
    
    def update_cell(self, number: int, symbol: str) -> None:
        self.board[number-1] = symbol
        self.empty_cells -= number
        
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
        return not self.empty_cells
    
    def print_board(self) -> None:
        cur_board_with_nums = []
        for i, cell in enumerate(self.board):
            match cell:
                case ' ':
                    cur_board_with_nums += str(i+1)
                case _:
                    cur_board_with_nums += cell
        print(" | ".join(cur_board_with_nums[:3]))
        print("-" * 9)
        print(" | ".join(cur_board_with_nums[3:6]))
        print("-" * 9)
        print(" | ".join(cur_board_with_nums[6:]))
        
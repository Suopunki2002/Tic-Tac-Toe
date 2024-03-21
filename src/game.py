
class Game:
    
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)]
        self.game_over = False
        self.current_player = 'X'
        self.other_player = 'O'

    def play(self, num_of_square: int) -> None:
        self.board[num_of_square - 1] = self.current_player

    def switch_player(self) -> None:
        temp = self.current_player
        self.current_player = self.other_player
        self.other_player = temp
    
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
    
    def empty_squares(self) -> list[int]:
        return [i for i, square in enumerate(self.board) if square == ' ']

    def is_tie(self) -> bool:
        return not self.empty_squares()


from copy import deepcopy
from math import inf
from random import randrange

from board import Board


class AI:
    def __init__(self, player_symbol: str) -> None:
        self.player = player_symbol
        self.opponent = "X" if player_symbol == 'O' else 'O'

    def minimax(self, board: Board, is_maximizing: bool) -> int:
        possible_winner = board.check_winner()
        if possible_winner is not None:
            return -1 if possible_winner == self.player else 1
        elif board.is_tie():
            return 0
        
        if is_maximizing:
            max_eval = -inf
            for position in board.empty_squares:
                child = deepcopy(board).update_square(position, self.player)
                eval = self.minimax(child, False)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = inf
            for position in board.empty_squares:
                child = deepcopy(board)
                child.update_square(position, self.opponent)
                eval = self.minimax(child, True)
                min_eval = min(min_eval, eval)
            return min_eval
    
    def random_move(self, board: Board):
        rand = 10
        while rand not in board.empty_squares:
            rand = randrange(1, 10)
        return rand
                
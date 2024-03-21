
from math import inf

from game import Game


class AI:
    
    def __init__(self, symbol: str) -> None:
        self.ai = symbol
        self.human = "X" if symbol == 'O' else 'O'

    def minimax(self, game: Game, depth: int, alpha: int, beta: int,
                is_maximizing: bool) -> int:
        possible_winner = game.check_winner()
        if possible_winner == self.ai:
            return 10 - depth
        elif possible_winner == self.human:
            return depth - 10
        elif game.is_tie():
            return 0
        
        if is_maximizing:
            max_eval = -inf
            possible_positions = game.empty_squares()
            for position in possible_positions:
                game.board[position] = self.ai
                eval = self.minimax(game, depth + 1, alpha, beta, False)
                game.board[position] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = inf
            possible_positions = game.empty_squares()
            for position in possible_positions:
                game.board[position] = self.human
                eval = self.minimax(game, depth + 1, alpha, beta, True)
                game.board[position] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
    
    def find_best_move(self, game: Game) -> int:
        best_score = -inf
        best_move = -1
        for move in game.empty_squares():
            game.board[move] = self.ai
            score = self.minimax(game, 0, -inf, inf, False)
            game.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move + 1

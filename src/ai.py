
from math import inf

from src.board import Board


class AI:
    
    def __init__(self, ai_symbol: str) -> None:
        self.ai = ai_symbol
        self.human = "X" if ai_symbol == 'O' else 'O'
        
    def minimax(self, board: Board, depth: int, is_maximizing: bool) -> int:
        possible_winner = board.check_winner()
        if possible_winner == self.ai:
            return 10 - depth
        elif possible_winner == self.human:
            return depth - 10
        elif board.is_tie():
            return 0
        
        if is_maximizing:
            max_eval = -inf
            for square in board.empty_squares():
                board.update_square(square, self.ai)
                eval = self.minimax(board, depth + 1, False)
                max_eval = max(max_eval, eval)
                board.update_square(square, ' ') 
            return max_eval
        else:
            min_eval = inf
            for square in board.empty_squares():
                board.update_square(square, self.human)
                eval = self.minimax(board, depth + 1, True)
                min_eval = min(min_eval, eval)
                board.update_square(square, ' ')
            return min_eval

    def minimax_pruning(self, board: Board, depth: int, alpha: int, beta: int,
                        is_maximizing: bool) -> int:
        possible_winner = board.check_winner()
        if possible_winner == self.ai:
            return 10 - depth
        elif possible_winner == self.human:
            return depth - 10
        elif board.is_tie():
            return 0
        
        if is_maximizing:
            max_eval = -inf
            for square in board.empty_squares():
                board.update_square(square, self.ai)
                eval = self.minimax_pruning(
                    board, depth + 1, alpha, beta, False)
                board.update_square(square, ' ')
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = inf
            for square in board.empty_squares():
                board.update_square(square, self.human)
                eval = self.minimax_pruning(
                    board, depth + 1, alpha, beta, True)
                board.update_square(square, ' ')
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
    
    def find_best_move(self, board: Board) -> int:
        best_score = -inf
        best_move = -1
        for move in board.empty_squares():
            board.update_square(move, self.ai)
            score = self.minimax(board, 0, False)
            board.update_square(move, ' ')
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
    
    def find_best_move_pruning(self, board: Board) -> int:
        best_score = -inf
        best_move = -1
        for move in board.empty_squares():
            board.update_square(move, self.ai)
            score = self.minimax_pruning(board, 0, -inf, inf, False)
            board.update_square(move, ' ')
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

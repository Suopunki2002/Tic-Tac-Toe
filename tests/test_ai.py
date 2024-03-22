
from time import perf_counter
from random import randrange
import unittest

from src.ai import AI
from src.game import Game


class TestAIMethods(unittest.TestCase):
    
    def test_minimax_correctness(self):
        ai = AI('X')
        game = Game()
        game.board = [
            'X', ' ', ' ',
            'X', 'O', ' ',
            'O', ' ', ' '
        ]
        self.assertEqual(ai.find_best_move(game), 3)
        
    def test_performance(self):
        # Test if the best move can consistantly be found
        # in under a  tenth of a second
        ai = AI('O')
        for _ in range(10):
            game = Game()
            three_random_moves = [randrange(1, 10) for _ in range(3)]
            for i in range(3):
                symbol = 'O' if i == 1 else 'X'
                game.board[three_random_moves[i] - 1] = symbol
                
            start_time = perf_counter()
            ai.find_best_move(game)
            end_time = perf_counter()
            time = end_time - start_time
            
            self.assertLess(time, 0.1)

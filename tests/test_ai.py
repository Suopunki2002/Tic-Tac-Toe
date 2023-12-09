
from time import perf_counter
from random import randrange
import unittest

from src.ai import AI
from src.board import Board


class TestAIMethods(unittest.TestCase):
    
    def test_minimax_correctness(self):
        ai = AI('X')
        test_board = Board()
        test_board.board = ['X', ' ', ' ',
                            'X', 'O', ' ',
                            'O', ' ', ' ']
        self.assertEqual(ai.find_best_move(test_board), 3)
        self.assertEqual(ai.find_best_move_pruning(test_board), 3)
        
    def test_performance_gain_from_pruning(self):
        ai = AI('O')
        for _ in range(10):
            test_board = Board()
            three_random_moves = [randrange(1, 10) for _ in range(3)]
            for i in range(3):
                symbol = 'O' if i == 1 else 'X'
                test_board.update_square(three_random_moves[i], symbol)
                
            no_pruning_start_t = perf_counter()
            ai.find_best_move(test_board)
            no_pruning_end_t = perf_counter()
            no_pruning_time = no_pruning_end_t - no_pruning_start_t
            
            pruning_start_t = perf_counter()
            ai.find_best_move_pruning(test_board)
            pruning_end_t = perf_counter()
            pruning_time = pruning_end_t - pruning_start_t
            
            self.assertLessEqual(pruning_time, no_pruning_time)
            
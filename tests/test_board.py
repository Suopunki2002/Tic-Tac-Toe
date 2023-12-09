
import unittest

from src.board import Board


class TestBoardMethods(unittest.TestCase):
    
    def test_empty_squares(self):
        test_board_1 = Board()
        test_board_1.board = ['X', 'O', 'X',
                              'X', 'O', ' ',
                              'O', ' ', ' ']
        test_board_2 = Board()
        test_board_2.board = ['O', ' ', 'X',
                              'X', 'X', 'O',
                              'O', ' ', ' ']
        test_list_1 = test_board_1.empty_squares()
        test_list_2 = test_board_2.empty_squares()
        self.assertEqual(test_list_1, [6, 8, 9])
        self.assertEqual(test_list_2, [2, 8, 9])
        
    def test_is_valid_square(self):
        test_board = Board()
        test_board.board = ['X', 'O', 'X',
                            'X', 'O', ' ',
                            'O', ' ', ' ']
        self.assertFalse(test_board.is_valid_square(1))
        self.assertTrue(test_board.is_valid_square(6))
        
    def test_update_square(self):
        test_board = Board()
        test_board.update_square(1, 'X')
        self.assertEqual(test_board.board[0], 'X')
        self.assertEqual(test_board.board[1], ' ')
        
    def test_check_winner(self):
        test_board = Board()
        test_board.board = ['X', ' ', ' ',
                            ' ', 'X', 'O',
                            'O', 'X', 'O']
        self.assertIsNone(test_board.check_winner())
        test_board.update_square(2, 'X')
        self.assertEqual(test_board.check_winner(), 'X')
    
    def test_is_tie(self):
        test_board = Board()
        test_board.board = ['X', 'O', 'X',
                            'X', 'O', 'O',
                            'O', 'X', ' ']
        self.assertFalse(test_board.is_tie())
        test_board.update_square(9, 'X')
        self.assertTrue(test_board.is_tie())
    
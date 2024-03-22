import unittest

from src.game import Game


class TestBoardMethods(unittest.TestCase):
    
    def test_play(self):
        game = Game()
        game.play(1)
        self.assertEqual(game.board[0], 'X')

    def test_check_winner(self):
        game = Game()
        moves = [1, 5, 4, 7, 2]
        for i, move in enumerate(moves):
            symbol = 'X' if (i % 2 == 0) else 'O'
            game.board[move - 1] = symbol
        self.assertIsNone(game.check_winner())
        
        game.board[2] = 'O'
        self.assertEqual(game.check_winner(), 'O')

    def test_empty_squares(self):
        game_1 = Game()
        game_1.board = [
            'X', 'O', 'X',
            'X', 'O', ' ',
            'O', ' ', ' '
        ]
        result_1 = game_1.empty_squares()
        self.assertEqual(result_1, [5, 7, 8])

        game_2 = Game()
        game_2.board = [
            'O', ' ', 'X',
            'X', 'X', 'O',
            'O', ' ', ' '
        ]
        result_2 = game_2.empty_squares()
        self.assertEqual(result_2, [1, 7, 8])
            
    def test_is_tie(self):
        game = Game()
        game.board = [
            'X', 'O', 'X',
            'X', 'O', 'O',
            'O', 'X', ' '
        ]
        self.assertFalse(game.is_tie())
        game.board[8] = 'X'
        self.assertTrue(game.is_tie())
    
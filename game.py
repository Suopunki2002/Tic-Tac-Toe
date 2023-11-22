
from board import Board


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player = 'O'
        self.game_over = False
        
    def make_move(self, position: int) -> None:
        self.board.update_position(position, self.player)
    
    def winner(self) -> str:
        return self.board.check_winner()

    def tie(self) -> bool:
        if self.board.is_full() and self.winner() == None:
            return True
        else:
            return False
        
    def new_turn(self) -> None:
        # Print current board
        print("\n")
        self.board.print_board()
        # Return if game over
        if self.winner() != None:
            self.game_over = True
            print(f"\nPlayer {self.player} wins!\n")
            return
        elif self.tie():
            self.game_over = True
            print("\nIt's a tie!\n")
            return
        # Change player
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
        # Player input for a move
        print("\n")
        instructions_1 = f"Player {self.player}'s turn. "
        instructions_2 = "Write the number of the square you want to choose. "
        instructions_3 = "The square must be empty and the number between 1 and 9."
        print(instructions_1 + instructions_2 + instructions_3)
        move_pos = int(input("Number of the square: "))
        # Ask for new input if move is invalid
        while not self.board.is_valid_position(move_pos):
            print("\nInvalid move! Square must exist and be empty.\n")
            new_pos = int(input("Number of the square: "))
            move_pos = new_pos
        # Make move if valid
        self.make_move(move_pos)

        """
        def new_turn(self) -> None:
        # Change player
        previous_player = self.current_player
        if previous_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        print("\n")
        self.board.print_board()
        # Return if game over
        if self.winner() != None:
            self.game_over = True
            print(f"\nPlayer {previous_player} wins!\n")
            return
        elif self.tie():
            self.game_over = True
            print("\nIt's a tie!\n")
            return
        # Player input for a move
        print("\n")
        instructions_1 = f"Player {self.current_player}'s turn. "
        instructions_2 = "Write the number of the square you want to choose. "
        instructions_3 = "The square must be empty and the number between 1 and 9."
        print(instructions_1 + instructions_2 + instructions_3)
        move_pos = int(input("Number of the square: "))
        # Ask for new input if move is invalid
        while not self.board.is_valid_position(move_pos):
            print("\nInvalid move! Square must exist and be empty.\n")
            new_pos = int(input("Number of the square: "))
            move_pos = new_pos
        # Make move when valid
        self.make_move(move_pos)
        """
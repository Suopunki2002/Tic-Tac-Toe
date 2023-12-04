
from game import Game


def main():
    play_again = True
    while play_again:
        # Initialize a new game
        game = Game()
        while not game.game_over:
            game.new_turn()
        response = play_again_prompt()
        play_again = response == "yes"
            
def play_again_prompt() -> str:
    while True:
        try:
            response = input("Do you want to play again? (yes/no): ").strip().lower()
            if response in {"yes", "no"}:
                return response
            else:
                raise ValueError
        except ValueError:
            print("Invalid response. Please answer with 'yes' or 'no'.")

if __name__ == "__main__":
    main()

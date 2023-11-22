
from game import Game


def main():
    play_again = True
    while play_again:
        # Initialize a new game
        game = Game()
        while not game.game_over:
            game.new_turn()
        # Ask if the player wants to play again
        play_again_prompt = "Do you want to play again? (y/n): "
        response = input(play_again_prompt).lower() # Case insensitive
        # positive = response == "y" or response == "yes"
        # negative = response == "n" or response == "no"
        while interpet_response(response) == None:
            print("\nInvalid response. Answer either y/Y/yes/Yes/YES or n/N/no/No/NO.\n")
            new_response = input(play_again_prompt).lower()
            response = new_response
        if interpet_response(response) == False:
            play_again = False
            
            
def interpet_response(response: str) -> bool:
    r = response.lower()
    if r == "y" or r == "yes":
        return True
    elif r == "n" or r == "no":
        return False
    else:   # Invalid response
        return None


if __name__ == "__main__":
    main()


# Tic-tac-toe
Tic-tac-toe CLI game written in Python. You can either play against another
player or a simple AI based on the [Minimax](https://en.wikipedia.org/wiki/Minimax)-algorithm.

## Playing the game
You can play the game by running the main.py file. If you have opened the root
directory of the project, you can run the game with the following commands:

- On Windows:
    ```py src\main.py```

- On Linux & Mac:
    ```python3 src/main.py```

The game itself will give the rest of the instructions needed to play the game.

## Tests
If you want to see and run the tests in in the tests directory, you should be
aware that there is a small bug where you will have to change the
"from game import Game" line in ai.py to "from src.game import Game".
This will allow the tests but will prevent you from running the game.
Once you have changed the line, you can run the tests with the commands:

- On Windows:
    ```py -m unittest discover -s tests```

- On Linux & Mac:
    ```python3 -m unittest discover -s tests```


from abc import ABC, abstractmethod
import random
import numpy as np
# from enum import Enum
# from pydantic import BaseModel, validator, ValidationError

class ConnectFour():
    def __init__(self, player_1, player_2) -> None:
        self._rows = 6
        self._columns = 7
        self._players = [player_1, player_2]
        self._grid = np.full((self.rows, self.columns), ' ')

        self.check_different_counters()

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def players(self):
        return self._players
    
    @property
    def grid(self):
        return self._grid
    
    def check_different_counters(self):
        """Validator to ensure that both players have different counters."""
        counters = {player.counter for player in self._players}
        if len(counters) != len(self._players):
            raise ValueError('Players must have different counters.')

    def show_grid(self):
        """
        display the board?
        """
        print("\n  " + "   ".join(str(i) for i in range(self.columns)))
        for row in self._grid:
            print("| " + " | ".join(row) + " |")

        
    def drop_counter(self, column, counter):
        """
        drop counter in col
        """
        pass

    def check_for_end(self):
        """"
        check if win or stalemate
        """
        pass

    def play(self):
        """
        play the game
        """

        while True:
            # display grid each time
            self.show_grid()
            break

class Player(ABC):
    def __init__(self, counter):
        self.counter = counter

    @abstractmethod
    def move(self):
        """
        Method to move. Must be implemented in subclasses."""
        pass

class HumanPlayer(Player):
    """
    human player needs to input
    """
    def move(self):
        while True:
            try:
                column = int(input("Enter the column (0-6) to drop your counter: "))
                return column
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 6.")

class ComputerPlayer(Player):
    """
    define a computer player; makes random moves
    """
    def move(self):
        return random.randint(0, 6)

# class Counter(str, Enum):
#     """Enumeration for valid counters in the game."""
#     X = 'X'
#     O = 'O'


if __name__ == "__main__":
    # Initialize the game
    game = ConnectFour(player_1=HumanPlayer('x'), player_2=ComputerPlayer('o'))
    # Start the game
    game.play()

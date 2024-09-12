import random
from abc import ABC, abstractmethod

import numpy as np

# from enum import Enum
# from pydantic import BaseModel, validator, ValidationError

# # Configure the logger
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


class ConnectFour:
    def __init__(self, player_1, player_2) -> None:
        self._rows = 6
        self._columns = 7
        self._players = [player_1, player_2]
        self._grid = np.full(
            (self.rows, self.columns), " "
        )  # return a filled grid with blank spaces

        # some basic validation
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

    # ensure that each player has a different counter
    # -- probably a better way with ENUM and pydantic
    def check_different_counters(self):
        """Validator to ensure that both players have different counters."""
        counters = {player.counter for player in self._players}
        if len(counters) != len(self._players):
            raise ValueError("Players must have different counters.")

    def show_grid(self):
        """
        display the board
        """
        print("\n  " + "   ".join(str(i) for i in range(self.columns)))
        for row in self._grid:
            print("| " + " | ".join(row) + " |")

    def drop_counter(self, column, counter):
        """
        drop counter in col
        """
        if column < 0 or column >= self.columns:
            # raise ValueError("Invalid column. Choose between 0 and 6.")
            print("Invalid column. Choose between 0 and 6.")
            return False

        for row in reversed(self.grid):  # Start checking from the bottom row
            if row[column] == " ":
                row[column] = counter
                return True

        print("Column is full. Choose another column.")
        return False

    def check_for_end(self, counter):
        """
        check if win or stalemate
        """

        # !TODO stalemate is when board is full
        # !TODO is there an algo that's optimised for the diagonal?

        # Check horizontal win
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if np.all(self._grid[row, col : col + 4] == counter):
                    return True

        # Check vertical win
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if np.all(self._grid[row : row + 4, col] == counter):
                    return True
        pass

    def play(self):
        """
        play the game
        """
        current_player_index = 0
        self.show_grid()  # show grid at beginning

        # oaky, so we want to iterate through turns until the game ends
        # so leave true, then for each turn, keep going until the move is valid
        # and then break the while loop when the game ends
        while True:
            current_player = self.players[current_player_index]
            # logger.info(f"Player {player_index}")
            print("\n\n-----------------------------------------")
            print(f"Current Player: Player {current_player_index}")

            valid_turn = False
            while not valid_turn:
                valid_turn = self.drop_counter(
                    current_player.move(),
                    current_player.counter,
                )

            # check for end (win/stalemate)
            if self.check_for_end(current_player.counter):
                self.show_grid()
                print(f"🎉 Player {current_player_index} Wins!")
                break

            # !TODO implement stalemate

            self.show_grid()

            current_player_index = 1 - current_player_index  # assumes two players


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
    game = ConnectFour(player_1=HumanPlayer("x"), player_2=ComputerPlayer("o"))
    # Start the game
    game.play()

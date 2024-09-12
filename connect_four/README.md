Programming Task

You have 1 hour to implement a solution to the following problem. At the start of the interview, we would like you to explain how you approached the problem, including any design and implementation decisions made; talk us through the code you have written; and demonstrate how the program runs. The preferred language is Python, but you can use another language of your choice, if you are unfamiliar with Python.

Problem Specification: Connect 4

Connect 4 (https://en.wikipedia.org/wiki/Connect_Four) is a two-player game. The players take turns dropping a counter into a 6x7 grid, where they occupy the lowest available space within the chosen column. The objective of the game is to be the first to form a horizontal, vertical or diagonal line of four with your own counters.

We would like you to write a program, which can be run from the terminal, that simulates a game of Connect 4. A user should be able to play against the computer, the latter of which randomly selects a column for its counter. We do not expect you to check for diagonal lines, only horizontal and vertical lines. The program should also satisfy the requirements below.

Requirements:
- Asks the user for input, specifically the column for their counter.
- Checks the validity of the user input.
- Displays the grid each time a counter is played.
- Checks for stalemate (i.e. the grid is full of counters and there is no winner).

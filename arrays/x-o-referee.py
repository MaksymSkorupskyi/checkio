"""Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O)
who take turns marking the spaces in a 3×3 grid.
The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows
(NW-SE and NE-SW) wins the game.

But we will not be playing this game.
You will be the referee for this games results.
You are given a result of a game and you must determine if the game ends in a win
or a draw as well as who will be the winner.
Make sure to return "X" if the X-player wins and "O" if the O-player wins.
If the game is a draw, return "D".

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).
Output: "X", "O" or "D" as a string.
Example:

checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"

How it is used: The concepts in this task will help you when iterating data types.
They can also be used in game algorithms, allowing you to know how to check results.

Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
"""

from typing import List


# v1 - lazy and pretty straightforward ))
def checkio(game_result: List[str]) -> str:
    """
    Return "X" if the X-player wins and "O" if the O-player wins.
    If the game is a draw, return "D".
    """
    # row check
    for row in game_result:
        if row == "XXX":
            return "X"
        if row == "OOO":
            return "O"
    # column check
    if game_result[0][0] != '.' and game_result[0][0] == game_result[1][0] == game_result[2][0]:
        return game_result[0][0]
    if game_result[0][1] != '.' and game_result[0][1] == game_result[1][1] == game_result[2][1]:
        return game_result[0][1]
    if game_result[0][2] != '.' and game_result[0][2] == game_result[1][2] == game_result[2][2]:
        return game_result[0][2]
    # diagonal check
    if game_result[0][0] != '.' and game_result[0][0] == game_result[1][1] == game_result[2][2]:
        return game_result[1][1]
    # anti-diagonal check
    if game_result[0][2] != '.' and game_result[0][2] == game_result[1][1] == game_result[2][0]:
        return game_result[1][1]
    return "D"


# v2 - lazy, a little bit optimized ))
def checkio(game_result: List[str]) -> str:
    """
    Return "X" if the X-player wins and "O" if the O-player wins.
    If the game is a draw, return "D".
    """
    # row check
    if "XXX" in game_result:
        return "X"
    if "OOO" in game_result:
        return "O"
    # column check
    if game_result[0][0] == game_result[1][0] == game_result[2][0] != '.':
        return game_result[0][0]
    if game_result[0][1] == game_result[1][1] == game_result[2][1] != '.':
        return game_result[0][1]
    if game_result[0][2] == game_result[1][2] == game_result[2][2] != '.':
        return game_result[0][2]
    # diagonal check
    if game_result[0][0] == game_result[1][1] == game_result[2][2] != '.':
        return game_result[1][1]
    # anti-diagonal check
    if game_result[0][2] == game_result[1][1] == game_result[2][0] != '.':
        return game_result[1][1]
    return "D"


# v3 - matrix transpose for columns check
def checkio(game_result: List[str]) -> str:
    """
    Return "X" if the X-player wins and "O" if the O-player wins.
    If the game is a draw, return "D".
    """
    # row check
    if 'XXX' in game_result:
        return "X"
    if 'OOO' in game_result:
        return 'O'
    # column check
    if ('X', 'X', 'X') in zip(*game_result):
        return 'X'
    if ('O', 'O', 'O') in zip(*game_result):
        return 'O'
    # diagonal check
    if game_result[0][0] == game_result[1][1] == game_result[2][2] != '.':
        return game_result[1][1]
    # anti-diagonal check
    if game_result[0][2] == game_result[1][1] == game_result[2][0] != '.':
        return game_result[1][1]
    return 'D'


# v4 - str + zip
def checkio(game_result: List[str]) -> str:
    """
    Return "X" if the X-player wins and "O" if the O-player wins.
    If the game is a draw, return "D".
    """
    columns = list(map(''.join, zip(*game_result)))
    diagonals = list(map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(game_result)])))
    lines = game_result + columns + diagonals
    if 'XXX' in lines:
        return 'X'
    if 'OOO' in lines:
        return 'O'
    return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio(["OOO", "XX.", ".XX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([".OX", ".XX", ".OO"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

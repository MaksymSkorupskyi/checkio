"""A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
With this strategy, one pawn defends the others.
A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer.

Example:
safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

Precondition:
0 < pawns ≤ 8
"""


def safe_pawns(pawns: set) -> int:
    """ Get the number of safe pawns """
    safe_count = 0
    for pawn in pawns:
        # for "b4" left_defender is "a3" and right_defender is "c3"
        left_defender = f'{chr(ord(pawn[:1]) - 1)}{int(pawn[1:]) - 1}'
        right_defender = f'{chr(ord(pawn[:1]) + 1)}{int(pawn[1:]) - 1}'
        if left_defender in pawns or right_defender in pawns:
            safe_count += 1
    return safe_count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"a1", "a8", "b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns({"a4", "b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

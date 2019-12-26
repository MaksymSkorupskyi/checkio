""" Golden Pyramid
Our Robo-Trio need to train for future journeys and treasure hunts.
Stephan has built a special flat model of a pyramid.
Now the robots can train for speed gold running.
They start at the top of the pyramid and must collect gold in each room,
choose to take the left or right path and continue down to the next level.
To optimise their gold runs, Stephan need to know the maximum amount of gold that can be collected in one run.

Consider a tuple of tuples in which the first tuple has one integer
and each consecutive tuple has one more integer then the last.
Such a tuple of tuples would look like a triangle.
You should write a program that will help Stephan find the highest possible sum
on the most profitable route down the pyramid.
All routes down the pyramid involve stepping down and to the left or down and to the right.

Tips:
Think of each step down to the left as moving to the same index location or to the right as one index location higher.
Be very careful if you plan to use recursion here.

Input: A pyramid as a tuple of tuples. Each tuple contains integers.
Output: The maximum possible sum as an integer.

How it is used: This is a classical problem which shows you how to use dynamic programming.
This concept is a core component of many optimisation tasks.

Precondition: 0 < len(pyramid) ≤ 20
all(all(0 < x < 10 for x in row) for row in pyramid)
"""
from typing import Tuple


# v1 - build a pyramid of max possible sums in a path from top to bottom
def count_gold(pyramid: Tuple[Tuple[int, ...], ...]) -> int:
    """
    Return max possible sum in a path from top to bottom
    """
    pyramid = [list(row) for row in pyramid]
    # build a pyramid of max possible sums in a path from top to bottom
    for i, row in enumerate(pyramid[1:], start=1):
        pyramid[i][0] += pyramid[i - 1][0]
        pyramid[i][-1] += pyramid[i - 1][-1]
        for j, element in enumerate(row[1:-1], start=1):
            pyramid[i][j] = max(pyramid[i][j] + pyramid[i - 1][j - 1], pyramid[i][j] + pyramid[i - 1][j])
    return max(pyramid[-1])


# v2 - build a pyramid of max possible sums in a path from bottom to top
def count_gold(pyramid: Tuple[Tuple[int, ...], ...]) -> int:
    """
    Return max possible sum in a path from top to bottom
    """
    pyramid = [list(row) for row in pyramid]
    # build a pyramid of max possible sums in a path from bottom to top
    for i in range(len(pyramid) - 2, -1, -1):
        for j in range(i + 1):
            pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])
    return pyramid[0][0]


# v3 - build a pyramid of max possible sums in a path from bottom to top
def count_gold(pyramid: Tuple[Tuple[int, ...], ...]) -> int:
    """
    Return max possible sum in a path from top to bottom
    """
    pyramid = list(pyramid)
    for i in range(len(pyramid) - 2, -1, -1):
        pyramid[i] = [pyramid[i][j] + max(pyramid[i + 1][j], pyramid[i + 1][j + 1]) for j in range(len(pyramid[i]))]
    return pyramid[0][0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold(((1,),
                       (2, 3),
                       (3, 3, 1),
                       (3, 1, 5, 4),
                       (3, 1, 3, 1, 3),
                       (2, 2, 2, 2, 2, 2),
                       (5, 6, 4, 5, 6, 4, 3))) == 23, "First example"
    assert count_gold(((1,),
                       (2, 1),
                       (1, 2, 1),
                       (1, 2, 1, 1),
                       (1, 2, 1, 1, 1),
                       (1, 2, 1, 1, 1, 1),
                       (1, 2, 1, 1, 1, 1, 9))) == 15, "Second example"
    assert count_gold(((9,),
                       (2, 2),
                       (3, 3, 3),
                       (4, 4, 4, 4))) == 18, "Third example"

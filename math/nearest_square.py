"""The Nearest Square Number
You have some number and you are trying to find the nearest square number (a perfect square).
Square number is the number the square root of which is an integer.
For example, if we start with the number 8, then the two nearby square numbers are 4 (sqrt(4) == 2) and 9 (sqrt(9) == 3)
So the answer is 9, because 9 is the nearest.

Input: A number.
Output: The nearest square number.

Example:
nearest_square(8) == 9
nearest_square(13) == 16
nearest_square(24) == 25
nearest_square(9876) == 9801

How it is used: For mathematical analysis.

Precondition:
0 < number <= 1000000"""


def nearest_square(number: int) -> int:
    """ find the nearest square number (a perfect square) """
    return round(number ** 0.5) ** 2


if __name__ == '__main__':
    print("Example:")
    print(nearest_square(8))
    print(nearest_square(13))
    print(nearest_square(24))
    print(nearest_square(9876))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert nearest_square(8) == 9
    assert nearest_square(13) == 16
    assert nearest_square(24) == 25
    assert nearest_square(9876) == 9801
    print("Coding complete? Click 'Check' to earn cool rewards!")

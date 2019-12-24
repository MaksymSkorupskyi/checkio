"""Making Change
Nicola is taking a much needed vacation.
He'll be backpacking around some lesser-known countries.
Each has its own unique currency.

When making purchases, Nicola would like to use the minimum number of coins possible.
For example, Outer Leftopia has coins with denomination 1, 3, and 5 shillings.
He wants to buy a souvenir that costs 13 shillings.
He can do that using two 5 shilling coins and one 3 shilling coin.

You can assume Nicola has access to an infinite number of coins of each denomination.
(He has a large bank account and access to an ATM).

Input: Two arguments.
The first argument is an int: the price of the purchase.
The second is a list of ints: the denominations of available coins.

Output: int. The minimum number of coins Nicola can use to make the purchase.
If the price cannot be made with the available denominations, return None.

Example:
checkio(8, [1, 3, 5]) == 2
checkio(12, [1, 4, 5]) == 3

How it is used: Besides helping Nicola make change, this is an example of a problem in combinatorial optimization.

Precondition: Inputs are all positive integers.
"""
from typing import List, Union


def checkio(price: int,
            denominations: List[int]) -> Union[int, None]:
    """ return the minimum number of coins that add up to the price """
    table = [0] + [price + 1] * price
    for coin in denominations:
        for i in range(coin, price + 1):
            table[i] = min(table[i], table[i - coin] + 1)
    return table[price] if table[price] <= price else None


if __name__ == '__main__':
    print(checkio(4, [3, 5]))
    print(checkio(8, [1, 3, 5]))
    print(checkio(12, [1, 4]))
    print(checkio(12, [1, 4, 5]))
    print(checkio(12, [1, 2, 4, 5, 10]))
    print(checkio(123456, [1, 6, 7, 456, 678]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4, [3, 5]) is None
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    assert checkio(12, [1, 2, 4, 5, 10]) == 2
    assert checkio(123456, [1, 6, 7, 456, 678]) == 187
    print('Done')

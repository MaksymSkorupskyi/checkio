"""Create Intervals
From a set of ints you have to create a list of closed intervals as tuples,
so the intervals are covering all the values found in the set.

A closed interval includes its endpoints! The interval 1..5, for example,
includes each value x that satisfies the condition 1 <= x <= 5.

Values can only be in the same interval if the difference between a value and the next smaller value
in the set equals one, otherwise a new interval begins.
Of course, the start value of an interval is excluded from this rule.
A single value, that does not fit into an existing interval becomes the start- and endpoint of a new interval.

Input: A set of ints.
Output: A list of tuples of two ints, indicating the endpoints of the interval.
The Array should be sorted by start point of each interval

Examples:
create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]
"""

from typing import List, Set, Tuple


# v1 - straightforward iteration through sorted(data)
def create_intervals(data: Set[int]) -> List[Tuple[int, int]]:
    """ Create a list of intervals out of set of ints. """
    subset = []
    intervals = []
    for element in sorted(data):
        if not subset or subset[-1] + 1 == element:
            subset.append(element)
        else:
            intervals.append((subset[0], subset[-1]))
            subset = [element]
    if subset:
        intervals.append((subset[0], subset[-1]))
    return intervals


# v2 - `starts` and `ends` lists
def create_intervals(data: Set[int]) -> List[Tuple[int, int]]:
    """ Create a list of intervals out of set of ints. """
    starts = []
    ends = []
    for element in data:
        if element - 1 not in data:
            starts.append(element)
        if element + 1 not in data:
            ends.append(element)
    return sorted(zip(starts, ends))


# v3 - `starts` and `ends` iterators
def create_intervals(data: Set[int]) -> List[Tuple[int, int]]:
    """ Create a list of intervals out of set of ints. """
    starts = (element for element in data if element - 1 not in data)
    ends = (element for element in data if element + 1 not in data)
    return sorted(zip(starts, ends))


# v4 - `starts` and `ends` iterators two-liner
def create_intervals(data: Set[int]) -> List[Tuple[int, int]]:
    """ Create a list of intervals out of set of ints. """
    return sorted(zip((element for element in data if element - 1 not in data),
                      (element for element in data if element + 1 not in data)))


if __name__ == '__main__':
    print(create_intervals({}))
    print(create_intervals({6, 9, 1, 7}))
    print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))
    print(create_intervals({4, 5, 7, 8, 12, 4, 20, 17, 1000, 100, 21, 19, 999, 998, 14, 13, 3}))
    print(create_intervals({1, 2, 3, 4, 5, 7, 8, 12}))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    assert create_intervals({6, 9, 1, 7}) == [(1, 1), (6, 7), (9, 9)], "Third"
    print('Almost done! The only thing left to do is to Check it!')

"""Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements.
If two elements have the same frequency, they should end up in the same order
as the first appearance in the iterable.

Precondition: elements can be ints or strings

frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
"""
from collections import Counter


# 1 brute force
def frequency_sort(items: list) -> list:
    """Sort the given iterable so that its elements end up in the decreasing frequency order"""
    counter = Counter(items)
    result = []
    for element, frequency in counter.most_common():
        for i in range(frequency):
            result.append(element)
    return result


# 2 optimized
def frequency_sort(items: list) -> list:
    """Sort the given iterable so that its elements end up in the decreasing frequency order"""
    counter = Counter(items)
    result = []
    for element, frequency in counter.most_common():
        result.extend([element] * frequency)
    return result


# 3 optimized Counter comprehension
def frequency_sort(items: list) -> list:
    """Sort the given iterable so that its elements end up in the decreasing frequency order"""
    counter = Counter(items)
    return sum([[element] * frequency for element, frequency in counter.most_common()], [])


# 4 no Counter
def frequency_sort(items: list) -> list:
    """Sort the given iterable so that its elements end up in the decreasing frequency order"""
    counter = {i: items.count(i) for i in items}
    return sum([[el] * freq for el, freq in sorted(counter.items(), key=lambda x: x[1], reverse=True)], [])


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 2, 2, 2, 6, 6]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

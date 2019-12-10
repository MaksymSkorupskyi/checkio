"""Here you should find the length of the longest substring that consists of the same letter.
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa".
The last substring is the longest one, which makes it the answer.

Input: String.
Output: Int.
Example:
long_repeat('sdsffffse') == 4
long_repeat('ddvvrwwwrggg') == 3
"""


# brute force O(n)
def long_repeat(line: str) -> int:
    """ Length the longest substring that consists of the same char """
    max_count = 0
    count = 0
    previous = None
    for char in line:
        if char == previous:
            count += 1
            max_count = max(max_count, count)
        else:
            previous = char
            count = 1
    return max(max_count, count)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('abababa') == 1, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')

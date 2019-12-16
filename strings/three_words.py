"""Three Words

You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters.
You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.

Example:
checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False

How it is used: This teaches you how to work with strings and introduces some useful functions.

Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100
"""

import re


def checkio(words: str) -> bool:
    """ check if the string contains three words in succession """
    return bool(re.search('([a-zA-Z]+ ){2}[a-zA-Z]+', words))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""You are given a text, which contains different english letters and punctuation symbols.
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter,
so for the purpose of your search, "A" == "a".
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency,
then return the letter which comes first in the latin alphabet.
For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Precondition:
A text contains only ASCII symbols.
0 < len(text) ≤ 105"""

from collections import Counter


def checkio(text: str) -> str:
    """ The most frequent letter in lower case as a string """
    c = Counter([t for t in sorted(text.lower()) if t.isalpha()])
    return c.most_common()[0][0]


import string


# bryukh's solution
def checkio(text):
    """
    We iterate through latin alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    return max(string.ascii_lowercase, key=text.lower().count)


def checkio(text):
    letter_count = {ch: text.lower().count(ch) for ch in text.lower() if ch.isalpha()}
    return max(sorted(letter_count), key=letter_count.get)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

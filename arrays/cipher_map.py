"""Cipher Map

A cipher grille is a 4×4 square of paper with four windows cut out.
Placing the grille on a paper sheet of the same size,
the encoder writes down the first four symbols of his password inside the windows.
After that, the encoder turns the grille 90 degrees clockwise.
The symbols written earlier become hidden under the grille and clean paper appears inside the windows.
The encoder then writes down the next four symbols of the password in the windows and turns the grille 90 degrees again.
Then, they write down the following four symbols and turns the grille once more.
Lastly, they write down the final four symbols of the password.
Without the same cipher grille,
it is difficult to discern the password from the resulting square comprised of 16 symbols.
Thus, the encoder can be confident that no hooligan will easily gain access to the locked door.

Write a module that enables the robots to easily recall their passwords through codes when they return home.
The cipher grille and the ciphered password are represented as an array (tuple) of strings.

Input: A cipher grille and a ciphered password as a tuples of strings.
Output: The password as a string.

Example:

recall_password(
    ('X...',
     '..X.',
     'X..X',
     '....'),
    ('itdf',
     'gdce',
     'aton',
     'qrdi')) == 'icantforgetiddqd'

recall_password(
    ('....',
     'X..X',
     '.X..',
     '...X'),
    ('xhwc',
     'rsqx',
     'xqzz',
     'fyzr')) == 'rxqrwsfzxqxzhczy'

How it is used: Here you can learn how to work with 2D arrays.
You also get to learn ab    out the ancient Grille Cipher,
a technique of encoding messages which has been used for half a millenium.
The earliest known description of the grille cipher comes from the Italian mathematician, Girolamo Cardano in 1550.

Precondition: len(cipher_grille) == 4
len(ciphered_password) == 4
all(len(row) == 4 for row in ciphered_password)
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)
"""

from typing import Tuple


# v1
def recall_password(cipher_grille: Tuple[str, str, str, str],
                    ciphered_password: Tuple[str, str, str, str]) -> str:
    """ Recall a passwords from the cipher grille and the ciphered password"""

    def rotate_grille(grille: Tuple[str, ...]) -> Tuple[str, ...]:
        """ Rotate cipher grille on 90 degrees clockwise (to the right) """
        return tuple(map(''.join, (zip(*grille[::-1]))))

    first_rotation = rotate_grille(cipher_grille)
    second_rotation = rotate_grille(first_rotation)
    third_rotation = rotate_grille(second_rotation)
    full_cipher_grille = cipher_grille + first_rotation + second_rotation + third_rotation

    return ''.join(p for g, p in zip(''.join(full_cipher_grille), ''.join(ciphered_password * 4)) if g == 'X')


# v2 - optimized
def recall_password(cipher_grille: Tuple[str, str, str, str],
                    ciphered_password: Tuple[str, str, str, str]) -> str:
    """ Recall a passwords from the cipher grille and the ciphered password"""

    password = ''
    for _ in range(4):
        password += ''.join(p for g, p in zip(''.join(cipher_grille), ''.join(ciphered_password)) if g == 'X')
        cipher_grille = tuple(map(''.join, (zip(*cipher_grille[::-1]))))  # rotate cipher grille on 90 degrees clockwise

    return password


if __name__ == '__main__':
    print(recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')))
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

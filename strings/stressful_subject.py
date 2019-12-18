"""Stressful Subject

Sofia has had a very stressful month and decided to take a vacation for a week.
 To avoid any stress during her vacation she wants to forward emails with a stressful subject line to Stephen.

The function should recognise if a subject line is stressful.
A stressful subject line means that:
- all letters are in uppercase,
- and/or ends by at least 3 exclamation marks,
- and/or contains at least one of the following “red” words: "help", "asap", "urgent".
Any of those "red" words can be spelled in different ways -
"HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP,"
they just can't have any other letters interspersed between them.

Input: Subject line as a string.
Output: Boolean.

Example:

is_stressful("Hi") == False
is_stressful("I neeed HELP") == True

Precondition: Subject can be up to 100 letters
"""
import re


# v1 - static
def is_stressful(subject: str) -> bool:
    """ recognize stressful subject """
    if subject.isupper() or subject.endswith('!!!'):
        return True
    if re.search(
            r'([hH]+\W*[eE]+\W*[lL]+\W*[pP])'
            r'|([aA]+\W*[sS]+\W*[aA]+\W*[pP])'
            r'|([uU]+\W*[rR]+\W*[gG]+\W*[eE]+\W*[nN]+\W*[tT]\W*)',
            subject):
        return True
    return False


# v2 - dynamic
RED_WORDS = ('help', 'asap', 'urgent')


def is_stressful(subject: str) -> bool:
    """ recognize stressful subject """
    red = '|'.join('(' + '+\W*'.join(w) + ')' for w in RED_WORDS)
    return subject.isupper() or subject.endswith('!!!') or re.search(red, subject, re.I) is not None


if __name__ == '__main__':
    # These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") is False, "First"
    assert is_stressful("I neeed HELP") is True, "Second"
    assert is_stressful("He loves peace") is False
    assert is_stressful("Headlamp, wastepaper bin and supermagnificently") is False
    print('Done! Go Check it!')

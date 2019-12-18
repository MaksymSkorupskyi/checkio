"""Between Markers
You are given a string and two markers (the initial and final).
You have to find a substring enclosed between these two markers.
But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.

Example:

between_markers('What is >apple<', '>', '<') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'

How it is used: for parsing texts

Precondition: can't be more than one final marker and can't be more than one initial
"""


# v1 - find() and split()
def between_markers(text: str,
                    begin: str,
                    end: str) -> str:
    """ returns substring between two given markers """
    first_marker = text.find(begin) + 1
    second_marker = text.find(end) + 1
    if first_marker and second_marker and first_marker > second_marker:
        return ''
    if first_marker:
        text = text.split(begin, 1)[1]
    if second_marker:
        text = text.split(end, 1)[0]

    return text


# v2 - find() and slice
def between_markers(text: str,
                    begin: str,
                    end: str) -> str:
    """ returns substring between two given markers """

    first_marker = text.find(begin) + 1
    second_marker = text.find(end)
    if first_marker:
        first_marker += len(begin) - 1
    if second_marker == -1:
        second_marker = len(text)

    return text[first_marker:second_marker]


# v3 - find() and slice 3 lines
def between_markers(text: str,
                    begin: str,
                    end: str) -> str:
    """ returns substring between two given markers """

    first_marker = text.find(begin) + len(begin) if text.find(begin) > -1 else 0
    second_marker = text.find(end) if text.find(end) > -1 else len(text)
    return text[first_marker:second_marker]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))
    print(between_markers("No <hi> one", ">", "<"))
    print(between_markers('No [b]hi', '[b]', '[/b]'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    assert between_markers("No <hi> one", ">", "<") == ''
    print('Wow, you are doing pretty good. Time to check it!')

"""Conversion into CamelCase
Your mission is to convert the name of a function (a string)
from the Python format (for example "my_function_name")
into CamelCase ("MyFunctionName"),
where the first char of every word is in uppercase and all words are concatenated without any intervening characters.

Input: A function name as a string.
Output: The same string, but in CamelCase.

Example:
to_camel_case("my_function_name") == "MyFunctionName"
to_camel_case("i_phone") == "IPhone"
to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
to_camel_case("name") == "Name"

How it is used: To apply function names in the style in which they are adopted in a specific language
(Python, JavaScript, etc.).

Precondition:
0 < len(string) <= 100
Input data won't contain any numbers.
"""


# v1 - capitalize() + split()
def to_camel_case(function_name: str) -> str:
    """
    convert the name of a function (a string)
    from the Python format (for example "my_function_name")
    into CamelCase ("MyFunctionName")
    """
    return ''.join(s.capitalize() for s in function_name.split('_'))


# v2 - title() + replace()
def to_camel_case(function_name: str) -> str:
    """
    convert the name of a function (a string)
    from the Python format (for example "my_function_name")
    into CamelCase ("MyFunctionName")
    """
    return function_name.title().replace('_', '')


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('my_function_name'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")

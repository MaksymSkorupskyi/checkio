""" Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import Iterable


def longest_common_prefix(strings: Iterable[str]):
    """ return the longest common prefix string amongst an array of strings """
    prefix = ''
    for string in zip(*strings):
        if len(set(string)) != 1:
            break
        prefix += string[0]
    return prefix

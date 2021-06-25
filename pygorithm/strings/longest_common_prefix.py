'''
Author : Nitish Kumar (nitish771)
25-06-21
'''

from inspect import getsource


def common_word(word1, word2):
    result = ''
    l1 = len(word1)
    l2 = len(word2)
    min_len = l1 if l1 < l2 else l2
    for i in range(min_len):
        if word1[i] != word2[i]:
            break
        result += word1[i]
    return result


def longest_prefix(words: list) -> str:
    """
            Args:
                    words : List of words (min lenght = 1)
            Return:
                    str
    """

    if len(words) == 1:
        return words[0]

    if not len(words):
        return 'Please give me a list of words'

    ans = words[0]
    for word in words:
        ans = common_word(ans, word)
    return ans


def get_code():
    return getsource(longest_prefix)

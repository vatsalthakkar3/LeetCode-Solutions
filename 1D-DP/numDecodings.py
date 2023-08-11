'''
    LeetCode Problem - 91: Decode Ways 
    
    A message containing letters from A-Z can be encoded into numbers using the following mapping:

    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"
    
    To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
        -> "AAJF" with the grouping (1 1 10 6)
        -> "KJF" with the grouping (11 10 6)
    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

    Given a string s containing only digits, return the number of ways to decode it.
'''

__author__ = 'Vatsal Thakkar'
__credits__ = ['Vatsal Thakkar']
__email__ = 'vatsalthakkar3.vt@gmail.com'


def numDecodings(s: str) -> int:
    """
    The function `numDecodings` takes a string `s` as input and returns the number of possible decodings
    of the string using a recursive approach with memoization.

    :param s: The parameter `s` is a string representing a sequence of digits
    :type s: str
    :return: the number of possible decodings of the given string 's'.
    """
    dp = {len(s): 1}

    def rec(i):
        if i in dp:
            return dp[i]
        if s[i] == '0':
            return 0
        res = rec(i+1)
        if (i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456')):
            res += rec(i+2)

        dp[i] = res
        return res

    return rec(0)


test_cases = [(["12"], 2),
              (["226"], 3),
              (["06"], 0)]


def test(cases):
    flag = 0
    for i, test in enumerate(cases):
        if test[1] == numDecodings(*test[0]):
            continue
        else:
            flag += 1
            print(f"{i}th ==> {test} case Failed.")

    if flag == 0:
        print("Passed All Test Cases...😘")
    else:
        print(f"Total Test Cases Failed : {flag} / {len(cases)}")


if __name__ == "__main__":
    test(test_cases)

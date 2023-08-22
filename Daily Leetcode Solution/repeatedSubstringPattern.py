"""
    LeetCode Problem - 459. Repeated Substring Pattern

    
    Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

"""

__author__ = "Vatsal Thakkar"
__credits__ = ["Vatsal Thakkar"]
__email__ = "vatsalthakkar3.vt@gmail.com"

#######################################################################
#                            SOLUTION                                 #
#######################################################################


def repeatedSubstringPattern( s: str) -> bool:
    """
    The function checks if a given string can be formed by repeating a substring.
    
    :param s: The parameter `s` is a string that represents the input string
    :type s: str
    :return: a boolean value. It returns True if the given string can be formed by repeating a
    substring, and False otherwise.
    """
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0 and s[:i] * (n // i) == s:
            return True
    
    return False


#######################################################################
#                           SANITY CHECK                              #
#######################################################################

test_cases = [(["abab"], True), (["aba"], False), (["abcabcabcabc"], True)]


def test(cases):
    flag = 0
    for i, test in enumerate(cases):
        if test[1] == repeatedSubstringPattern(*test[0]):
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


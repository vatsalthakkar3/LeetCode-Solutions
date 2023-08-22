"""
    LeetCode Problem - 168. Excel Sheet Column Title
    
    Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

        For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
        ...
"""

__author__ = "Vatsal Thakkar"
__credits__ = ["Vatsal Thakkar"]
__email__ = "vatsalthakkar3.vt@gmail.com"

#######################################################################
#                            SOLUTION                                 #
#######################################################################


def convertToTitle(columnNumber: int) -> str:
    """
    The function `convertToTitle` takes an integer `columnNumber` and returns the corresponding column
    title in Excel.
    
    :param columnNumber: The parameter `columnNumber` represents the column number in an Excel sheet. It
    is an integer value
    :type columnNumber: int
    :return: The function `convertToTitle` returns a string.
    """
    ans=""        
    while columnNumber>0:
        c=chr(ord('A')+(columnNumber-1)%26)
        ans=c+ans
        columnNumber=(columnNumber-1)//26    
    return ans 


#######################################################################
#                           SANITY CHECK                              #
#######################################################################

test_cases = [([1], "A"), ([28], "AB"), ([701], "ZY")]


def test(cases):
    flag = 0
    for i, test in enumerate(cases):
        if test[1] == convertToTitle(*test[0]):
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


"""
    LeetCode Problem - 152: Maximum Product Subarray
       
    Given an integer array nums, find a subarray that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.
"""

__author__ = "Vatsal Thakkar"
__credits__ = ["Vatsal Thakkar"]
__email__ = "vatsalthakkar3.vt@gmail.com"

#######################################################################
#                            SOLUTION                                 #
#######################################################################


def maxProduct(nums: list[int]) -> int:
    """
    The function `maxProduct` takes in a list of integers and returns the maximum product that can be
    obtained from any contiguous subarray within the list.
    
    :param nums: The parameter `nums` is a list of integers
    :type nums: List[int]
    :return: The function `maxProduct` returns an integer, which is the maximum product that can be
    obtained from a subarray of the given list of integers.
    """
    res = max(nums)
    tempMax, tempMin = 1, 1
    for i in nums:
        tmp = i * tempMax
        tempMax = max(i*tempMax, i*tempMin,i)
        tempMin = min(tmp, i*tempMin, i)
        res = max(res, tempMax)
    
    return res


#######################################################################
#                           SANITY CHECK                              #
#######################################################################

test_cases = [([[2,3,-2,4]], 6), ([[-2,0,-1]], 0)]


def test(cases):
    flag = 0
    for i, test in enumerate(cases):
        if test[1] == maxProduct(*test[0]):
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

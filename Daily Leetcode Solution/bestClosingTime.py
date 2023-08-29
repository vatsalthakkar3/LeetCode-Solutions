"""
    LeetCode Problem - 2483. Minimum Penalty for a Shop

    You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

    -> if the ith character is 'Y', it means that customers come at the ith hour
    -> whereas 'N' indicates that no customers come at the ith hour.
    
    If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

    -> For every hour when the shop is open and no customers come, the penalty increases by 1.
    -> For every hour when the shop is closed and customers come, the penalty increases by 1.
    
    Return the earliest hour at which the shop must be closed to incur a minimum penalty.

    Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
"""
import collections

__author__ = "Vatsal Thakkar"
__credits__ = ["Vatsal Thakkar"]
__email__ = "vatsalthakkar3.vt@gmail.com"

#######################################################################
#                            SOLUTION                                 #
#######################################################################


def bestClosingTime(customers: str) -> int:
    """
    The function `bestClosingTime` calculates the best closing time for a business based on the number
    of customers who say "Yes" or "No" to staying open.

    :param customers: The `customers` parameter is a string that represents the attendance of customers
    at a store. Each character in the string represents a customer, where 'Y' indicates that the
    customer attended and 'N' indicates that the customer did not attend
    :type customers: str
    """

    count = collections.Counter(customers)
    curY, curN = count["Y"], count["N"]

    penalty, hour = curY, 0
    for i in range(0, len(customers)):
        if customers[i] == "N":
            curN -= 1
        else:
            curY -= 1
        temp_penalty = count["N"] - curN + curY
        if penalty > temp_penalty:
            penalty, hour = temp_penalty, i + 1

    return hour


#######################################################################
#                           SANITY CHECK                              #
#######################################################################

test_cases = [(["YYNY"], 2), (["NNNNN"], 0), (["YYYY"], 4)]


def test(cases):
    flag = 0
    for i, test in enumerate(cases):
        if test[1] == bestClosingTime(*test[0]):
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

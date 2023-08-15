"""
    LeetCode Problem - 322 : Coin Change
    
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

    Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    You may assume that you have an infinite number of each kind of coin.
"""

__author__ = "Vatsal Thakkar"
__credits__ = ["Vatsal Thakkar"]
__email__ = "vatsalthakkar3.vt@gmail.com"

#######################################################################
#                            SOLUTION                                 #
#######################################################################

################### BOTTOM UP DP #####################

# def coinChange(self, coins: List[int], amount: int) -> int:

#         dp = [amount+1] * (amount + 1)
#         dp[0] = 0

#         for a in range(1, amount + 1):
#             for c in coins:
#                 if a - c >= 0:
#                     dp[a] = min(dp[a], 1 + dp[a - c])
#         return dp[amount] if dp[amount] != amount + 1 else -1

################### TOP DOWN DP #####################


def coinChange(coins: list[int], amount: int) -> int:
    """
    The function `coinChange` calculates the minimum number of coins needed to make up a given amount
    using a dynamic programming approach.

    :param coins: The `coins` parameter is a list of integers representing the different denominations
    of coins available
    :type coins: list[int]
    :param amount: The amount is the target value that we want to make using the given coins
    :type amount: int
    :return: The function `coinChange` returns an integer value. If the value is less than or equal to
    10000, it returns the value. Otherwise, it returns -1.
    """
    dp = {}
    ans = helper(coins, amount, dp)
    return ans if ans <= 10000 else -1


def helper(coins, amount, dp):
    if amount in dp:
        return dp[amount]
    if amount < 0:
        return 10001
    if amount == 0:
        return 0
    dp[amount] = 1 + min([helper(coins, amount - i, dp) for i in coins])
    return dp[amount]


#######################################################################
#                           SANITY CHECK                              #
#######################################################################

test_cases = [([[1, 2, 5], 11], 3), ([[2], 3], -1), ([[1], 0], 0)]


def test(cases):
    flag = 0
    for i, test in enumerate(cases):
        if test[1] == coinChange(*test[0]):
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

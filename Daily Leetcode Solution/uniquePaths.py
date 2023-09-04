"""
    LeetCode Problem - 62. Unique Paths

    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

__author__ = "Vatsal Thakkar"
__credits__ = ["Vatsal Thakkar"]
__email__ = "vatsalthakkar3.vt@gmail.com"

#######################################################################
#                            SOLUTION                                 #
#######################################################################


def uniquePaths(m: int, n: int) -> int:
    """
    The function `uniquePaths` calculates the number of unique paths from the top-left corner to the
    bottom-right corner of a grid with dimensions `m` by `n`.

    :param m: The parameter `m` represents the number of rows in a grid
    :type m: int
    :param n: The parameter `n` represents the number of columns in the grid
    :type n: int
    :return: The function `uniquePaths` returns the number of unique paths from the top-left corner to
    the bottom-right corner of a grid with dimensions `m` x `n`.
    """

    def dfs(x, y, dp={}):
        if (x, y) in dp:
            return dp[(x, y)]
        if x == m - 1 and y == n - 1:
            return 1
        if x >= m or y >= n:
            return 0

        dp[(x, y)] = dfs(x + 1, y, dp) + dfs(x, y + 1, dp)
        return dp[(x, y)]

    return dfs(0, 0)


#######################################################################
#                           SANITY CHECK                              #
#######################################################################

test_cases = [([3, 7], 28), ([3, 2], 3)]


def test(cases):
    flag = 0
    for i, test in enumerate(cases):
        if test[1] == uniquePaths(*test[0]):
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

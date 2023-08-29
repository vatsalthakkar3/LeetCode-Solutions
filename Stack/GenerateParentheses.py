

__author__ = 'Vatsal'
__email__ = 'vatsalthakkar3.vt@gmail.com'


def generateParenthesis(n: int) -> list[str]:
    """
    The `generateParenthesis` function generates all possible valid combinations of n pairs of
    parentheses using backtracking.

    :param n: The input parameter "n" represents the number of pairs of parentheses to be generated in
    the function `generateParenthesis`
    :type n: int
    :return: The function `generateParenthesis` returns a list of strings, where each string represents
    a valid combination of parentheses of length `2n`.
    """
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res


def main():
       

    tests = [([3], ["((()))", "(()())", "(())()", "()(())", "()()()"]),
             ([1], ["()"])]

    FLAG = 0
    for i, test in enumerate(tests):
        if test[1] == generateParenthesis(*test[0]):
            continue
        else:
            FLAG += 1
            print(f"{test} case Failed.")

    if FLAG == 0:
        print("Passed All Test Cases.")
    else:
        print(f'Total Cases Failed : {FLAG}')


if __name__ == "__main__":
    print(__author__)
    main()

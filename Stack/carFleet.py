def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    # 1     3.  1.    4.   2
    # ->    ->. ->    ->.  ->

    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    # 4   2   1
    # ->  ->. ->
    lst = []
    for i in range(len(position)):
        lst.append((position[i], speed[i]))

    lst = sorted(lst, key=lambda x: x[0])
    print(lst)
    stack = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i][1] < stack[-1][1] and (lst[i][0] + (lst[i][0]-stack[-1][0])/(stack[-1][1]-lst[i][1])) < target:

            stack.append(
                (lst[i][0] + ((lst[i][0]-stack[-1][0])/(stack[-1][1]-lst[i][1])), lst[i][1]))
            stack.pop(-2)

        else:
            stack.append(lst[i])

    return len(stack)


tests = [([10, [0, 4, 2], [2, 1, 3]], 1)]

FLAG = 0
for i, test in enumerate(tests):
    if test[1] == carFleet(*test[0]):
        continue
    else:
        FLAG += 1
        print(f"{test} case Failed.")

if FLAG == 0:
    print("Passed All Test Cases.")

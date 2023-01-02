def daily_temp(arr):
    lst = [0] * len(arr)
    stack = []
    # iterate the index and value through the array
    for ind, temp in enumerate(arr):
        while stack and temp > stack[-1][0]:
            # pop two element from stack
            stackTemp, stackInd = stack.pop()
            # insert index value in list
            lst[stackInd] = (ind - stackInd)
        # insert value of temp and its index into the stack
        stack.append([temp, ind])
    # print list value
    return lst


print(daily_temp([30, 40, 50, 60]))
print(daily_temp([30, 60, 90]))
print(daily_temp([73, 74, 75, 71, 69, 72, 76, 73]))

# complexity = O(N)

def minNumberOfJumps(arr):  # complexity = O(n)
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1
    end, maxReach, jumps = 0, 0, 0
    for idx, val in enumerate(arr[:-1]):
        maxReach = max(maxReach, idx + val)
        if idx == end:
            jumps += 1
            end = maxReach
    return jumps if end >= n - 1 else -1


print(minNumberOfJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
print(minNumberOfJumps([1, 4, 3, 2, 6, 7]))

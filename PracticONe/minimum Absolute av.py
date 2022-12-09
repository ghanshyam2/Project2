def minAbsAvg(nums):
    minAvg = float('inf')
    left = 0
    right = 0
    res = 0
    s = sum(nums)

    for i, num in enumerate(nums):
        left += num
        right = s - left
        if i != len(nums) - 1:
            if abs(left // (i + 1) - right // (len(nums) - i - 1)) < minAvg:
                minAvg = abs(left // (i + 1) - right // (len(nums) - i - 1))
                res = i
        else:
            if left // (i + 1) < minAvg:
                res = i

    return res


print(minAbsAvg([2, 5, 3, 9, 5, 3]))
print(minAbsAvg([0]))

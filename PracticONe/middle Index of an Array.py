def middleIndex(nums):
    left = 0
    right = sum(nums)

    for i, num in enumerate(nums):
        if left == right - num:
            return i

        left += num
        right -= num
    return -1


print(middleIndex([3, 2, -1, 8, 4]))
print(middleIndex([1, -1, 4]))
print(middleIndex([2, 5]))

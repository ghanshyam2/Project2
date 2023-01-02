def max_min(nums):
    left, right = 0, len(nums) - 1
    ar = [0]* len(nums)

    flag = True

    for i in range(len(nums)):
        if flag is True:
            ar[i] = nums[right]
            right -= 1
        else:
            ar[i] = nums[left]
            left += 1
        flag = bool(1-flag)
    for i in range(len(nums)):
        nums[i] = ar[i]
    return ar


print(max_min([1, 2, 3, 4, 5, 6]))

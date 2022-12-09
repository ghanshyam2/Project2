def searchDuplicate(nums):
    lis = []
    nums.sort()
    for i in range(1, len(nums) - 1):

        if nums[i] == nums[i - 1]:
            lis.append(nums[i])
    return lis


print(searchDuplicate([1, 3, 2, 4, 4, 5, 6, 7, 6, 2]))
print(searchDuplicate([1, 2, 3, 4, 5, 3, 1]))

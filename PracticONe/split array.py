def splitArray(nums):
    s_um = 0
    sum_ = 0
    n = nums[:len(nums) // 2]
    m = nums[len(nums) // 2:]
    for i in n:
        s_um += i
    for i in m:
        sum_ += i
    return (s_um // len(n)) == (sum_ // len(m))


print(splitArray([1, 2, 3, 4, 5, 6, 7, 8]))
print(splitArray([1,2,3,4]))

# incomplete

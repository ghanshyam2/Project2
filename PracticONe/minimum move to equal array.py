def min_move_equal_array(nums):
    min_nums = min(nums)
    ret = 0
    for i in nums:
        ret += i - min_nums
    return ret


print(min_move_equal_array([1,2,3]))
print(min_move_equal_array([1,1,1]))
print(min_move_equal_array([2,4,6]))

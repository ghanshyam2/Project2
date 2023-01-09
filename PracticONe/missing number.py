def missing_number(arr):
    ans = 0

    while ans in arr:
        ans += 1
    return ans


print(missing_number([1,2]))

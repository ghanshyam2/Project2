def revList(arr):
    lis = []
    arr.sort()
    for ar in arr[::-1]:
        lis.append(ar)
    return lis


print(revList([1, 2, 3, 4, 5]))
print(revList([2, 3, 1, 4, 5, 8]))

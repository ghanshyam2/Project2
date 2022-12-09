def ternarySearch(arr, key):
    left, right = 0, len(arr)-1
    while left < right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if key == arr[mid1]:
            return mid1
        if key == mid2:
            return mid2
        if key < arr[mid1]:
            right = mid1 - 1
        elif key > arr[mid2]:
            left = mid2 + 1
        else:
            right = mid2 - 1
            left = mid1 + 1
    return -1


print(ternarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(ternarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50))
print(ternarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))

def search_insert_position(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    if target > arr[-1]:
        return len(arr)

    while left <= right:
        mid = left + (right - left) // 2
        if target == arr[mid]:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid
    return ans


print(search_insert_position([1, 2, 3, 4, 6], 5))

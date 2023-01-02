def FirstNonRepeat(arr):
    for i in range(len(arr)):
        j = 0

        while j < len(arr):
            if i != j and arr[i] == arr[j]:
                break
            j += 1
        if j == len(arr):
            return arr[i]
    return -1


print(FirstNonRepeat([9, 4, 9, 6, 7, 4]))
print(FirstNonRepeat([1, 5, 9, 2, 1, 3, 2, 6, 6, 3, 7, 2, 8, 9, 4]))
print(FirstNonRepeat([1, 4, 9, 2, 1, 3, 2, 6, 6, 3, 7, 2, 8, 9, 4]))

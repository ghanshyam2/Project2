def lessThanItself(arr1, arr2):
    lis = []
    arr2.sort()
    for i in range(len(arr1)):

        count = 0
        for j in range(len(arr2)):
            if arr1[i] >= arr2[j]:
                count += 1
            if arr1[i] < arr2[j]:
                break
        lis.append(count)
    return lis


print(lessThanItself([1, 2, 3, 4, 5,6], [0, 1, 1, 2, 1, 1, 4]))

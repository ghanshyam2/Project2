def bubbleSort(arr):
    # traverse through loop
    for i in range(len(arr)):
        #  traverse through the size of array less than the index-1
        for j in range(0, len(arr) - i - 1):
            # compare j to the next value of j
            if arr[j + 1] < arr[j]:
                # then swap the element between each other
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    test_cases = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for tests in test_cases:
        bubbleSort(tests)
        print(tests)

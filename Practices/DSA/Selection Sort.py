def selectionSort(arr):
    for i in range(len(arr)):
        # assign first index as min value
        min_index = i
        # reverse it to the whole loop
        for j in range(min_index + 1, len(arr)):
            # then find the lowest value in arr
            if arr[j] < arr[min_index]:
                # assign that index as min index
                min_index = j
        # then compare it to the assigned value, whether it is not equal
        if i != min_index:
            # at last swap min index value to the first value
            arr[i], arr[min_index] = arr[min_index], arr[i]

    # return arr


# complexity = O(n2)
if __name__ == "__main__":
    test_cases = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for tests in test_cases:
        selectionSort(tests)
        print(tests)

def even_grater_than_odd(arr):
    for i in range(len(arr)):

        if i % 2 == 0:
            if arr[i] > arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        else:
            if arr[i] < arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    return arr


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
        even_grater_than_odd(tests)
        print(tests)

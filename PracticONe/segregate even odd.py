def seg_even_odd(arr):
    a = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[a] = arr[a], arr[i]
            a += 1
    return arr


if __name__ == "__main__":
    test_cases = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [1, 5, 8, 6, 10, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for tests in test_cases:
        seg_even_odd(tests)
        print(tests)

def nextLetter(letters, key):
    n = len(letters)
    if key < letters[0] or key > letters[n-1]:
        return letters[0]
    left, right = 0, n - 1
    while left <= right:
        mid = left + (right - left) // 2

        if key < letters[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return letters[left % n]


print(nextLetter(['a', 'c', 'f', 'h'], 'f'))
print(nextLetter(['a', 'c', 'f', 'h'], 'b'))
print(nextLetter(['a', 'c', 'f', 'h'], 'm'))

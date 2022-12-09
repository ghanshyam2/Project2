def listTup(arr):
    return [(val, val ** 3) for val in arr]


print(listTup([5, 6, 7]))
for i in range(3):
    for j in range(0, i+1):
        print("*", end='')
    print()
for i in range(3):
    for j in range(i, 2):
        print("*", end='')
    print()

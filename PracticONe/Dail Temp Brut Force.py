def dailyTemp_Brute(arr):
    lst = [0] * len(arr)

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                lst[i] = j - 1
                break
    return lst


print(dailyTemp_Brute([30, 40, 50, 60]))
print(dailyTemp_Brute([30, 60, 90]))
print(dailyTemp_Brute([73, 74, 75, 71, 69, 72, 76, 73]))

# wrong answer

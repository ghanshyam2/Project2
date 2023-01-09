def sub_array_sum(arr, k):
    total = 0
    count = 0
    dp = {0: 1}

    for i in range(len(arr)):
        total += arr[i]

    if total % k in dp:
        count += dp[total % k]

    if total in dp:
        dp[total] += 1
    else:
        dp[total] = 1
    return count


print(sub_array_sum([4, 5, 0, -2, -3, 1], 5))

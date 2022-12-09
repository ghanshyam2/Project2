def mostEvenFreq(arr):
    val, frq = 10 ** 6, 0
    dic = {}
    for i in arr:
        if i % 2 == 0:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
            if dic[i] > frq or dic[i] == frq and i < val:
                val, frq = i, dic[i]

    return -1 if frq == 0 else val


print(mostEvenFreq([1, 2, 2, 4, 4, 1, 3]))

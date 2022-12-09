def sortCharByFreq(s):
    dic = {}

    for st in s:
        if st in dic:
            dic[st] += 1
        else:
            dic[st] = 1
    # return dic
    items = sorted(dic.items(), key=lambda k: k[1], reverse=True)
    str_ = ""
    for item in items:
        if item != 0:
            str_ += item[0] * item[1]
    return str_


print(sortCharByFreq("tree"))
print(sortCharByFreq("paneling"))

def string_con(str1, str2):
    str3 = ""
    a = 0
    for i in range(1, len(str1)):

        if i == int(str1[a]):
            if (i + a) <= len(str2):
                if i != 3:
                    str3 += str2[a:i + a] + str1[a]
                    a += 1
                else:
                    str3 += str1[a] + str2[i:len(str1)]
                    a += 1
        else:
            str3 += str1[a:len(str2)]
    return str3


print(string_con("123456", "abcdef"))
#print(string_con("1234567","abcdefg"))

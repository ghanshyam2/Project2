def rremove(S):
    str_ = ""
    i = 0
    a = 1
    while i < len(S)-1:
        if S[i] != S[i]:
            str_ += S[i]
        else:
            while S[i] == S[i+1]:
                i += 1

        i += 1

    if str_ == S:
        return S
    else:
        return rremove(str_)


print(rremove("forgetfulness"))

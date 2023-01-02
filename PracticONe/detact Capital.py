def detectCapital(string):
    counts = 0

    for s in string:
        if s.isupper():
            counts += 1
    if counts == 0:
        return True
    if counts == len(string):
        return True
    if counts == 1 and string[0].isupper():
        return True
    return False


print(detectCapital("USA"))
print(detectCapital("leeTcode"))
print(detectCapital("PaininG"))

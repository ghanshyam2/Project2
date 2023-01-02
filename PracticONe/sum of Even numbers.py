def sum_of_even_number():
    num = int(input())
    temp = 0
    for i in range(num):
        if i % 8 == 0:
            temp += i
    print(temp)


sum_of_even_number()

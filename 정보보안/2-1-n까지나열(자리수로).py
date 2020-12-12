def where_is_n(n):
    sum = 0
    jali = 10
    num_len = 1
    while n > 0:
        namozi = n % jali
        print(namozi)
        sum += namozi
        n -= namozi
        jali *= 10
        num_len += 1
    return sum


print(where_is_n(12345))

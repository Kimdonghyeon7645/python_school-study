def where_is_n(n):
    jali = 1
    sum = 0
    while True:
        print(n, jali, sum)
        if n > 9:
            sum += ((10**jali-1) * jali)
            print(sum)
            n //= 10
            jali += 1
        else:
            sum += (n % 10) * (jali*10)*jali
            break
    return sum


print(where_is_n(20))

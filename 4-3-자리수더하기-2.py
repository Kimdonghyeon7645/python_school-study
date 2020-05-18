def plus(sum, num):
    if not num:
        return sum
    sum += int(num[-1])
    return plus(sum, num[:-1])


print(plus(0, input()))

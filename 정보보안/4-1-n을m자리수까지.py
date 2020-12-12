def n_and_m(n, m):
    sum = 0
    for i in range(1, m+1):
        sum += int(f'{n}' * i)
    return sum


a, b = map(int, input().rstrip().split(' '))
print(n_and_m(a, b))

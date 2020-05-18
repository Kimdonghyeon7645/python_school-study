def where_is_n(n):
    sum = ''
    for i in range(1, n+1):
        sum += str(i)
    return sum[n-1]


print(where_is_n(2020))
# 문제를 잘못읽고 어려운 내용에서 삽질하고 있었습니다. ^^;;
# 마찬가지로 자리수로 구해보는 문제도 해결해 보겠습니다!

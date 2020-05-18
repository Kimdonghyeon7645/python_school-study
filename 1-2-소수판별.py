def are_you_sosu(n: int) -> str:
    for i in range(2, n):
        if n % i == 0:
            return '합성수입니다.'
    return '소수입니다.'


print(are_you_sosu(int(input())))

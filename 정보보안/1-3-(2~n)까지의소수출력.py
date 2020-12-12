from typing import NoReturn


def are_you_sosu(n: int) -> NoReturn:
    """
    :param n:   2 ~ n 까지의 숫자를 대상
    :return:    없음, 2 ~ n 까지의 숫자가 소수 or 합성수 인지 출력.
    """
    for m in range(2, n+1):
        for i in range(2, m+1):
            if i == m:
                print(f"{m}은 소수 입니다.")
                break
            elif m % i == 0:
                print(f"{m}은 합성수 입니다.")
                break


are_you_sosu(int(input()))

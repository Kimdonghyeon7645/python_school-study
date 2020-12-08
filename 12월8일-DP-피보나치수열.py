import time
"""
메모리제이션(memoization)
= 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 
  동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술
"""
n = 35


# 1. 일반 방식, 재귀함수만으로 구현
def common_fibonacci(i):
    if i < 3:
        return 1
    return common_fibonacci(i-1) + common_fibonacci(i-2)


start = time.time()
print(common_fibonacci(n))
end = time.time()
print(end - start)


# 2. Top Down = 가장 큰 문제들부터 작은 문제들을 호출하여 답을 찾는 방식 (재귀함수에 메모리제이션을 추가해 구현)
def top_down_fibonacci(i):
    if i < 3:
        return li[-1]
    li.append(li[n-i+1]+li[n-i])
    return top_down_fibonacci(i-1)


li = [1, 1]
start = time.time()
print(top_down_fibonacci(n))
end = time.time()
print(end - start)


# 3. Bottom Up = 가장 작은 문제들부터 전체 문제까지로 답을 찾는 방식 (반복문으로 구현)
def bottom_up_fibonacci(i):
    i1, i2 = 1, 1
    for _ in range(2, i):
        i1, i2 = i2, i1 + i2
    return i2


start = time.time()
print(bottom_up_fibonacci(n))
end = time.time()
print(end - start)

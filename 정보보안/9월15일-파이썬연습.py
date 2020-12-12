# 3가지 수 입력받아 변수들로 출력
a, b, c = map(int, input().rstrip().split())
print(a, b, c)

# n가지 수 입력받아 리스트로 출력
li1 = list(map(int, input().rstrip().split()))
li2 = [int(i) for i in input().rstrip().split()]    # 리스트 표현식을 활용
print(li1)
print(li2)

# 1~1000 리스트중 3의 배수 삭제
print([i for i in range(1, 1001) if i % 3 != 0])
print(set(range(1, 1001)) - set(range(3, 1001, 3)))

# 2차원 배열
print([[0]*3 for _ in range(3)])

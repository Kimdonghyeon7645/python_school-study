def solution(participant, completion):
    key_sum = 0
    table = dict()

    for i in participant:
        table[hash(i)] = i
        key_sum += hash(i)
    for i in completion:
        key_sum -= hash(i)

    return table[key_sum]


# 테스트 코드
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

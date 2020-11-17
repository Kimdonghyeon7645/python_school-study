def solution(participant, completion):
    answer = dict()     # 해시 테이블로 활용할 딕셔너리 생성
    for ele in participant:
        if ele in answer:
            answer[ele] += 1
        else:
            answer.update({ele: 1})
    for ele in completion:
        if answer[ele] > 1:
            answer[ele] -= 1
        else:
            answer.pop(ele)
    print(*answer.items())
    return list(answer.keys())[0]


# 테스트 코드
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

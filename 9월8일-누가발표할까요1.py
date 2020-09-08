import random

student_count = 20
lst = ['선택정렬', '삽입정렬', '버블정렬', '퀵정렬', '병합정렬', '해시', '스택', '큐', '힙', '탐욕(그리디)', '그래프', '동적계획(DP)',
       '이분탐색', '완적탐색(BF)', '너비우선탐색(BFS)', '깊이우선탐색(DFS)']
random.shuffle(lst)
sub_lst = lst[:student_count - len(lst)]
random.shuffle(sub_lst)
# print(dict(zip([i for i in range(1, student_count)], lst+sub_lst)))   딕셔너리로 출력할 때
for k, v in zip([i for i in range(1, student_count)], lst+sub_lst):
    print(f"{k}번 학생 : {v} 발표")

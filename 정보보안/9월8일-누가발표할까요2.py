import random
student_count = 20
lst = ['선택정렬', '삽입정렬', '버블정렬', '퀵정렬', '병합정렬', '해시', '스택', '큐', '힙', '탐욕(그리디)', '그래프', '동적계획(DP)',
       '이분탐색', '완적탐색(BF)', '너비우선탐색(BFS)', '깊이우선탐색(DFS)']


# 선생님의 파일을 활용한 방법
random.shuffle(lst)
sub_lst = lst[:student_count - len(lst)]
random.shuffle(sub_lst)
lst += sub_lst  # 이렇게 되면 lst는 겹침을 최소화한 하나의 가로 열이 됩니다.

pre_list = [['']] * student_count
print(pre_list[0])
with open('../list.txt', 'r+') as f:
    for line in f.readlines():
        print(line[:-1].split(','))
        for i, n in enumerate(line[:-1].split(',')):
            print(i, n)
            pre_list[i].append(n)
        print(pre_list)
print(pre_list)
# for i in range(len(lst)):
#     hey = random.choice(lst)
#     if hey in

with open('../list.txt', 'a') as f:
    f.write(','.join(lst)+'\n')

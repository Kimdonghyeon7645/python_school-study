# def solution(number, k):
#     for _ in range(k):
#         number = ''.join(number.split(min(number), 1))
#         print(number)
#     return number
""" 시간 복잡도 별로... """


# def solution(number, k):
#     l_num, r_num = [], list(reversed(number))
#     for _ in range(k):
#         print(l_num, r_num)
#         for _ in range(len(r_num)-1):
#             item = r_num.pop()
#             if item < r_num[-1]:
#                 break
#             else:
#                 l_num.append(item)
#     return ''.join(l_num + r_num)
""" l_num에 보내버린 값은 더이상 검사 못함... """


# def solution(number, k):
#     num = list(number)
#     for _ in range(k):
#         for i in range(1, len(num)):
#             if num[i-1] < num[i]:
#                 del num[i-1]
#                 break
#             elif i == len(num)-1:
#                 del num[i]
#     return ''.join(num)
""" 통과는 다 되는데 시간 초과... """




# 테스트 코드
print(solution('1924', 2))
print(solution("4177252841", 4))
print(solution("99991", 3))
print(solution("999", 2))

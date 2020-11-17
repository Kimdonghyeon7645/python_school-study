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


# def solution(number, k):
#     num = list(reversed(number))
#     for _ in range(k):
#         l_list, r_list = [], num
#         for _ in range(len(r_list)):
#             item = r_list.pop()
#             if not r_list or item < r_list[-1]:
#                 break
#             else:
#                 l_list.append(item)
#         print(l_list, r_list, "오", ''.join(l_list+r_list))
#         num = num + list(reversed(l_list))
#     return ''.join(list(reversed(num)))
""" 이렇게 개고생했는데 역시 시간 초과... """


def solution(number, k):    # 결국 인터넷... 너무 깔끔한 정석같은 코드
    stack = [number[0]]
    for num in number[1:]:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)
"""
약이 머리끝까지 올랐다.
https://eda-ai-lab.tistory.com/465?category=766271
용을 썼는데도 안풀리는 것을 주변에선 누어서 떡먹기로 풀고 있으니...
오늘은 집에 안간다.
"""


# 테스트 코드
print(solution('1924', 2))
print(solution('1231234', 3))
print(solution("4177252841", 4))
print(solution("99991", 3))
print(solution("999", 2))

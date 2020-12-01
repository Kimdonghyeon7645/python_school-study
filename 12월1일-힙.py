# 참고 : https://www.daleseo.com/python-heapq/
import heapq

li = []     # 기본 리스트 -> 이것을 heapq 모듈로 최소힙처럼 사용할 거임

"""
원소 추가 : heapq.heappush(리스트, 추가할원소)
"""
heapq.heappush(li, 4)
heapq.heappush(li, 1)
heapq.heappush(li, 2)
heapq.heappush(li, 6)
print(li)

"""
(최소값의) 원소 삭제 : heapq.heappop(리스트)
"""
heapq.heappop(li)
print(li)

"""
최소값 삭제(pop)하지 않고 구하기 : 리스트[0]
(인덱스 0이 최소값이라 해서 인덱스 1, 2가 두번째, 세번째 작은 원소가 아님 (힙 = 느슨한 정렬))
"""
print(li[0])

"""
기존 리스트 -> 힙 : heapq.heapify(리스트)
"""
target_li = [8, 4, 3, 2]
heapq.heapify(target_li)
print(target_li)

"""
(응용) 최대힙
(힙의 원소로 튜플이 들어가면, 튜플의 첫번째 원소로 정렬하는 것을 이용)
"""
nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)
print(nums, "->", [i[1] for i in heap])

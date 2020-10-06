li = list(map(int, input("정렬할 배열을 입력하세요. (띄어쓰기로 구분): ").rstrip().split()))
sorted_li, not_sorted_li = [li[0]], li[1:]

for count in range(len(not_sorted_li)):
    key = not_sorted_li.pop(0)
    for i, n in enumerate(sorted_li):
        if key < n:
            sorted_li.insert(i, key)
            break
    print(f"{count}번째 정렬 결과 :", sorted_li + not_sorted_li)

print("최종 정렬 결과 :", sorted_li)



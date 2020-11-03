def solution(phone_book):
    hash_map = dict().fromkeys(phone_book)
    for number in phone_book:
        temp = ""
        for i in number:
            temp += i
            if temp in phone_book and temp != number:
                return False
    return True


# 테스트 코드
print(solution(["119", "97674223", "1195524421"]))


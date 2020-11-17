class HashTable:
    def __init__(self):
        self.table = dict()

    def __str__(self):
        if self.table:
            return list(self.table.keys())[0]
        else:
            return None

    def __setitem__(self, key, value=1):
        if key not in self.table:
            self.table.update({key: value})
        else:
            self.table[key] += 1

    def __delitem__(self, item):
        if item not in self.table:
            return None
        elif self.table[item] > 1:
            self.table[item] -= 1
        else:
            del self.table[item]


def solution(participant, completion):
    table = HashTable()
    for i in participant:
        table[i] = 1
    for i in completion:
        del table[i]
    return str(table)


# 테스트 코드
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

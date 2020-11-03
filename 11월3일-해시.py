lst = [chr(i) for i in range(65, 91)]
print(lst)
for i in lst:
    print(f"{i} : {hash(i)}")

for i in ["A", "A"]:
    print(f"{i} : {hash(i)}")       # 같은 값은 같은 해시값

for i in ['Ab', 'AB', "Ac"]:
    print(f"{i} : {hash(i)}")


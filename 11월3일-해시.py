lst = [chr(i) for i in range(65, 91)]
print(lst)
for i in lst:
    print(f"{i} : {hash(i)}")

lst2 = ["A", "A"]
for i in lst2:
    print(f"{i} : {hash(i)}")

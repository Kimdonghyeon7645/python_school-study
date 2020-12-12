n = int(input())
out_li = []
for i in range(n):
    li = list(input())
    sum = count = 0
    for n in li:
        if n == 'X':
            count = 0
        elif n == 'O':
            count += 1
            sum += count
    out_li.append(sum)

for out in out_li:
    print(out)

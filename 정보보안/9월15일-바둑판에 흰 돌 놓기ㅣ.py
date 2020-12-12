pan = [[0]*19 for _ in range(19)]
for _ in range(int(input())):
    x, y = map(int, input().strip().split())
    pan[x-1][y-1] = 1
print(*[' '.join(map(str, i)) for i in pan], sep='\n')

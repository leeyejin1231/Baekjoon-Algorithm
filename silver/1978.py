import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
res = 0

for i in lst:
    check = True
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                check = False
                break
        if check:
            res += 1
print(res)
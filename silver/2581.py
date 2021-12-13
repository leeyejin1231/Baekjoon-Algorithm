import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
so = []
for i in range(M, N+1):
    check = False
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                check = True
                break
        if check == False:
            so.append(i)
if len(so) == 0:
    print(-1)
else:
    print(sum(so))
    print(min(so))
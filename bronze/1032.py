N = int(input())
arr = []
n = 0
res = []

for i in range(N):
    arr.append(str(input()))

for i in arr[0]:
    c = 0
    for j in range(N):
        if arr[j][n] == i:
            c += 1;
    if c == N:
        res.append(i)
    else:
        res.append("?")
    n += 1

for i in range(len(res)):
    print(res[i], end='')
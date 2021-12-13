n = int(input())
c = list(map(int, input().split()))
res = 0
for i in c:
    if n == i:
        res += 1
print(res)
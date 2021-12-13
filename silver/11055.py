n = int(input())
l = list(map(int, input().split()))
temp = []
res = 0

for i in range(n-1):
    if l[i] < l[i+1]:
        temp.append(l[i])
    else:
        temp.append(l[i])
        if res < sum(temp):
            res = sum(temp)
            print(res)

print(res)

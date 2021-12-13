def check(li):
    s = [False for i in range(n)]
    for i in range(n-1):
        if li[i] == li[i+1]:
            continue
        elif abs(li[i] - li[i+1])>1:
            return False
        if li[i] > li[i+1]:
            temp = li[i+1]
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if li[j] != temp: return False
                    if s[j] == True: return False
                    s[j] = True
                else:
                    return False
        else:
            temp = li[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if li[j] != temp: return False
                    if s[j] == True: return False
                    s[j] = True
                else:
                    return False
    return True

n, l = map(int, input().split())
mapp = []
res = 0



for i in range(n):
    mapp.append(list(map(int, input().split())))

for i in mapp:
    if(check(i)):
        res += 1
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(mapp[j][i])
    if check(temp):
        res += 1;

print(res)
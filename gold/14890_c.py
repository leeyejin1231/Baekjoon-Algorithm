def check(li):
    sw = [False for i in range(n)]
    for i in range(n - 1):
        if li[i] == li[i + 1]:
            continue
        if abs(li[i] - li[i + 1]) > 1:
            return False
        if li[i] > li[i + 1]:
            temp = li[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    if li[j] != temp: return False
                    if sw[j] == True: return False
                    sw[j] = True
                else:
                    return False
        else:
            temp = li[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if li[j] != temp: return False
                    if sw[j] == True: return False
                    sw[j] = True
                else:
                    return False
    return True
    
n, l = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
cnt = 0
for i in s:
    if check(i):
        cnt += 1
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(s[j][i])
    if check(temp):
        cnt += 1
print(cnt)
n = int(input())
res = 0
while(n>=0):
    if n%5 == 0:
        print(res+n//5)
        break
    else:
        n -= 3
        res += 1
else:
    print(-1)
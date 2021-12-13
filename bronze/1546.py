n = int(input())
s = list(map(int, input().split()))
m = max(s)
for i in range(n):
    s[i] = s[i]/m*100
print((sum(s))/n)
n = int(input())
res = 0

for i in range(1, n+1):
    if i<100:
        res += 1
    elif (i//100 - ((i%100)//10)) == (((i%100)//10) - i%10):
        res += 1

print(res)


arr = set(range(1, 10001))
res = set()

for a in arr:
    # while a < 10001:
    #     a = a + (a//1000) + (a//100) + (a//10) + (a%10)
    #     res.add(a)
    for j in str(a):
        a += int(j)
    res.add(a)

result = sorted(arr-res)
for i in result:
    print(i)
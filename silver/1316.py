N = int(input())
arr = []
res = 0;

for i in range(N):
    word = list(input())
    arr.append(word)

for i in range(N):
    b = ""
    check = set()
    group = True
    for j in arr[i]:
        if j == b:
            continue
        else:
            if (j not in check)==True:
                check.add(j)
            else: 
                group = False
        b = j
    if group == True:
        res += 1;

print(res)
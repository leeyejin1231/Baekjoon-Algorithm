from ast import Index

a = list(input().upper())
A = set(a)
aa = list(A)
cnt = []

for i in aa:
   cnt.append(a.count(i))

max = max(cnt)
if cnt.count(max) == 1:
    print(aa[cnt.index(max)])
else:
    print("?")
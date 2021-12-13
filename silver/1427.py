n = int(input())
list = []
while(n>0):
    list.append(n%10)
    n = n//10
list = sorted(list, reverse=True)
for i in list:
    print(i, end='')

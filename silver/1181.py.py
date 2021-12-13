import sys
n = int(input())
llist = []
for i in range(n):
    llist.append(sys.stdin.readline())
llist = set(llist)
llist = list(llist)
llist.sort()
llist.sort(key=len)
for i in llist:
    print(i, end='')
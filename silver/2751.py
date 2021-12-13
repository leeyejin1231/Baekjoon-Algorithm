import sys
n = int(input())
list = []
for i in range(n):
    list.append(int(sys.stdin.readline()))
list = sorted(list)
for i in list:
    print(i)
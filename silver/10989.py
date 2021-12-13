import sys
n = int(sys.stdin.readline())
list = [0]*10001
for i in range(n):
    m = (int(sys.stdin.readline()))
    list[m] += 1
    
for i in range(len(list)):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)
import sys

n = int(sys.stdin.readline())
m = []

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        m.pop()
    else:
        m.append(num)

print(sum(m))

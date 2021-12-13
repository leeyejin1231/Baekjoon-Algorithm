import sys
from collections import deque

input = sys.stdin.readline

def check_right(n, r):
    if n > 4 or top[n][6] == top[n-1][2]:
        return
    
    if top[n][6] != top[n-1][2]:
        check_right(n+1, -r)
        top[n].rotate(r)


def check_left(n, r):
    if n < 1 or top[n][2] == top[n+1][6]:
        return
    
    if top[n][2] != top[n+1][6]:
        check_left(n-1, -r)
        top[n].rotate(r)


top = {}
for i in range(1,5):
    top[i] = deque(map(int, input().replace("\n", "")))

n = int(input())

for i in range(n):
    n, r = map(int, input().split())
    check_right(n+1, -r)
    check_left(n-1, -r)
    top[n].rotate(r)

result = 0
for i in range(4):
    result += (2**i) * top[i+1][0]

print(result)



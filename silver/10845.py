import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    lst = sys.stdin.readline().split()
    if lst[0] == 'push':
        queue.append(lst[1])
    elif lst[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft()) 
    elif lst[0] == 'size':
        print(len(queue))
    elif lst[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif lst[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif lst[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

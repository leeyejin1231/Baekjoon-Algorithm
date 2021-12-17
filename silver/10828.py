import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    lst = sys.stdin.readline().split()
    if lst[0] == 'push':
        stack.append(lst[1])
    elif lst[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif lst[0] == 'size':
        print(len(stack))
    elif lst[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif lst[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
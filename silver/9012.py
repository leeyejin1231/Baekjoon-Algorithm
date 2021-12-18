import sys

n = int(sys.stdin.readline())

for i in range(n):
    lst = sys.stdin.readline()
    open = 0
    close = 0
    check = True
    for j in lst:
        if j == '(':
            open += 1
        elif j == ')':
            close += 1
            if open < close:
                print('NO')
                check = False
                break
    if open == close:
        print('YES')
    else:
        if check:
            print('NO')

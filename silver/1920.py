import sys

n = sys.stdin.readline()
a = set(sys.stdin.readline().split())
m = sys.stdin.readline()
mm = sys.stdin.readline().split()

for i in mm:
    # if i in a:
    #     print(1)
    # else:
    #     print(0)
    print(1 if i in a else 0)

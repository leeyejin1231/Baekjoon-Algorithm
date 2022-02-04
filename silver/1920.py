import sys

n = sys.stdin.readline()
a = set(sys.stdin.readline().split())
m = sys.stdin.readline()
mm = sys.stdin.readline().split()

for i in mm:
    print(1 if i in a else 0)
